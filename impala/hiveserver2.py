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
import sys
from six.moves import range
from bitarray import bitarray

from impala.compat import Decimal
from impala.util import get_logger_and_init_null
from impala.interface import Connection, Cursor, _bind_parameters
from impala.error import (NotSupportedError, OperationalError,
                          ProgrammingError, HiveServer2Error)
from impala._thrift_api import (
    get_socket, get_http_transport, get_transport, THttpClient,
    TTransportException, TBinaryProtocol, TOpenSessionReq, TFetchResultsReq,
    TCloseSessionReq, TExecuteStatementReq, TGetInfoReq, TGetInfoType, TTypeId,
    TFetchOrientation, TGetResultSetMetadataReq, TStatusCode, TGetColumnsReq,
    TGetSchemasReq, TGetTablesReq, TGetFunctionsReq, TGetOperationStatusReq,
    TOperationState, TCancelOperationReq, TCloseOperationReq, TGetLogReq,
    TProtocolVersion, TGetRuntimeProfileReq, TRuntimeProfileFormat,
    TGetExecSummaryReq, ImpalaHiveServer2Service, TExecStats, ThriftClient,
    TApplicationException)


log = get_logger_and_init_null(__name__)

V6_VERSION = TProtocolVersion.HIVE_CLI_SERVICE_PROTOCOL_V6


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
        log.debug('Closing HS2 connection')
        self.service.close()

    def reconnect(self):
        self.service.reconnect()

    def commit(self):
        """Impala doesn't support transactions; does nothing."""
        # PEP 249
        pass

    def rollback(self):
        """Impala doesn't support transactions; raises NotSupportedError"""
        # PEP 249
        raise NotSupportedError

    def cursor(self, user=None, configuration=None, convert_types=True,
               dictify=False, fetch_error=True):
        """Get a cursor from the HiveServer2 (HS2) connection.

        Parameters
        ----------
        user : str, optional
        configuration : dict of str keys and values, optional
            Configuration overlay for the HS2 session.
        convert_types : bool, optional
            When `False`, timestamps and decimal values will not be converted
            to Python `datetime` and `Decimal` values. (These conversions are
            expensive.) Only applies when using HS2 protocol versions > 6.
        dictify : bool, optional
            When `True` cursor will return key value pairs instead of rows.
        fetch_error : bool, optional
            In versions of impala prior to 2.7.0, when an operation fails and
            the impalad returns an error state, the error message is not always
            returned. In these cases the error message can be retrieved by a
            subsequent fetch rpc call but this has a side effect of invalidating
            the query handle and causing any further operations against it to
            fail. e.g. calling log() or profile().

            When set to `True` impyla will attempt to fetch the error message.
            When set to `False`, this flag will cause impyla not to attempt to
            fetch the message with a fetch call . In this case the query
            handle remains valid and impyla will raise an exception with a
            message of "Operation is in ERROR_STATE".
            The Default option is `True`.

        Returns
        -------
        HiveServer2Cursor
            A `Cursor` object (DB API 2.0-compliant).
        """
        # PEP 249
        log.debug('Getting a cursor (Impala session)')

        if user is None:
            user = getpass.getuser()

        log.debug('.cursor(): getting new session_handle')

        session = self.service.open_session(user, configuration)

        log.debug('HiveServer2Cursor(service=%s, session_handle=%s, '
                  'default_config=%s, hs2_protocol_version=%s)',
                  self.service, session.handle,
                  session.config, session.hs2_protocol_version)

        cursor_class = HiveServer2DictCursor if dictify else HiveServer2Cursor

        cursor = cursor_class(session, convert_types=convert_types,
                              fetch_error=fetch_error)

        if self.default_db is not None:
            log.info('Using database %s as default', self.default_db)
            cursor.execute('USE %s' % self.default_db)
        return cursor


class HiveServer2Cursor(Cursor):
    """The DB API 2.0 Cursor object.

    See the PEP 249 specification for more details.
    """
    # PEP 249
    # HiveServer2Cursor objects are associated with a Session
    # they are instantiated with alive session_handles

    def __init__(self, session, convert_types=True, fetch_error=True):
        self.session = session
        self.convert_types = convert_types
        self.fetch_error = fetch_error

        self._last_operation = None

        self._last_operation_string = None
        self._last_operation_active = False
        self._buffersize = None
        self._buffer = Batch()  # zero-length

        # initial values, per PEP 249
        self._description = None
        self._rowcount = -1

        self._closed = False

    def __del__(self):
        if self._closed:
            return
        try:
           self.close_operation()
        except Exception:
            pass
        try:
           self.session.close()
        except Exception:
            pass

    @property
    def description(self):
        # PEP 249
        if self._description is None and self.has_result_set:
            log.debug('description=None has_result_set=True => getting schema')

            schema = self._last_operation.get_result_schema()
            self._description = schema
        return self._description

    @property
    def rowcount(self):
        # PEP 249
        return self._rowcount

    @property
    def rowcounts(self):
        # Work around to get the number of rows modified for Inserts/Update/Delte statements
        modifiedRows, errorRows = -1, -1
        if self._last_operation_active:
            logList = self.get_profile().split('\n')
            resultDict = {}
            subs = ['NumModifiedRows', 'NumRowErrors']
            resultSet = [s for s in logList if any(item in s for item in subs)]
            if resultSet:
                for items in resultSet:
                    key, value = items.split(':')
                    key, value = key.strip(), value.strip()
                    resultDict[key] = value

                modifiedRows = int(resultDict.get('NumModifiedRows', -1))
                errorRows = int(resultDict.get('NumRowErrors', -1))

        return (modifiedRows, errorRows)      
      
    @property
    def lastrowid(self):
        # PEP 249
        return None

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
        return (self._last_operation is not None and
                self._last_operation.has_result_set)

    def close(self):
        # PEP 249
        if self._closed:
            return
        # If an operation is active and isn't closed before the session is
        # closed, then the server will cancel the operation upon closing
        # the session. Cancellation could be problematic for some DDL
        # operations. This avoids requiring the user to call the non-PEP 249
        # close_operation().
        exc_info = None
        try:
            self.close_operation()
        except Exception:
            exc_info = sys.exc_info()

        log.debug('Closing HiveServer2Cursor')
        try:
            self.session.close()
        except Exception:
            # If we encountered an error when closing the session
            # then print operation close exception to logs and
            # raise the session close exception
            if exc_info:
                log.error('Failure encountered closing last operation.',
                                                        exc_info=exc_info)
            raise

        self._closed = True
        # If there was an error when closing last operation then
        # raise exception
        if exc_info:
            six.reraise(*exc_info)

    def cancel_operation(self, reset_state=True):
        if self._last_operation_active:
            log.info('Canceling active operation')
            self._last_operation.cancel()
            if reset_state:
                self._reset_state()

    def close_operation(self):
        if self._last_operation_active:
            log.info('Closing active operation')
            self._reset_state()

    def _reset_state(self):
        log.debug('_reset_state: Resetting cursor state')
        self._buffer = Batch()
        self._description = None
        if self._last_operation_active:
            self._last_operation_active = False

            self._last_operation.close()
        self._last_operation_string = None
        self._last_operation = None

    def execute(self, operation, parameters=None, configuration=None):
        """Synchronously execute a SQL query.

        Blocks until results are available.

        Parameters
        ----------
        operation : str
            The SQL query to execute.
        parameters : str, optional
            Parameters to be bound to variables in the SQL query, if any.
            Impyla supports all DB API `paramstyle`s, including `qmark`,
            `numeric`, `named`, `format`, `pyformat`.
        configuration : dict of str keys and values, optional
            Configuration overlay for this query.

        Returns
        -------
        NoneType
            Results are available through a call to `fetch*`.
        """
        # PEP 249
        self.execute_async(operation, parameters=parameters,
                           configuration=configuration)
        log.debug('Waiting for query to finish')
        self._wait_to_finish()  # make execute synchronous
        log.debug('Query finished')

    def execute_async(self, operation, parameters=None, configuration=None):
        """Asynchronously execute a SQL query.

        Immediately returns after query is sent to the HS2 server.  Poll with
        `is_executing`. A call to `fetch*` will block.

        Parameters
        ----------
        operation : str
            The SQL query to execute.
        parameters : str, optional
            Parameters to be bound to variables in the SQL query, if any.
            Impyla supports all DB API `paramstyle`s, including `qmark`,
            `numeric`, `named`, `format`, `pyformat`.
        configuration : dict of str keys and values, optional
            Configuration overlay for this query.

        Returns
        -------
        NoneType
            Results are available through a call to `fetch*`.
        """
        log.debug('Executing query %s', operation)

        paramstyle = None
        if configuration:
            paramstyle = configuration.pop('paramstyle', None)

        def op():
            if parameters:
                self._last_operation_string = _bind_parameters(operation,
                                                               parameters,
                                                               paramstyle)
            else:
                self._last_operation_string = operation

            op = self.session.execute(self._last_operation_string,
                                      configuration,
                                      run_async=True)
            self._last_operation = op

        self._execute_async(op)

    def _debug_log_state(self):
        if self._last_operation_active:
            handle = self._last_operation.handle
        else:
            handle = None
        log.debug('_execute_async: self._buffer=%s self._description=%s '
                  'self._last_operation_active=%s '
                  'self._last_operation=%s',
                  self._buffer, self._description,
                  self._last_operation_active, handle)

    def _execute_async(self, operation_fn):
        # operation_fn should set self._last_operation_string and
        # self._last_operation
        self._debug_log_state()
        self._reset_state()
        self._debug_log_state()
        operation_fn()
        self._last_operation_active = True
        self._debug_log_state()

    def _wait_to_finish(self):
        # Prior to IMPALA-1633 GetOperationStatus does not populate errorMessage
        # in case of failure. If not populated, queries that return results
        # can get a failure description with a further call to FetchResults rpc.
        loop_start = time.time()
        while True:
            req = TGetOperationStatusReq(operationHandle=self._last_operation.handle)
            resp = self._last_operation._rpc('GetOperationStatus', req)
            operation_state = TOperationState._VALUES_TO_NAMES[resp.operationState]

            log.debug('_wait_to_finish: waited %s seconds so far',
                      time.time() - loop_start)
            if self._op_state_is_error(operation_state):
                if resp.errorMessage:
                    raise OperationalError(resp.errorMessage)
                else:
                    if self.fetch_error and self.has_result_set:
                        self._last_operation_active=False
                        self._last_operation.fetch()
                    else:
                        raise OperationalError("Operation is in ERROR_STATE")
            if not self._op_state_is_executing(operation_state):
                break
            time.sleep(self._get_sleep_interval(loop_start))

    def status(self):
        if self._last_operation is None:
            raise ProgrammingError("Operation state is not available")
        return self._last_operation.get_status()

    def execution_failed(self):
        if self._last_operation is None:
            raise ProgrammingError("Operation state is not available")
        operation_state = self._last_operation.get_status()
        return self._op_state_is_error(operation_state)

    def _op_state_is_error(self, operation_state):
        return operation_state == 'ERROR_STATE'

    def is_executing(self):
        if self._last_operation is None:
            raise ProgrammingError("Operation state is not available")
        operation_state = self._last_operation.get_status()
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

    def executemany(self, operation, seq_of_parameters, configuration=None):
        # PEP 249
        log.debug('Attempting to execute %s queries', len(seq_of_parameters))
        for parameters in seq_of_parameters:
            self.execute(operation, parameters, configuration)
            if self.has_result_set:
                raise ProgrammingError("Operations that have result sets are "
                                       "not allowed with executemany.")

    def fetchone(self):
        # PEP 249
        self._wait_to_finish()
        if not self.has_result_set:
            raise ProgrammingError("Tried to fetch but no results.")
        log.debug('Fetching a single row')
        try:
            return next(self)
        except StopIteration:
            return None


    def fetchcbatch(self):
        '''Return a CBatch object containing the next rows to be fetched. If data is
           currently buffered, returns that data, otherwise fetches the next batch.
           Returns None if no more rows are currently available. Note that if None
           is returned, more rows may still be available in future.'''
        if not self._last_operation.is_columnar:
            raise NotSupportedError("Server does not support columnar "
                                    "fetching")
        if not self.has_result_set:
            raise ProgrammingError(
                "Trying to fetch results on an operation with no results.")
        if len(self._buffer) > 0:
            log.debug('fetchcbatch: buffer has data in. Returning it and wiping buffer')
            batch = self._buffer
            self._buffer = Batch()
            return batch
        elif self._last_operation_active:
            log.debug('fetchcbatch: buffer empty and op is active => fetching '
                      'more data')
            batch = (self._last_operation.fetch(
                         self.description,
                         self.buffersize,
                         convert_types=self.convert_types))
            if len(batch) == 0:
               return None
            return batch
        else:
           return None


    def fetchmany(self, size=None):
        # PEP 249
        self._wait_to_finish()
        if not self.has_result_set:
            raise ProgrammingError("Tried to fetch but no results.")
        if size is None:
            size = self.arraysize
        log.debug('Fetching up to %s result rows', size)
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
        self._wait_to_finish()
        log.debug('Fetching all result rows')
        try:
            return list(self)
        except StopIteration:
            return []

    def fetchcolumnar(self):
        """Executes a fetchall operation returning a list of CBatches"""
        self._wait_to_finish()
        if not self._last_operation.is_columnar:
            raise NotSupportedError("Server does not support columnar "
                                    "fetching")
        batches = []
        while True:
            batch = (self._last_operation.fetch(
                         self.description,
                         self.buffersize,
                         convert_types=self.convert_types))
            if len(batch) == 0:
                break
            batches.append(batch)
        return batches

    def setinputsizes(self, sizes):
        # PEP 249
        pass

    def setoutputsize(self, size, column=None):
        # PEP 249
        pass

    def __iter__(self):
        return self

    def next(self):
        return self.__next__()

    def __next__(self):
        while True:
            if not self.has_result_set:
                raise ProgrammingError(
                    "Trying to fetch results on an operation with no results.")
            if len(self._buffer) > 0:
                log.debug('__next__: popping row out of buffer')
                return self._buffer.pop()
            elif self._last_operation_active:
                log.debug('__next__: buffer empty and op is active => fetching '
                          'more data')
                self._buffer = self._last_operation.fetch(self.description,
                                                          self.buffersize,
                                                          convert_types=self.convert_types)
                if len(self._buffer) > 0:
                  log.debug('__next__: popping row out of buffer')
                  return self._buffer.pop()
                if not self._buffer.expect_more_rows:
                    log.debug('__next__: no more data to fetch')
                    raise StopIteration
                # If we didn't get rows, but more are expected, need to iterate again.
            else:
                log.debug('__next__: buffer empty')
                raise StopIteration

    def ping(self):
        """Checks connection to server by requesting some info."""
        log.info('Pinging the impalad')
        return self.session.ping()

    def get_log(self):
        if self._last_operation is None:
            raise ProgrammingError("Operation state is not available")
        return self._last_operation.get_log()

    def get_profile(self, profile_format=TRuntimeProfileFormat.STRING):
        if self._last_operation is None:
            raise ProgrammingError("Operation state is not available")
        return self._last_operation.get_profile(profile_format=profile_format)

    def get_summary(self):
        return self._last_operation.get_summary()

    def build_summary_table(self, summary, output, idx=0,
                            is_fragment_root=False, indent_level=0):
        return build_summary_table(summary, idx, is_fragment_root,
                                   indent_level, output)

    def get_databases(self):
        def op():
            self._last_operation_string = "RPC_GET_DATABASES"
            self._last_operation = self.session.get_databases()
        self._execute_async(op)
        self._wait_to_finish()

    def database_exists(self, db_name):
        return self.session.database_exists(db_name)

    def get_tables(self, database_name=None):
        if database_name is None:
            database_name = '.*'

        def op():
            self._last_operation_string = "RPC_GET_TABLES"
            self._last_operation = self.session.get_tables(database_name)

        self._execute_async(op)
        self._wait_to_finish()

    def table_exists(self, table_name, database_name=None):
        if database_name is None:
            database_name = '.*'
        return self.session.table_exists(table_name,
                                         database=database_name)

    def get_table_schema(self, table_name, database_name=None):
        if database_name is None:
            database_name = '.*'

        def op():
            self._last_operation_string = "RPC_DESCRIBE_TABLE"
            self._last_operation = self.session.get_table_schema(
                table_name, database_name)

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
            self._last_operation = self.session.get_functions(database_name)

        self._execute_async(op)
        self._wait_to_finish()


class HiveServer2DictCursor(HiveServer2Cursor):

    """The cursor that returns each element as a dictionary"""
    def execute(self, operation, parameters=None, configuration=None):
        super(self.__class__, self).execute(operation, parameters,
                                            configuration)
        if self.description is not None:
            self.fields = [d[0] for d in self.description]
        else:
            self.fields = None

    def __next__(self):
        record = super(self.__class__, self).__next__()
        return dict(zip(self.fields, record))


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
    'MAP': operator.attrgetter('stringVal'),
    'ARRAY': operator.attrgetter('stringVal'),
    'STRUCT': operator.attrgetter('stringVal'),
    'UNIONTYPE': operator.attrgetter('stringVal'),
    'NULL': operator.attrgetter('stringVal'),
    'DATE': operator.attrgetter('stringVal')
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


def connect(host, port, timeout=None, use_ssl=False, ca_cert=None,
            user=None, password=None, kerberos_service_name='impala',
            auth_mechanism=None, krb_host=None, use_http_transport=False,
            http_path=''):
    log.debug('Connecting to HiveServer2 %s:%s with %s authentication '
              'mechanism', host, port, auth_mechanism)

    if use_http_transport:
        # TODO(#362): Add server authentication with thrift 0.12.
        if ca_cert:
            raise NotSupportedError("Server authentication is not supported " +
                                    "with HTTP endpoints")
        if krb_host:
            raise NotSupportedError("Kerberos authentication is not " +
                                    "supported with HTTP endpoints")
        transport = get_http_transport(host, port, http_path=http_path,
                                       use_ssl=use_ssl, ca_cert=ca_cert,
                                       user=user, password=password,
                                       auth_mechanism=auth_mechanism)
    else:
        sock = get_socket(host, port, use_ssl, ca_cert)

        if krb_host:
            kerberos_host = krb_host
        else:
            kerberos_host = host

        if timeout is not None:
            timeout = timeout * 1000.  # TSocket expects millis
        if six.PY2:
            sock.setTimeout(timeout)
        elif six.PY3:
            try:
                # thriftpy has a release where set_timeout is missing
                sock.set_timeout(timeout)
            except AttributeError:
                sock.socket_timeout = timeout
                sock.connect_timeout = timeout
        log.debug('sock=%s', sock)
        transport = get_transport(sock, kerberos_host, kerberos_service_name,
                                auth_mechanism, user, password)

    transport.open()
    protocol = TBinaryProtocol(transport)
    if six.PY2:
        # ThriftClient == ImpalaHiveServer2Service.Client
        service = ThriftClient(protocol)
    elif six.PY3:
        # ThriftClient == TClient
        service = ThriftClient(ImpalaHiveServer2Service, protocol)
    log.debug('transport=%s protocol=%s service=%s', transport, protocol,
              service)

    return HS2Service(service)


def _is_columnar_protocol(hs2_protocol_version):
    return (hs2_protocol_version ==
            TProtocolVersion.HIVE_CLI_SERVICE_PROTOCOL_V6)


def _is_precolumnar_protocol(hs2_protocol_version):
    return hs2_protocol_version in _pre_columnar_protocols


class Batch(object):
    def __init__(self):
        pass

    def __len__(self):
        return 0

    def pop(self):
        raise NotImplementedError("Cannot pop a Batch object")

    def __iter__(self):
        return self

    def next(self):
        return self.__next__()

    def __next__(self):
        if len(self) > 0:
            return self.pop()
        raise StopIteration

    def __str__(self):
        return 'Batch()'


class Column(object):
    def __init__(self, data_type, values, nulls):
        self.data_type = data_type
        self.values = values
        self.nulls = nulls
        self.rows_left = len(self.values)
        self.num_rows = self.rows_left

    def __len__(self):
        return self.rows_left

    def __str__(self):
        return 'Column(type={0}, values={1}, nulls={2})'.format(
            self.data_type, self.values, self.nulls)

    def pop(self):
        if self.rows_left < 1:
            raise StopIteration
        pos = self.num_rows-self.rows_left
        self.rows_left -= 1
        if self.nulls[pos]:
           return None
        value = self.values[pos]
        return value


class CBatch(Batch):

    def __init__(self, trowset, expect_more_rows, schema, convert_types=True):
        self.expect_more_rows = expect_more_rows
        self.schema = schema
        tcols = [_TTypeId_to_TColumnValue_getters[schema[i][1]](col)
                 for (i, col) in enumerate(trowset.columns)]
        num_cols = len(tcols)
        num_rows = len(tcols[0].values)

        log.debug('CBatch: input TRowSet num_cols=%s num_rows=%s tcols=%s',
                  num_cols, num_rows, tcols)

        self.columns = []
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

            if convert_types:
                values = self._convert_values(type_, is_null, values)

            self.columns.append(Column(type_, values, is_null))

    def _convert_values(self, type_, is_null, values):
        # pylint: disable=consider-using-enumerate
        if type_ == 'TIMESTAMP':
            for i in range(len(values)):
                values[i] = (None if is_null[i] else
                             _parse_timestamp(values[i]))
        if type_ == 'DECIMAL':
            for i in range(len(values)):
                values[i] = (None if is_null[i] else Decimal(values[i]))

        return values

    def __len__(self):
        return len(self.columns[0]) if len(self.columns) > 0 else 0

    def pop(self):
        return tuple([c.pop() for c in self.columns])

    def __str__(self):
        col_string = ','.join([str(col) for col in self.columns])
        return 'CBatch({0})'.format(col_string)


class RBatch(Batch):
    def __init__(self, trowset, expect_more_rows, schema):
        log.debug('RBatch: input TRowSet: %s', trowset)
        self.expect_more_rows = expect_more_rows
        self.schema = schema
        self.rows = []
        for trow in trowset.rows:
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
            self.rows.append(tuple(row))

    def __len__(self):
        return len(self.rows)

    def pop(self):
        return self.rows.pop(0)


class ThriftRPC(object):

    def __init__(self, client, retries=3):
        self.client = client
        self.retries = retries

    def _rpc(self, func_name, request):
        self._log_request(func_name, request)
        response = self._execute(func_name, request)
        self._log_response(func_name, response)
        err_if_rpc_not_ok(response)
        return response

    def _execute(self, func_name, request):
        # pylint: disable=protected-access
        # get the thrift transport
        transport = self.client._iprot.trans
        tries_left = self.retries
        while tries_left > 0:
            try:
                log.debug('Attempting to open transport (tries_left=%s)',
                          tries_left)
                open_transport(transport)
                log.debug('Transport opened')
                func = getattr(self.client, func_name)
                return func(request)
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

        raise HiveServer2Error('Failed after retrying {0} times'
                               .format(self.retries))

    def _operation(self, kind, request):
        resp = self._rpc(kind, request)
        return self._get_operation(resp.operationHandle)

    def _log_request(self, kind, request):
        log.debug('%s: req=%s', kind, request)

    def _log_response(self, kind, response):
        log.debug('%s: resp=%s', kind, response)


def open_transport(transport):
    if six.PY2 and not transport.isOpen():
        transport.open()
    elif six.PY3 and not transport.is_open():
        transport.open()


class HS2Service(ThriftRPC):

    def __init__(self, thrift_client, retries=3):
        ThriftRPC.__init__(self, thrift_client, retries=retries)

    def close(self):
        # pylint: disable=protected-access
        log.debug('close_service: client=%s', self.client)
        self.client._iprot.trans.close()

    def reconnect(self):
        # pylint: disable=protected-access
        log.debug('reconnect: client=%s', self.client)
        self.client._iprot.trans.close()
        self.client._iprot.trans.open()

    def open_session(self, user, configuration=None):
        protocol = TProtocolVersion.HIVE_CLI_SERVICE_PROTOCOL_V6
        req = TOpenSessionReq(client_protocol=protocol,
                              username=user,
                              configuration=configuration)
        resp = self._rpc('OpenSession', req)
        return HS2Session(self, resp.sessionHandle,
                          resp.configuration,
                          resp.serverProtocolVersion)


class HS2Session(ThriftRPC):

    def __init__(self, service, handle, config, hs2_protocol_version,
                 retries=3):
        # pylint: disable=protected-access
        self.service = service
        self.handle = handle
        self.config = config
        self.hs2_protocol_version = hs2_protocol_version

        if hs2_protocol_version not in TProtocolVersion._VALUES_TO_NAMES:
            raise HiveServer2Error("Got HiveServer2 version {0}; "
                                   "expected V1 - V6"
                                   .format(hs2_protocol_version))

        ThriftRPC.__init__(self, self.service.client, retries=retries)

    def close(self):
        req = TCloseSessionReq(sessionHandle=self.handle)
        self._rpc('CloseSession', req)

    def execute(self, statement, configuration=None, run_async=False):
        req = TExecuteStatementReq(sessionHandle=self.handle,
                                   statement=statement,
                                   confOverlay=configuration,
                                   runAsync=run_async)
        return self._operation('ExecuteStatement', req)

    def get_databases(self, schema='.*'):
        req = TGetSchemasReq(sessionHandle=self.handle, schemaName=schema)
        return self._operation('GetSchemas', req)

    def get_tables(self, database='.*', table_like='.*'):
        req = TGetTablesReq(sessionHandle=self.handle,
                            schemaName=database,
                            tableName=table_like)
        return self._operation('GetTables', req)

    def get_table_schema(self, table, database='.*'):
        req = TGetColumnsReq(sessionHandle=self.handle,
                             schemaName=database,
                             tableName=table, columnName='.*')
        return self._operation('GetColumns', req)

    def get_functions(self, database='.*'):
        # TODO: need to test this one especially
        req = TGetFunctionsReq(sessionHandle=self.handle,
                               schemaName=database,
                               functionName='.*')
        return self._operation('GetFunctions', req)

    def database_exists(self, db_name):
        op = self.get_databases(schema=db_name)

        # this only fetches default max_rows, but there should only be one row
        # ideally
        results = op.fetch()

        exists = False
        for result in results:
            if result[0].lower() == db_name.lower():
                exists = True
        op.close()
        return exists

    def table_exists(self, table, database='.*'):
        op = self.get_tables(database=database, table_like=table)
        results = op.fetch()
        exists = False
        for result in results:
            if result[2].lower() == table.lower():
                exists = True
        op.close()
        return exists

    def ping(self):
        req = TGetInfoReq(sessionHandle=self.handle,
                          infoType=TGetInfoType.CLI_SERVER_NAME)
        log.debug('ping: req=%s', req)
        try:
            resp = self.client.GetInfo(req)
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

    def _get_operation(self, handle):
        return Operation(self, handle)


class Operation(ThriftRPC):

    def __init__(self, session, handle, retries=3):
        self.session = session
        self.handle = handle
        self._schema = None
        ThriftRPC.__init__(self, self.session.client, retries=retries)

    @property
    def has_result_set(self):
        return self.handle.hasResultSet

    def get_status(self):
        # pylint: disable=protected-access
        req = TGetOperationStatusReq(operationHandle=self.handle)
        resp = self._rpc('GetOperationStatus', req)
        return TOperationState._VALUES_TO_NAMES[resp.operationState]

    def get_state(self):
        req = TGetOperationStatusReq(operationHandle=self.handle)
        return self._rpc('GetOperationStatus', req)

    def get_log(self, max_rows=1024, orientation=TFetchOrientation.FETCH_NEXT):
        try:
            req = TGetLogReq(operationHandle=self.handle)
            log = self._rpc('GetLog', req).log
        except TApplicationException as e: # raised if Hive is used
            if not e.type == TApplicationException.UNKNOWN_METHOD:
                raise
            req = TFetchResultsReq(operationHandle=self.handle,
                                   orientation=orientation,
                                   maxRows=max_rows,
                                   fetchType=1)
            resp = self._rpc('FetchResults', req)
            schema = [('Log', 'STRING', None, None, None, None, None)]
            log = self._wrap_results(resp.results, schema, convert_types=True)
            log = '\n'.join(l[0] for l in log)
        return log

    def cancel(self):
        req = TCancelOperationReq(operationHandle=self.handle)
        return self._rpc('CancelOperation', req)

    def close(self):
        req = TCloseOperationReq(operationHandle=self.handle)
        return self._rpc('CloseOperation', req)

    def get_profile(self, profile_format=TRuntimeProfileFormat.STRING):
        req = TGetRuntimeProfileReq(operationHandle=self.handle,
                                    sessionHandle=self.session.handle,
                                    format=profile_format)
        resp = self._rpc('GetRuntimeProfile', req)
        if profile_format == TRuntimeProfileFormat.THRIFT:
            return resp.thrift_profile
        return resp.profile

    def get_summary(self):
        req = TGetExecSummaryReq(operationHandle=self.handle,
                                 sessionHandle=self.session.handle)
        resp = self._rpc('GetExecSummary', req)
        return resp.summary

    def fetch(self, schema=None, max_rows=1024,
              orientation=TFetchOrientation.FETCH_NEXT,
              convert_types=True):
        if not self.has_result_set:
            log.debug('fetch_results: operation_handle.hasResultSet=False')
            return None

        # the schema is necessary to pull the proper values (i.e., coalesce)
        if schema is None:
            schema = self.get_result_schema()

        req = TFetchResultsReq(operationHandle=self.handle,
                               orientation=orientation,
                               maxRows=max_rows)
        resp = self._rpc('FetchResults', req)
        return self._wrap_results(resp.results, resp.hasMoreRows, schema,
                                  convert_types=convert_types)

    def _wrap_results(self, results, expect_more_rows, schema, convert_types=True):
        if self.is_columnar:
            log.debug('fetch_results: constructing CBatch')
            return CBatch(results, expect_more_rows, schema, convert_types=convert_types)
        else:
            log.debug('fetch_results: constructing RBatch')
            return RBatch(results, expect_more_rows, schema)

    @property
    def is_columnar(self):
        protocol = self.session.hs2_protocol_version
        return _is_columnar_protocol(protocol)

    def get_result_schema(self):
        if not self.handle.hasResultSet:
            log.debug('get_result_schema: handle.hasResultSet=False')
            return None

        req = TGetResultSetMetadataReq(operationHandle=self.handle)
        resp = self._rpc('GetResultSetMetadata', req)

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
