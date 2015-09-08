# Copyright 2014 Cloudera Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import

import six
import time
import getpass
import datetime
import socket
import operator
import re
from six.moves import range
from bitarray import bitarray


from impala.compat import lzip, Decimal
from impala.util import get_logger_and_init_null
from impala.interface import Connection, Cursor, _bind_parameters
from impala.error import NotSupportedError, OperationalError, ProgrammingError


from impala.error import HiveServer2Error
from impala._thrift_api import (
    get_socket, get_transport, TTransportException, TBinaryProtocol)
from impala._thrift_api.hiveserver2 import (
    TOpenSessionReq, TFetchResultsReq, TCloseSessionReq, TExecuteStatementReq,
    TGetInfoReq, TGetInfoType, TTypeId, TFetchOrientation,
    TGetResultSetMetadataReq, TStatusCode, TGetColumnsReq, TGetSchemasReq,
    TGetTablesReq, TGetFunctionsReq, TGetOperationStatusReq, TOperationState,
    TCancelOperationReq, TCloseOperationReq, TGetLogReq, TProtocolVersion,
    TGetRuntimeProfileReq, TGetExecSummaryReq, ImpalaHiveServer2Service,
    TExecStats, ThriftClient)


log = get_logger_and_init_null(__name__)


class HiveServer2Connection(Connection):
    # PEP 249
    # HiveServer2Connection objects are associated with a TCLIService.Client
    # thrift service
    # it's instantiated with an alive TCLIService.Client

    def __init__(self, service, default_db=None):
        log.debug('HiveServer2Connection(service=%s, default_db=%s)', service,
                  default_db)
        self.service = service
        self.default_db = default_db

    def close(self):
        """Close the session and the Thrift transport."""
        # PEP 249
        log.info('Closing HS2 connection')
        close_service(self.service)

    def commit(self):
        """Impala doesn't support transactions; does nothing."""
        # PEP 249
        pass

    def rollback(self):
        """Impala doesn't support transactions; raises NotSupportedError"""
        # PEP 249
        raise NotSupportedError

    def cursor(self, session_handle=None, user=None, configuration=None):
        # PEP 249
        log.info('Getting a cursor (Impala session)')
        if user is None:
            user = getpass.getuser()
        if session_handle is None:
            log.debug('.cursor(): getting new session_handle')
            (session_handle, default_config, hs2_protocol_version) = (
                open_session(self.service, user, configuration))
        cursor = HiveServer2Cursor(
            self.service, session_handle, default_config, hs2_protocol_version)
        if self.default_db is not None:
            log.info('Using database %s as default', self.default_db)
            cursor.execute('USE %s' % self.default_db)
        return cursor

    def reconnect(self):
        reconnect(self.service)


class HiveServer2Cursor(Cursor):
    # PEP 249
    # HiveServer2Cursor objects are associated with a Session
    # they are instantiated with alive session_handles

    def __init__(self, service, session_handle, default_config=None,
                 hs2_protocol_version=(
                     TProtocolVersion.HIVE_CLI_SERVICE_PROTOCOL_V6)):
        log.debug('HiveServer2Cursor(service=%s, session_handle=%s, '
                  'default_config=%s, hs2_protocol_version=%s)', service,
                  session_handle, default_config, hs2_protocol_version)
        self.service = service
        self.session_handle = session_handle
        self.default_config = default_config
        self.hs2_protocol_version = hs2_protocol_version

        self._last_operation_string = None
        self._last_operation_handle = None
        self._last_operation_active = False
        self._buffersize = None
        self._buffer = []

        # initial values, per PEP 249
        self._description = None
        self._rowcount = -1

    @property
    def description(self):
        # PEP 249
        if self._description is None and self.has_result_set:
            log.debug('description=None has_result_set=True => getting schema')
            schema = get_result_schema(self.service,
                                       self._last_operation_handle)
            self._description = schema
        return self._description

    @property
    def rowcount(self):
        # PEP 249
        return self._rowcount

    @property
    def query_string(self):
        return self._last_operation_string

    def get_arraysize(self):
        # PEP 249
        return self._buffersize if self._buffersize else 1

    def set_arraysize(self, arraysize):
        # PEP 249
        log.debug('set_arraysize: arraysize=%s', arraysize)
        self._buffersize = arraysize

    arraysize = property(get_arraysize, set_arraysize)

    @property
    def buffersize(self):
        # this is for internal use.  it provides an alternate default value for
        # the size of the buffer, so that calling .next() will read multiple
        # rows into a buffer if arraysize hasn't been set.  (otherwise, we'd
        # get an unbuffered impl because the PEP 249 default value of arraysize
        # is 1)
        return self._buffersize if self._buffersize else 1024

    @property
    def has_result_set(self):
        return (self._last_operation_handle is not None and
                self._last_operation_handle.hasResultSet)

    def close(self):
        # PEP 249
        log.info('Closing HiveServer2Cursor')
        close_session(self.service, self.session_handle)

    def cancel_operation(self):
        if self._last_operation_active:
            log.info('Canceling active operation')
            cancel_operation(self.service, self._last_operation_handle)
            self._reset_state()

    def close_operation(self):
        if self._last_operation_active:
            log.info('Closing active operation')
            self._reset_state()

    def execute(self, operation, parameters=None, configuration=None):
        # PEP 249
        self.execute_async(operation, parameters=parameters,
                           configuration=configuration)
        log.info('Waiting for query to finish')
        self._wait_to_finish()  # make execute synchronous
        log.info('Query finished')

    def execute_async(self, operation, parameters=None, configuration=None):
        log.info('Executing query %s', operation)

        def op():
            if parameters:
                self._last_operation_string = _bind_parameters(operation,
                                                               parameters)
            else:
                self._last_operation_string = operation
            self._last_operation_handle = execute_statement(
                self.service, self.session_handle, self._last_operation_string,
                configuration)

        self._execute_async(op)

    def _debug_log_state(self):
        log.debug(
            '_execute_async: self._buffer=%s self._description=%s '
            'self._last_operation_active=%s self._last_operation_handle=%s',
            self._buffer, self._description, self._last_operation_active,
            self._last_operation_handle)

    def _execute_async(self, operation_fn):
        # operation_fn should set self._last_operation_string and
        # self._last_operation_handle
        self._debug_log_state()
        self._reset_state()
        self._debug_log_state()
        operation_fn()
        self._last_operation_active = True
        self._debug_log_state()

    def _reset_state(self):
        log.debug('_reset_state: Resetting cursor state')
        self._buffer = []
        self._description = None
        if self._last_operation_active:
            self._last_operation_active = False
            close_operation(self.service, self._last_operation_handle)
        self._last_operation_string = None
        self._last_operation_handle = None

    def _wait_to_finish(self):
        loop_start = time.time()
        while True:
            operation_state = get_operation_status(
                self.service, self._last_operation_handle)
            log.debug('_wait_to_finish: waited %s seconds so far',
                      time.time() - loop_start)
            if self._op_state_is_error(operation_state):
                raise OperationalError("Operation is in ERROR_STATE")
            if not self._op_state_is_executing(operation_state):
                break
            time.sleep(self._get_sleep_interval(loop_start))

    def execution_failed(self):
        if self._last_operation_handle is None:
            raise ProgrammingError("Operation state is not available")
        operation_state = get_operation_status(
            self.service, self._last_operation_handle)
        return self._op_state_is_error(operation_state)

    def _op_state_is_error(self, operation_state):
        return operation_state == 'ERROR_STATE'

    def is_executing(self):
        if self._last_operation_handle is None:
            raise ProgrammingError("Operation state is not available")
        operation_state = get_operation_status(
            self.service, self._last_operation_handle)
        return self._op_state_is_executing(operation_state)

    def _op_state_is_executing(self, operation_state):
        return operation_state in (
            'PENDING_STATE', 'INITIALIZED_STATE', 'RUNNING_STATE')

    def _get_sleep_interval(self, start_time):
        """Returns a step function of time to sleep in seconds before polling
        again. Maximum sleep is 1s, minimum is 0.1s"""
        elapsed = time.time() - start_time
        if elapsed < 0.05:
            return 0.01
        elif elapsed < 1.0:
            return 0.05
        elif elapsed < 10.0:
            return 0.1
        elif elapsed < 60.0:
            return 0.5
        return 1.0

    def executemany(self, operation, seq_of_parameters):
        # PEP 249
        log.info('Attempting to execute %s queries', len(seq_of_parameters))
        for parameters in seq_of_parameters:
            self.execute(operation, parameters)
            if self.has_result_set:
                raise ProgrammingError("Operations that have result sets are "
                                       "not allowed with executemany.")

    def fetchone(self):
        # PEP 249
        if not self.has_result_set:
            raise ProgrammingError("Tried to fetch but no results.")
        log.info('Fetching a single row')
        try:
            return next(self)
        except StopIteration:
            return None

    def fetchmany(self, size=None):
        # PEP 249
        if not self.has_result_set:
            raise ProgrammingError("Tried to fetch but no results.")
        if size is None:
            size = self.arraysize
        log.info('Fetching up to %s result rows', size)
        local_buffer = []
        i = 0
        while i < size:
            try:
                local_buffer.append(next(self))
                i += 1
            except StopIteration:
                break
        return local_buffer

    def fetchall(self):
        # PEP 249
        log.info('Fetching all result rows')
        try:
            return list(self)
        except StopIteration:
            return []

    def setinputsizes(self, sizes):
        # PEP 249
        pass

    def setoutputsize(self, size, column=None):
        # PEP 249
        pass

    def __iter__(self):
        return self

    def __next__(self):
        if not self.has_result_set:
            raise ProgrammingError(
                "Trying to fetch results on an operation with no results.")
        if len(self._buffer) > 0:
            log.debug('__next__: popping row out of buffer')
            return self._buffer.pop(0)
        elif self._last_operation_active:
            # self._buffer is empty here and op is active: try to pull more
            # rows
            log.debug('__next__: buffer empty and op is active => fetching '
                      'more rows')
            rows = fetch_results(self.service, self._last_operation_handle,
                                 self.hs2_protocol_version, self.description,
                                 self.buffersize)
            self._buffer.extend(rows)
            if len(self._buffer) == 0:
                log.debug('__next__: no more rows to fetch')
                raise StopIteration
            log.debug('__next__: popping row out of buffer')
            return self._buffer.pop(0)
        else:
            # buffer is already empty
            raise StopIteration

    def ping(self):
        """Checks connection to server by requesting some info from the
        server."""
        log.info('Pinging the impalad')
        return ping(self.service, self.session_handle)

    def get_log(self):
        return get_log(self.service, self._last_operation_handle)

    def get_profile(self):
        return get_profile(
            self.service, self._last_operation_handle, self.session_handle)

    def get_summary(self):
        return get_summary(
            self.service, self._last_operation_handle, self.session_handle)

    def build_summary_table(self, summary, output, idx=0,
                            is_fragment_root=False, indent_level=0):
        return build_summary_table(
            summary, idx, is_fragment_root, indent_level, output)

    def get_databases(self):
        def op():
            self._last_operation_string = "RPC_GET_DATABASES"
            self._last_operation_handle = get_databases(self.service,
                                                        self.session_handle)
        self._execute_async(op)
        self._wait_to_finish()

    def database_exists(self, db_name):
        return database_exists(self.service, self.session_handle,
                               self.hs2_protocol_version, db_name)

    def get_tables(self, database_name=None):
        if database_name is None:
            database_name = '.*'

        def op():
            self._last_operation_string = "RPC_GET_TABLES"
            self._last_operation_handle = get_tables(self.service,
                                                     self.session_handle,
                                                     database_name)
        self._execute_async(op)
        self._wait_to_finish()

    def table_exists(self, table_name, database_name=None):
        if database_name is None:
            database_name = '.*'
        return table_exists(self.service, self.session_handle,
                            self.hs2_protocol_version, table_name,
                            database_name)

    def get_table_schema(self, table_name, database_name=None):
        if database_name is None:
            database_name = '.*'

        def op():
            self._last_operation_string = "RPC_DESCRIBE_TABLE"
            self._last_operation_handle = get_table_schema(
                self.service, self.session_handle, table_name, database_name)

        self._execute_async(op)
        self._wait_to_finish()
        results = self.fetchall()
        if len(results) == 0:
            # TODO: the error raised here should be different
            raise OperationalError(
                "no schema results for table %s.%s" % (
                    database_name, table_name))
        # check that results are derived from a unique table
        tables = set()
        for col in results:
            tables.add((col[1], col[2]))
        if len(tables) > 1:
            # TODO: the error raised here should be different
            raise ProgrammingError(
                "db: %s, table: %s is not unique" % (
                    database_name, table_name))
        return [(r[3], r[5]) for r in results]

    def get_functions(self, database_name=None):
        if database_name is None:
            database_name = '.*'

        def op():
            self._last_operation_string = "RPC_GET_FUNCTIONS"
            self._last_operation_handle = get_functions(
                self.service, self.session_handle, database_name)

        self._execute_async(op)
        self._wait_to_finish()


# This work builds off of:
# 1. the Hue interface:
#       hue/apps/beeswax/src/beeswax/server/dbms.py
#       hue/apps/beeswax/src/beeswax/server/hive_server2_lib.py
#       hue/desktop/core/src/desktop/lib/thrift_util.py
# 2. the Impala shell:
#       Impala/shell/original_impala_shell.py


# mapping between the schema types (based on
# com.cloudera.impala.catalog.PrimitiveType) and TColumnValue (in returned
# rows) helper object for converting from TRow to something friendlier
_TTypeId_to_TColumnValue_getters = {
    'BOOLEAN': operator.attrgetter('boolVal'),
    'TINYINT': operator.attrgetter('byteVal'),
    'SMALLINT': operator.attrgetter('i16Val'),
    'INT': operator.attrgetter('i32Val'),
    'BIGINT': operator.attrgetter('i64Val'),
    'TIMESTAMP': operator.attrgetter('stringVal'),
    'FLOAT': operator.attrgetter('doubleVal'),
    'DOUBLE': operator.attrgetter('doubleVal'),
    'STRING': operator.attrgetter('stringVal'),
    'DECIMAL': operator.attrgetter('stringVal'),
    'BINARY': operator.attrgetter('binaryVal'),
    'VARCHAR': operator.attrgetter('stringVal'),
    'CHAR': operator.attrgetter('stringVal'),
}

_pre_columnar_protocols = [
    TProtocolVersion.HIVE_CLI_SERVICE_PROTOCOL_V1,
    TProtocolVersion.HIVE_CLI_SERVICE_PROTOCOL_V2,
    TProtocolVersion.HIVE_CLI_SERVICE_PROTOCOL_V3,
    TProtocolVersion.HIVE_CLI_SERVICE_PROTOCOL_V4,
    TProtocolVersion.HIVE_CLI_SERVICE_PROTOCOL_V5,
]


def err_if_rpc_not_ok(resp):
    if (resp.status.statusCode != TStatusCode.SUCCESS_STATUS and
            resp.status.statusCode != TStatusCode.SUCCESS_WITH_INFO_STATUS and
            resp.status.statusCode != TStatusCode.STILL_EXECUTING_STATUS):
        raise HiveServer2Error(resp.status.errorMessage)


# datetime only supports 6 digits of microseconds but Impala supports 9.
# If present, the trailing 3 digits will be ignored without warning.
_TIMESTAMP_PATTERN = re.compile(r'(\d+-\d+-\d+ \d+:\d+:\d+(\.\d{,6})?)')


def _parse_timestamp(value):
    input_value = value
    if value:
        match = _TIMESTAMP_PATTERN.match(value)
        if match:
            if match.group(2):
                format = '%Y-%m-%d %H:%M:%S.%f'
                # use the pattern to truncate the value
                value = match.group()
            else:
                format = '%Y-%m-%d %H:%M:%S'
            value = datetime.datetime.strptime(value, format)
        else:
            raise Exception(
                'Cannot convert "{}" into a datetime'.format(value))
    else:
        value = None
    log.debug('%s => %s', input_value, value)
    return value


# TODO: Add another decorator that runs the function in its own thread
def threaded(func):
    # pylint: disable=unused-argument
    raise NotImplementedError


def retry(func):
    # Retries RPCs after closing/reopening transport
    # `service` must be the first arg in args or must be a kwarg

    def wrapper(*args, **kwargs):
        # pylint: disable=protected-access
        # get the thrift transport
        if 'service' in kwargs:
            transport = kwargs['service']._iprot.trans
        elif len(args) > 0 and isinstance(args[0], ThriftClient):
            transport = args[0]._iprot.trans
        else:
            raise HiveServer2Error(
                "RPC function does not have expected 'service' arg")

        tries_left = 3
        while tries_left > 0:
            try:
                log.debug('Attempting to open transport (tries_left=%s)',
                          tries_left)
                if six.PY2 and not transport.isOpen():
                    transport.open()
                elif six.PY3 and not transport.is_open():
                    transport.open()
                log.debug('Transport opened')
                return func(*args, **kwargs)
            except socket.error:
                log.exception('Failed to open transport (tries_left=%s)',
                              tries_left)
            except TTransportException:
                log.exception('Failed to open transport (tries_left=%s)',
                              tries_left)
            except Exception:
                raise
            log.debug('Closing transport (tries_left=%s)', tries_left)
            transport.close()
            tries_left -= 1
        raise

    return wrapper


def connect(host, port, timeout=None, use_ssl=False, ca_cert=None,
            user=None, password=None, kerberos_service_name='impala',
            auth_mechanism=None):
    log.info('Connecting to HiveServer2 %s:%s with %s authentication '
             'mechanism', host, port, auth_mechanism)
    sock = get_socket(host, port, use_ssl, ca_cert)
    if timeout is not None:
        timeout = timeout * 1000.  # TSocket expects millis
    if six.PY2:
        sock.setTimeout(timeout)
    elif six.PY3:
        sock.set_timeout(timeout)
    transport = get_transport(sock, host, kerberos_service_name,
                              auth_mechanism, user, password)
    transport.open()
    protocol = TBinaryProtocol(transport)
    if six.PY2:
        # ThriftClient == ImpalaHiveServer2Service.Client
        service = ThriftClient(protocol)
    elif six.PY3:
        # ThriftClient == TClient
        service = ThriftClient(ImpalaHiveServer2Service, protocol)
    log.debug('sock=%s transport=%s protocol=%s service=%s', sock, transport,
              protocol, service)
    return service


def close_service(service):
    # pylint: disable=protected-access
    log.debug('close_service: service=%s', service)
    service._iprot.trans.close()


def reconnect(service):
    # pylint: disable=protected-access
    log.debug('reconnect: service=%s', service)
    service._iprot.trans.close()
    service._iprot.trans.open()


@retry
def open_session(service, user, configuration=None):
    req = TOpenSessionReq(
        client_protocol=TProtocolVersion.HIVE_CLI_SERVICE_PROTOCOL_V6,
        username=user, configuration=configuration)
    log.debug('open_session: req=%s', req)
    resp = service.OpenSession(req)
    log.debug('open_session: resp=%s', resp)
    err_if_rpc_not_ok(resp)
    return (resp.sessionHandle, resp.configuration, resp.serverProtocolVersion)


@retry
def close_session(service, session_handle):
    req = TCloseSessionReq(sessionHandle=session_handle)
    log.debug('close_session: req=%s', req)
    resp = service.CloseSession(req)
    log.debug('close_session: resp=%s', resp)
    err_if_rpc_not_ok(resp)


@retry
def execute_statement(service, session_handle, statement, configuration=None,
                      async=False):
    req = TExecuteStatementReq(sessionHandle=session_handle,
                               statement=statement, confOverlay=configuration,
                               runAsync=async)
    log.debug('execute_statement: req=%s', req)
    resp = service.ExecuteStatement(req)
    log.debug('execute_statement: resp=%s', resp)
    err_if_rpc_not_ok(resp)
    return resp.operationHandle


@retry
def get_result_schema(service, operation_handle):
    if not operation_handle.hasResultSet:
        log.debug('get_result_schema: operation_handle.hasResultSet=False')
        return None
    req = TGetResultSetMetadataReq(operationHandle=operation_handle)
    log.debug('get_result_schema: req=%s', req)
    resp = service.GetResultSetMetadata(req)
    log.debug('get_result_schema: resp=%s', resp)
    err_if_rpc_not_ok(resp)

    schema = []
    for column in resp.schema.columns:
        # pylint: disable=protected-access
        name = column.columnName
        entry = column.typeDesc.types[0].primitiveEntry
        type_ = TTypeId._VALUES_TO_NAMES[entry.type].split('_')[0]
        if type_ == 'DECIMAL':
            qualifiers = entry.typeQualifiers.qualifiers
            precision = qualifiers['precision'].i32Value
            scale = qualifiers['scale'].i32Value
            schema.append((name, type_, None, None,
                           precision, scale, None))
        else:
            schema.append((name, type_, None, None, None, None, None))

    log.debug('get_result_schema: schema=%s', schema)

    return schema


@retry
def fetch_results(service, operation_handle, hs2_protocol_version, schema=None,
                  max_rows=1024, orientation=TFetchOrientation.FETCH_NEXT):
    # pylint: disable=too-many-locals,too-many-branches,protected-access
    if not operation_handle.hasResultSet:
        log.debug('fetch_results: operation_handle.hasResultSet=False')
        return None

    # the schema is necessary to pull the proper values (i.e., coalesce)
    if schema is None:
        schema = get_result_schema(service, operation_handle)

    req = TFetchResultsReq(operationHandle=operation_handle,
                           orientation=orientation,
                           maxRows=max_rows)
    log.debug('fetch_results: hs2_protocol_version=%s max_rows=%s '
              'orientation=%s req=%s', hs2_protocol_version, max_rows,
              orientation, req)
    resp = service.FetchResults(req)
    err_if_rpc_not_ok(resp)

    if hs2_protocol_version == TProtocolVersion.HIVE_CLI_SERVICE_PROTOCOL_V6:
        tcols = [_TTypeId_to_TColumnValue_getters[schema[i][1]](col)
                 for (i, col) in enumerate(resp.results.columns)]
        num_cols = len(tcols)
        num_rows = len(tcols[0].values)
        log.debug('fetch_results: COLUMNAR num_cols=%s num_rows=%s tcols=%s',
                  num_cols, num_rows, tcols)

        column_data = []
        for j in range(num_cols):
            type_ = schema[j][1]
            nulls = tcols[j].nulls
            values = tcols[j].values

            # thriftpy sometimes returns unicode instead of bytes
            if six.PY3 and isinstance(nulls, str):
                nulls = nulls.encode('utf-8')

            is_null = bitarray(endian='little')
            is_null.frombytes(nulls)

            # Ref HUE-2722, HiveServer2 sometimes does not add trailing '\x00'
            if len(values) > len(nulls):
                to_append = ((len(values) - len(nulls) + 7) // 8)
                is_null.frombytes(b'\x00' * to_append)

            if type_ == 'TIMESTAMP':
                for i in range(num_rows):
                    values[i] = (None if is_null[i] else
                                 _parse_timestamp(values[i]))
            elif type_ == 'DECIMAL':
                for i in range(num_rows):
                    values[i] = (None if is_null[i] else Decimal(values[i]))
            else:
                for i in range(num_rows):
                    if is_null[i]:
                        values[i] = None
            column_data.append(values)

        # TODO: enable columnar fetch
        rows = lzip(*column_data)
    elif hs2_protocol_version in _pre_columnar_protocols:
        log.debug('fetch_results: ROWS num-rows=%s', len(resp.results.rows))
        rows = []
        for trow in resp.results.rows:
            row = []
            for (i, col_val) in enumerate(trow.colVals):
                type_ = schema[i][1]
                value = _TTypeId_to_TColumnValue_getters[type_](col_val).value
                if type_ == 'TIMESTAMP':
                    value = _parse_timestamp(value)
                elif type_ == 'DECIMAL':
                    if value:
                        value = Decimal(value)
                row.append(value)
            rows.append(tuple(row))
    else:
        raise HiveServer2Error(
            "Got HiveServer2 version {0}; expected V1 - V6".format(
                TProtocolVersion._VALUES_TO_NAMES[hs2_protocol_version]))
    return rows


@retry  # pylint: disable=unused-argument
def get_current_database(service, session_handle):
    # pylint: disable=unused-argument
    raise NotImplementedError


@retry
def get_databases(service, session_handle):
    req = TGetSchemasReq(sessionHandle=session_handle, schemaName='.*')
    log.debug('get_databases: req=%s', req)
    resp = service.GetSchemas(req)
    log.debug('get_databases: resp=%s', resp)
    err_if_rpc_not_ok(resp)
    return resp.operationHandle


@retry
def database_exists(service, session_handle, hs2_protocol_version, db_name):
    req = TGetSchemasReq(sessionHandle=session_handle, schemaName=db_name)
    log.debug('database_exists: req=%s', req)
    resp = service.GetSchemas(req)
    log.debug('database_exists: resp=%s', resp)
    err_if_rpc_not_ok(resp)
    operation_handle = resp.operationHandle
    # this only fetches default max_rows, but there should only be one row
    # ideally
    results = fetch_results(service=service, operation_handle=operation_handle,
                            hs2_protocol_version=hs2_protocol_version)
    exists = False
    for result in results:
        if result[0].lower() == db_name.lower():
            exists = True
    close_operation(service, operation_handle)
    return exists


@retry
def get_tables(service, session_handle, database_name='.*'):
    req = TGetTablesReq(sessionHandle=session_handle, schemaName=database_name,
                        tableName='.*')
    log.debug('get_tables: req=%s', req)
    resp = service.GetTables(req)
    log.debug('get_tables: resp=%s', resp)
    err_if_rpc_not_ok(resp)
    return resp.operationHandle


@retry
def table_exists(service, session_handle, hs2_protocol_version, table_name,
                 database_name='.*'):
    req = TGetTablesReq(sessionHandle=session_handle, schemaName=database_name,
                        tableName=table_name)
    log.debug('table_exists: req=%s', req)
    resp = service.GetTables(req)
    log.debug('table_exists: resp=%s', resp)
    err_if_rpc_not_ok(resp)
    operation_handle = resp.operationHandle
    # this only fetches default max_rows, but there should only be one row
    # ideally
    results = fetch_results(service=service, operation_handle=operation_handle,
                            hs2_protocol_version=hs2_protocol_version)
    exists = False
    for result in results:
        if result[2].lower() == table_name.lower():
            exists = True
    close_operation(service, operation_handle)
    return exists


@retry
def get_table_schema(service, session_handle, table_name, database_name='.*'):
    req = TGetColumnsReq(sessionHandle=session_handle,
                         schemaName=database_name, tableName=table_name,
                         columnName='.*')
    log.debug('get_table_schema: req=%s', req)
    resp = service.GetColumns(req)
    log.debug('get_table_schema: resp=%s', resp)
    err_if_rpc_not_ok(resp)
    return resp.operationHandle


@retry
def get_functions(service, session_handle, database_name='.*'):
    # TODO: need to test this one especially
    req = TGetFunctionsReq(sessionHandle=session_handle,
                           schemaName=database_name,
                           functionName='.*')
    log.debug('get_functions: req=%s', req)
    resp = service.GetFunctions(req)
    log.debug('get_functions: resp=%s', resp)
    err_if_rpc_not_ok(resp)
    return resp.operationHandle


@retry
def get_operation_status(service, operation_handle):
    # pylint: disable=protected-access
    req = TGetOperationStatusReq(operationHandle=operation_handle)
    log.debug('get_operation_status: req=%s', req)
    resp = service.GetOperationStatus(req)
    log.debug('get_operation_status: resp=%s', resp)
    err_if_rpc_not_ok(resp)
    return TOperationState._VALUES_TO_NAMES[resp.operationState]


@retry
def cancel_operation(service, operation_handle):
    req = TCancelOperationReq(operationHandle=operation_handle)
    log.debug('cancel_operation: req=%s', req)
    resp = service.CancelOperation(req)
    log.debug('cancel_operation: resp=%s', resp)
    err_if_rpc_not_ok(resp)


@retry
def close_operation(service, operation_handle):
    req = TCloseOperationReq(operationHandle=operation_handle)
    log.debug('close_operation: req=%s', req)
    resp = service.CloseOperation(req)
    log.debug('close_operation: resp=%s', resp)
    err_if_rpc_not_ok(resp)


@retry
def get_log(service, operation_handle):
    req = TGetLogReq(operationHandle=operation_handle)
    log.debug('get_log: req=%s', req)
    resp = service.GetLog(req)
    log.debug('get_log: resp=%s', resp)
    err_if_rpc_not_ok(resp)
    return resp.log


def ping(service, session_handle):
    req = TGetInfoReq(sessionHandle=session_handle,
                      infoType=TGetInfoType.CLI_SERVER_NAME)
    log.debug('ping: req=%s', req)
    try:
        resp = service.GetInfo(req)
    except TTransportException:
        log.exception('ping: failed')
        return False
    log.debug('ping: resp=%s', resp)
    try:
        err_if_rpc_not_ok(resp)
    except HiveServer2Error:
        log.exception('ping: failed')
        return False
    return True


def get_profile(service, operation_handle, session_handle):
    req = TGetRuntimeProfileReq(operationHandle=operation_handle,
                                sessionHandle=session_handle)
    log.debug('get_profile: req=%s', req)
    resp = service.GetRuntimeProfile(req)
    log.debug('get_profile: resp=%s', resp)
    err_if_rpc_not_ok(resp)
    return resp.profile


def get_summary(service, operation_handle, session_handle):
    req = TGetExecSummaryReq(operationHandle=operation_handle,
                             sessionHandle=session_handle)
    log.debug('get_summary: req=%s', req)
    resp = service.GetExecSummary(req)
    log.debug('get_summary: resp=%s', resp)
    err_if_rpc_not_ok(resp)
    return resp.summary


def build_summary_table(summary, idx, is_fragment_root, indent_level, output):
    """Direct translation of Coordinator::PrintExecSummary() to recursively
    build a list of rows of summary statistics, one per exec node

    summary: the TExecSummary object that contains all the summary data

    idx: the index of the node to print

    is_fragment_root: true if the node to print is the root of a fragment (and
    therefore feeds into an exchange)

    indent_level: the number of spaces to print before writing the node's
    label, to give the appearance of a tree. The 0th child of a node has the
    same indent_level as its parent. All other children have an indent_level
    of one greater than their parent.

    output: the list of rows into which to append the rows produced for this
    node and its children.

    Returns the index of the next exec node in summary.exec_nodes that should
    be processed, used internally to this method only.
    """
    # pylint: disable=too-many-locals

    attrs = ["latency_ns", "cpu_time_ns", "cardinality", "memory_used"]

    # Initialise aggregate and maximum stats
    agg_stats, max_stats = TExecStats(), TExecStats()
    for attr in attrs:
        setattr(agg_stats, attr, 0)
        setattr(max_stats, attr, 0)

    node = summary.nodes[idx]
    for stats in node.exec_stats:
        for attr in attrs:
            val = getattr(stats, attr)
            if val is not None:
                setattr(agg_stats, attr, getattr(agg_stats, attr) + val)
                setattr(max_stats, attr, max(getattr(max_stats, attr), val))

    if len(node.exec_stats) > 0:
        avg_time = agg_stats.latency_ns / len(node.exec_stats)
    else:
        avg_time = 0

    # If the node is a broadcast-receiving exchange node, the cardinality of
    # rows produced is the max over all instances (which should all have
    # received the same number of rows). Otherwise, the cardinality is the sum
    # over all instances which process disjoint partitions.
    if node.is_broadcast and is_fragment_root:
        cardinality = max_stats.cardinality
    else:
        cardinality = agg_stats.cardinality

    est_stats = node.estimated_stats
    label_prefix = ""
    if indent_level > 0:
        label_prefix = "|"
        if is_fragment_root:
            label_prefix += "    " * indent_level
        else:
            label_prefix += "--" * indent_level

    def prettyprint(val, units, divisor):
        for unit in units:
            if val < divisor:
                if unit == units[0]:
                    return "%d%s" % (val, unit)
                else:
                    return "%3.2f%s" % (val, unit)
            val /= divisor

    def prettyprint_bytes(byte_val):
        return prettyprint(
            byte_val, [' B', ' KB', ' MB', ' GB', ' TB'], 1024.0)

    def prettyprint_units(unit_val):
        return prettyprint(unit_val, ["", "K", "M", "B"], 1000.0)

    def prettyprint_time(time_val):
        return prettyprint(time_val, ["ns", "us", "ms", "s"], 1000.0)

    row = [label_prefix + node.label,
           len(node.exec_stats),
           prettyprint_time(avg_time),
           prettyprint_time(max_stats.latency_ns),
           prettyprint_units(cardinality),
           prettyprint_units(est_stats.cardinality),
           prettyprint_bytes(max_stats.memory_used),
           prettyprint_bytes(est_stats.memory_used),
           node.label_detail]

    output.append(row)
    try:
        sender_idx = summary.exch_to_sender_map[idx]
        # This is an exchange node, so the sender is a fragment root, and
        # should be printed next.
        build_summary_table(summary, sender_idx, True, indent_level, output)
    except (KeyError, TypeError):
        # Fall through if idx not in map, or if exch_to_sender_map itself is
        # not set
        pass

    idx += 1
    if node.num_children > 0:
        first_child_output = []
        idx = build_summary_table(summary, idx, False, indent_level,
                                  first_child_output)
        # pylint: disable=unused-variable
        # TODO: is child_idx supposed to be unused?  See #120
        for child_idx in range(1, node.num_children):
            # All other children are indented (we only have 0, 1 or 2 children
            # for every exec node at the moment)
            idx = build_summary_table(summary, idx, False, indent_level + 1,
                                      output)
        output += first_child_output
    return idx
