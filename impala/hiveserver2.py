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

import getpass
import re
import socket

import datetime
import operator
import six
import sys
import time
from bitarray import bitarray
from six.moves import range

from thrift.transport.TTransport import TTransportException
from thrift.Thrift import TApplicationException
from thrift.protocol.TBinaryProtocol import TBinaryProtocolAccelerated
from impala._thrift_gen.TCLIService.ttypes import (
    TOpenSessionReq, TFetchResultsReq, TCloseSessionReq,
    TExecuteStatementReq, TGetInfoReq, TGetInfoType, TTypeId,
    TFetchOrientation, TGetResultSetMetadataReq, TStatusCode,
    TGetColumnsReq, TGetSchemasReq, TGetTablesReq, TGetFunctionsReq,
    TGetOperationStatusReq, TOperationState, TCancelOperationReq,
    TCloseOperationReq, TGetLogReq, TProtocolVersion)
from impala._thrift_gen.ImpalaService.ImpalaHiveServer2Service import (
    TGetRuntimeProfileReq, TGetExecSummaryReq, TCloseImpalaOperationReq)
from impala._thrift_api import (
    get_socket, get_http_transport, get_transport, ThriftClient)
from impala._thrift_gen.RuntimeProfile.ttypes import TRuntimeProfileFormat
from impala.compat import (Decimal, _xrange as xrange)
from impala.error import (NotSupportedError, OperationalError,
                          ProgrammingError, HiveServer2Error, HttpError)
from impala.interface import Connection, Cursor, _bind_parameters
from impala.util import get_logger_and_init_null

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
               dictify=False, fetch_error=True, close_finished_queries=True,
               convert_strings_to_unicode=True):
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
        convert_strings_to_unicode : bool, optional
            When `True`, the following types, which are transmitted as strings
            in HS2 protocol, will be converted to unicode: STRING, LIST, MAP, 
            STRUCT, UNIONTYPE, NULL, VARCHAR, CHAR, TIMESTAMP, DECIMAL, DATE.
            When `False`, conversion will occur only for types expected by 
            convert_types in python3: TIMESTAMP, DECIMAL, DATE.
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
        close_finished_queries : bool, optional
            If True, queries are closed after:
                - queries with results set: all rows are returned with fetch
                - DDL/DML: execution is finished
            If False, then the query will be only closed when:
                - execute() is called again on the cursor with a new query
                - close() is called on the cursor
                - the cursor's destructor is called
            Property 'rowcount' will not be available in the 'False' case for DML
            statements.
            Before closing the query GetLog() is called as this will be no longer
            possible after closing.
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
                              fetch_error=fetch_error,
                              close_finished_queries=close_finished_queries,
                              convert_strings_to_unicode=convert_strings_to_unicode)

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

    def __init__(self, session, convert_types=True, fetch_error=True, close_finished_queries=True,
                 convert_strings_to_unicode=True):
        self.session = session
        self.convert_types = convert_types
        self.convert_strings_to_unicode = convert_strings_to_unicode
        self.fetch_error = fetch_error
        self.close_finished_queries = close_finished_queries

        self._last_operation = None

        self._last_operation_string = None
        self._last_operation_active = False
        self._last_operation_finished = False
        self._last_operation_log = None
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
        # Note that _rowcount will be always -1 as we do not know the number of rows
        # until all rows are fetched from the query.
        return self._rowcount

    @property
    def rowcounts(self):
        # Work around to get the number of rows modified for Inserts/Update/Delete statements
        # Todo: For the non-Kudu case, this function could use self._rowcount without fetching
        #       and parsing the profile. This wouldn't be enough for Kudu as NumRowErrors is not
        #       included in DmlResult.
        modifiedRows, errorRows = -1, -1
        if self._last_operation is not None:
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
        # the size of the buffer, so that calling ._ensure_buffer_is_filled() will read
        # multiple rows into a buffer if arraysize hasn't been set.  (otherwise, we'd
        # get an unbuffered impl because the PEP 249 default value of arraysize
        # is 1)
        # Impala's batch size is 1024 and older versions of Impala will not return
        # more than 1024 rows in one fetch call. Using a bigger value (same as in
        # impala-shell) is useful if result spooling is enabled in Impala.
        return self._buffersize if self._buffersize else 10240

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
        if self._last_operation is not None:
            log.debug('Closing operation')
            self._reset_state()

    def _reset_state(self):
        log.debug('_reset_state: Resetting cursor state')
        self._buffer = Batch()
        self._description = None
        if self._last_operation_active:
            self._last_operation_active = False

            self._last_operation.close()
        self._last_operation_finished = False
        self._last_operation_string = None
        self._last_operation = None
        self._last_operation_log = None
        self._rowcount = -1

    def _set_rowcount_from_close_result(self, close_result):
        if not hasattr(close_result, 'dml_result') or not close_result.dml_result:
            return
        rows_modified_per_partition = close_result.dml_result.rows_modified
        self._rowcount = 0
        for _, val in rows_modified_per_partition.items():
            self._rowcount += val

    def _close_finished_operation(self):
        # Save the log as it can't be accessed after closing the query.
        self._last_operation_log = self.get_log()
        self._last_operation_active = False
        close_result = self._last_operation.close()
        log.debug('Query closed')
        # Set rowcount for DMLs.
        self._set_rowcount_from_close_result(close_result)

    def execute(self, operation, parameters=None, configuration=None):
        """Synchronously execute a SQL query.

        Blocks until results are available.
        For DMLs/DDLs if close_finished_queries is true then the query is
        closed once finished.

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
        if not self.has_result_set and self.close_finished_queries:
            # Close query if no results need to be fetched.
            self._close_finished_operation()


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
        if configuration and 'paramstyle' in configuration:
            configuration = configuration.copy()
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
        if self._last_operation is not None:
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
        if self._last_operation_finished:
            return
        loop_start = time.time()
        while True:
            start_rpc_time = time.time()
            req = TGetOperationStatusReq(operationHandle=self._last_operation.handle)
            resp = self._last_operation._rpc('GetOperationStatus', req, True)
            self._last_operation.update_has_result_set(resp)
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
                self._last_operation_finished = True
                break
            rpc_time = time.time() - start_rpc_time
            sleep_time = self._get_sleep_interval(loop_start)
            # Subtract RPC time from the total sleep time. If query option
            # long_polling_time_ms is set then Impala will sleep in GetOperationStatus
            # meaning that impyla may not need to sleep at all (IMPALA-13294).
            if rpc_time < sleep_time:
                time.sleep(sleep_time - rpc_time)

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
        rowcount = -1
        for parameters in seq_of_parameters:
            self.execute(operation, parameters, configuration)
            if self.has_result_set:
                raise ProgrammingError("Operations that have result sets are "
                                       "not allowed with executemany.")
            if self._rowcount != -1:
                if rowcount == -1:
                    rowcount = self._rowcount
                else:
                    rowcount += self._rowcount
        self._rowcount = rowcount

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
                         convert_types=self.convert_types,
                         convert_strings_to_unicode=self.convert_strings_to_unicode))
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
        while size > 0:
            try:
                elements = self._pop_from_buffer(size)
                local_buffer.extend(elements)
                size -= len(elements)
                assert size >= 0
            except StopIteration:
                break
        return local_buffer

    def fetchall(self):
        # PEP 249
        self._wait_to_finish()
        log.debug('Fetching all result rows')
        local_buffer = []
        while True:
            try:
                elements = self._pop_from_buffer(self.buffersize)
                local_buffer.extend(elements)
            except StopIteration:
                break
        return local_buffer

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
                         convert_types=self.convert_types,
                         convert_strings_to_unicode=self.convert_strings_to_unicode))
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
        self._ensure_buffer_is_filled()
        log.debug('__next__: popping row out of buffer')
        self._rowcount += 1
        return self._buffer.pop()

    def _ensure_buffer_is_filled(self):
        if self._rowcount == -1:
            self._rowcount = 0
        while True:
            if not self.has_result_set:
                raise ProgrammingError(
                    "Trying to fetch results on an operation with no results.")
            if len(self._buffer) > 0:
                return
            elif self._last_operation_active:
                log.debug('_ensure_buffer_is_filled: buffer empty and op is active '
                          '=> fetching more data')
                self._buffer = self._last_operation.fetch(self.description,
                    self.buffersize,
                    convert_types=self.convert_types,
                    convert_strings_to_unicode=self.convert_strings_to_unicode)
                if len(self._buffer) > 0:
                    return
                if not self._buffer.expect_more_rows:
                    log.debug('_ensure_buffer_is_filled: no more data to fetch')
                    if self.close_finished_queries:
                        # Close query as it no longer has rows.
                        # TODO: this could be done earlier after calling fetch - not sure
                        #       if this would bring enough benefits to worth complicating
                        #       the state machine
                        self._close_finished_operation()
                    raise StopIteration
                # If we didn't get rows, but more are expected, need to iterate again.
            else:
                log.debug('_ensure_buffer_is_filled: buffer empty')
                raise StopIteration

    def _pop_from_buffer(self, size):
        self._ensure_buffer_is_filled()
        log.debug('pop_from_buffer: popping row out of buffer')
        elements = self._buffer.pop_many(size)
        self._rowcount += len(elements)
        return elements

    def ping(self):
        """Checks connection to server by requesting some info."""
        log.info('Pinging the impalad')
        return self.session.ping()

    def get_log(self):
        if self._last_operation is None:
            raise ProgrammingError("Operation state is not available")
        if self._last_operation_log is not None:
            # Return the log saved before closing the query.
            return self._last_operation_log
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

    def _pop_from_buffer(self, size):
        records = super(self.__class__, self)._pop_from_buffer(size)
        return [dict(zip(self.fields, record)) for record in records]


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

# Regex to extract year/month/date from date.
_DATE_PATTERN = re.compile(r'(\d+)-(\d+)-(\d+)')

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

def _parse_date(value):
    if value:
        match = _DATE_PATTERN.match(value)
        if match:
          return datetime.date(int(match.group(1)), int(match.group(2)), int(match.group(3)))
        else:
            raise Exception(
                'Cannot convert "{}" into a date'.format(value))
    return value


# TODO: Add another decorator that runs the function in its own thread
def threaded(func):
    # pylint: disable=unused-argument
    raise NotImplementedError


def connect(host, port, timeout=None, use_ssl=False, ca_cert=None,
            user=None, password=None, kerberos_service_name='impala',
            auth_mechanism=None, krb_host=None, use_http_transport=False,
            http_path='', http_cookie_names=None, retries=3, jwt=None,
            user_agent=None, get_user_custom_headers_func=None):
    log.debug('Connecting to HiveServer2 %s:%s with %s authentication '
              'mechanism', host, port, auth_mechanism)

    if krb_host:
        kerberos_host = krb_host
    else:
        kerberos_host = host

    if use_http_transport:
        # TODO(#362): Add server authentication with thrift 0.12.
        if ca_cert:
            raise NotSupportedError("Server authentication is not supported " +
                                    "with HTTP endpoints")

        transport = get_http_transport(
            host, port, http_path=http_path,
            use_ssl=use_ssl, ca_cert=ca_cert,
            auth_mechanism=auth_mechanism,
            user=user, password=password,
            kerberos_host=kerberos_host,
            kerberos_service_name=kerberos_service_name,
            http_cookie_names=http_cookie_names,
            jwt=jwt, user_agent=user_agent,
            get_user_custom_headers_func=get_user_custom_headers_func)
    else:
        sock = get_socket(host, port, use_ssl, ca_cert)

        if timeout is not None:
            timeout = timeout * 1000.  # TSocket expects millis
        sock.setTimeout(timeout)
        log.debug('sock=%s', sock)
        transport = get_transport(sock, kerberos_host, kerberos_service_name,
                                auth_mechanism, user, password)

    transport.open()
    protocol = TBinaryProtocolAccelerated(transport)
    service = ThriftClient(protocol)
    log.debug('transport=%s protocol=%s service=%s', transport, protocol,
              service)

    return HS2Service(service, retries=retries)


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

    def pop_to_preallocated_list(self, output_list, count, offset=0, stride=1):
        """ Tries to pop 'count' values and write them to every 'stride'th element of
            'output_list' starting with 'offset'.
            Returns the number of values popped.
        """
        count = min(count, self.rows_left)
        start_pos = self.num_rows - self.rows_left
        self.rows_left -= count
        for pos in xrange(start_pos, start_pos + count):
            output_list[offset] = None if self.nulls[pos] else self.values[pos]
            offset += stride
        return count


class CBatch(Batch):

    def __init__(self, trowset, expect_more_rows, schema, convert_types=True,
                 convert_strings_to_unicode=True):
        self.expect_more_rows = expect_more_rows
        self.schema = schema
        tcols = [_TTypeId_to_TColumnValue_getters[schema[i][1]](col)
                 for (i, col) in enumerate(trowset.columns)]
        num_cols = len(tcols)
        num_rows = len(tcols[0].values)
        self.remaining_rows = num_rows

        log.debug('CBatch: input TRowSet num_cols=%s num_rows=%s tcols=%s',
                  num_cols, num_rows, tcols)
        
        HS2_STRING_TYPES = ["STRING", "LIST", "MAP", "STRUCT", "UNIONTYPE", "NULL", "VARCHAR", "CHAR", "TIMESTAMP", "DECIMAL", "DATE"]
        CONVERTED_TYPES=["TIMESTAMP", "DECIMAL", "DATE"]

        self.columns = []
        for j in range(num_cols):
            type_ = schema[j][1]
            nulls = tcols[j].nulls
            values = tcols[j].values

            is_null = bitarray(endian='little')
            is_null.frombytes(nulls)

            # Ref HUE-2722, HiveServer2 sometimes does not add trailing '\x00'
            if len(values) > len(nulls):
                to_append = ((len(values) - len(nulls) + 7) // 8)
                is_null.frombytes(b'\x00' * to_append)

            # STRING columns are read as binary and decoded here to be able to handle
            # non-valid utf-8 strings in Python 3.

            if six.PY3:
                if convert_strings_to_unicode:
                    self._convert_strings_to_unicode(type_, is_null, values, types=HS2_STRING_TYPES)
                elif convert_types:
                    self._convert_strings_to_unicode(type_, is_null, values, types=CONVERTED_TYPES)

            if convert_types:
                values = self._convert_values(type_, is_null, values)

            self.columns.append(Column(type_, values, is_null))

    def _convert_strings_to_unicode(self, type_, is_null, values, types):
        if type_ in types:
            for i in range(len(values)):
                if is_null[i]:
                    values[i] = None
                    continue
                try:
                    # Do similar handling of non-valid UTF-8 strings as Thriftpy2:
                    # https://github.com/Thriftpy/thriftpy2/blob/8e218b3fd89c597c2e83d129efecfe4d280bdd89/thriftpy2/protocol/binary.py#L241
                    # If decoding fails then keep the original bytearray.
                    values[i] = values[i].decode("UTF-8")
                except UnicodeDecodeError:
                    pass

    def _convert_values(self, type_, is_null, values):
        # pylint: disable=consider-using-enumerate
        if type_ == 'TIMESTAMP':
            for i in range(len(values)):
                values[i] = (None if is_null[i] else
                             _parse_timestamp(values[i]))
        elif type_ == 'DECIMAL':
            for i in range(len(values)):
                values[i] = (None if is_null[i] else Decimal(values[i]))
        elif type_ == 'DATE':
            for i in range(len(values)):
                values[i] = (None if is_null[i] else _parse_date(values[i]))
        return values

    def __len__(self):
        return self.remaining_rows

    def pop(self):
        self.remaining_rows -= 1
        return tuple([c.pop() for c in self.columns])

    def __str__(self):
        col_string = ','.join([str(col) for col in self.columns])
        return 'CBatch({0})'.format(col_string)

    def pop_many(self, row_count):
        """Returns a list of tuples with min('row_count', rows in batch) elements."""
        row_count = min(row_count, self.remaining_rows)
        self.remaining_rows -= row_count
        col_count = len(self.columns)
        # 'dataset' holds all rows x columns in list in row major order.
        # The transposition of columnar data is done by writing 'dataset' per-column
        # and then returning it per-row.
        dataset = [None] * (col_count * row_count)
        for col_id, col in enumerate(self.columns):
            rows_returned = col.pop_to_preallocated_list(
                dataset, row_count, offset=col_id, stride=col_count)
            assert row_count == rows_returned
        # Split 'dataset' to 'col_count' sized sublists and create tuples from them.
        return [tuple(dataset[i * col_count: (i + 1) * col_count])
                for i in xrange(row_count)]


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
        # TODO: this looks extremely inefficient
        return self.rows.pop(0)

    def pop_many(self, row_count):
        row_count = min(row_count, len(self.rows))
        result = self.rows[:row_count]
        self.rows = self.rows[row_count:]
        return result


class ThriftRPC(object):

    def __init__(self, client, retries=3):
        self.client = client
        self.retries = retries

    def _rpc(self, func_name, request, safe_to_retry=False):
        self._log_request(func_name, request)
        response = self._execute(func_name, request, safe_to_retry)
        self._log_response(func_name, response)
        err_if_rpc_not_ok(response)
        return response

    def _execute(self, func_name, request, safe_to_retry=False):
        # pylint: disable=protected-access
        # get the thrift transport
        transport = self.client._iprot.trans
        tries_left = self.retries
        last_exception = None
        open_finished = False
        while tries_left > 0:
            try:
                log.debug('Attempting to open transport (tries_left=%s)',
                          tries_left)
                open_transport(transport)
                open_finished = True
                log.debug('Transport opened')
                func = getattr(self.client, func_name)
                return func(request)
            except (socket.error, TTransportException) as e:
                if open_finished and not safe_to_retry: raise e
                msg = "RPC failed" if open_finished else "Failed to open transport"
                log.exception('%s (tries_left=%s)', msg, tries_left)
                last_exception = e
            except HttpError as h:
                if not safe_to_retry:
                    log.debug('Caught HttpError %s %s in %s which is not retryable',
                              h, str(h.body or ''), func_name)
                    raise
                last_exception = h
                if tries_left > 1:
                    retry_secs = None
                    retry_after = h.http_headers.get('Retry-After', None)
                    if retry_after:
                        try:
                            retry_secs = int(retry_after)
                        except ValueError:
                            retry_secs = None
                    if retry_secs:
                        log.debug("sleeping after seeing Retry-After value of %d", retry_secs)
                        log.debug('Caught HttpError %s %s in %s (tries_left=%s), retry after %d secs',
                                  h, str(h.body or ''), func_name, tries_left, retry_secs)
                        time.sleep(retry_secs)
                    else:
                        retry_secs = 1  # Future: use exponential backoff?
                        log.debug("sleeping for %d second before retrying", retry_secs)
                        time.sleep(retry_secs)
                        log.debug('Caught HttpError %s %s in %s (tries_left=%s)',
                                  h, str(h.body or ''), func_name, tries_left)

            except Exception:
                raise
            log.debug('Closing transport (tries_left=%s)', tries_left)
            transport.close()
            open_finished = False
            tries_left -= 1

        if last_exception:
            raise last_exception
        raise HiveServer2Error('Failed after retrying {0} times'
                               .format(self.retries))

    def _operation(self, kind, request, safe_to_retry=False):
        resp = self._rpc(kind, request, safe_to_retry)
        return self._get_operation(resp.operationHandle)

    def _log_request(self, kind, request):
        log.debug('%s: req=%s', kind, request)

    def _log_response(self, kind, response):
        log.debug('%s: resp=%s', kind, response)


def open_transport(transport):
    """
    Open transport if needed.
    """
    if not transport.isOpen():
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
        # OpenSession rpcs are idempotent and so ok to retry. If the client gets
        # disconnected and the server successfully opened a session, the client
        # will retry and rely on server to clean up the session.
        resp = self._rpc('OpenSession', req, True)
        return HS2Session(self, resp.sessionHandle,
                          resp.configuration,
                          resp.serverProtocolVersion,
                          retries=self.retries)


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
        # CloseSession rpcs don't retry as a session cannot be closed twice.
        self._rpc('CloseSession', req, False)

    def execute(self, statement, configuration=None, run_async=False):
        req = TExecuteStatementReq(sessionHandle=self.handle,
                                   statement=statement,
                                   confOverlay=configuration,
                                   runAsync=run_async)
        # Do not attempt to retry requests.
        # Read queries should be idempotent but most dml queries are not. Also retrying
        # query execution from client could be expensive and so likely makes sense to do
        # it if server is also aware of the retries.
        return self._operation('ExecuteStatement', req, False)

    def get_databases(self, schema='.*'):
        req = TGetSchemasReq(sessionHandle=self.handle, schemaName=schema)
        return self._operation('GetSchemas', req, True)

    def get_tables(self, database='.*', table_like='.*'):
        req = TGetTablesReq(sessionHandle=self.handle,
                            schemaName=database,
                            tableName=table_like)
        return self._operation('GetTables', req, True)

    def get_table_schema(self, table, database='.*'):
        req = TGetColumnsReq(sessionHandle=self.handle,
                             schemaName=database,
                             tableName=table, columnName='.*')
        return self._operation('GetColumns', req, True)

    def get_functions(self, database='.*'):
        # TODO: need to test this one especially
        req = TGetFunctionsReq(sessionHandle=self.handle,
                               schemaName=database,
                               functionName='.*')
        return self._operation('GetFunctions', req, True)

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
        return Operation(self, handle,
                         retries=self.retries)


class Operation(ThriftRPC):

    def __init__(self, session, handle, retries=3):
        self.session = session
        self.handle = handle
        self._schema = None
        self._state_has_result_set = None
        ThriftRPC.__init__(self, self.session.client, retries=retries)

    @property
    def has_result_set(self):
        # When HIVE_CLI_SERVICE_PROTOCOL_V10 or later API is used and async compilation is
        # enabled, self.handle.hasResultSet is not set any longer.
        # In this case self._state_has_result_set should be used instead.
        if self._state_has_result_set is not None:
            return self._state_has_result_set
        else:
            return self.handle.hasResultSet

    def update_has_result_set(self, state):
        self._state_has_result_set = state.hasResultSet

    def get_status(self):
        # pylint: disable=protected-access
        req = TGetOperationStatusReq(operationHandle=self.handle)
        # GetOperationStatus rpc is idempotent and so safe to retry.
        resp = self._rpc('GetOperationStatus', req, True)
        self.update_has_result_set(resp)
        return TOperationState._VALUES_TO_NAMES[resp.operationState]

    def get_state(self):
        req = TGetOperationStatusReq(operationHandle=self.handle)
        # GetOperationStatus rpc is idempotent and so safe to retry.
        resp = self._rpc('GetOperationStatus', req, True)
        self.update_has_result_set(resp)
        return resp

    def get_log(self, max_rows=1024, orientation=TFetchOrientation.FETCH_NEXT):
        try:
            req = TGetLogReq(operationHandle=self.handle)
            # GetLog rpc is idempotent and so safe to retry.
            log = self._rpc('GetLog', req, True).log
        except TApplicationException as e: # raised if Hive is used
            if not e.type == TApplicationException.UNKNOWN_METHOD:
                raise
            req = TFetchResultsReq(operationHandle=self.handle,
                                   orientation=orientation,
                                   maxRows=max_rows,
                                   fetchType=1)
            resp = self._rpc('FetchResults', req, False)
            schema = [('Log', 'STRING', None, None, None, None, None)]
            log = self._wrap_results(resp.results, resp.hasMoreRows, schema,
                convert_types=True, convert_strings_to_unicode=True)
            log = '\n'.join(l[0] for l in log)
        return log

    def cancel(self):
        req = TCancelOperationReq(operationHandle=self.handle)
        # CancelOperation rpc is idempotent and so safe to retry.
        return self._rpc('CancelOperation', req, True)

    def close(self):
        # Try Impala specific CloseImpalaOperation() as it also returns the number of
        # modified rows for DML statements.
        # If it doesn't exist (Hive, old Impala) fallback to regular HS2 CloseOperation()
        # The RPCs are not retried as CloseOperation rpc is not idempotent for dml and we're not sure
        # here if this is dml or not.
        # TODO: we know in many cases that the query can't be a DML. Not sure if it worth putting
        #       effort into retrying close()
        try:
            req = TCloseImpalaOperationReq(operationHandle=self.handle)
            return self._rpc('CloseImpalaOperation', req, False)
        except TApplicationException as e:
            if not e.type == TApplicationException.UNKNOWN_METHOD:
                raise
            req = TCloseOperationReq(operationHandle=self.handle)
            return self._rpc('CloseOperation', req, False)

    def get_profile(self, profile_format=TRuntimeProfileFormat.STRING):
        req = TGetRuntimeProfileReq(operationHandle=self.handle,
                                    sessionHandle=self.session.handle,
                                    format=profile_format)
        # GetRuntimeProfile rpc is idempotent and so safe to retry.
        resp = self._rpc('GetRuntimeProfile', req, True)
        if profile_format == TRuntimeProfileFormat.THRIFT:
            return resp.thrift_profile
        return resp.profile

    def get_summary(self):
        req = TGetExecSummaryReq(operationHandle=self.handle,
                                 sessionHandle=self.session.handle)
        # GetExecSummary rpc is idempotent and so safe to retry.
        resp = self._rpc('GetExecSummary', req, True)
        return resp.summary

    def fetch(self, schema=None, max_rows=1024,
              orientation=TFetchOrientation.FETCH_NEXT,
              convert_types=True, convert_strings_to_unicode=True):
        if not self.has_result_set:
            log.debug('fetch_results: has_result_set=False')
            return None

        # the schema is necessary to pull the proper values (i.e., coalesce)
        if schema is None:
            schema = self.get_result_schema()

        req = TFetchResultsReq(operationHandle=self.handle,
                               orientation=orientation,
                               maxRows=max_rows)
        # FetchResults rpc is not idempotent unless the client and server communicate and
        # results are kept around for retry to be successful.
        resp = self._rpc('FetchResults', req, False)
        return self._wrap_results(resp.results, resp.hasMoreRows, schema,
                                  convert_types=convert_types, 
                                  convert_strings_to_unicode=convert_strings_to_unicode)

    def _wrap_results(self, results, expect_more_rows, schema, convert_types=True, 
                      convert_strings_to_unicode=True):
        if self.is_columnar:
            log.debug('fetch_results: constructing CBatch')
            return CBatch(results, expect_more_rows, schema, convert_types=convert_types, 
                          convert_strings_to_unicode=convert_strings_to_unicode)
        else:
            log.debug('fetch_results: constructing RBatch')
            # TODO: RBatch ignores 'convert_types' and 'convert_strings_to_unicode'
            return RBatch(results, expect_more_rows, schema)

    @property
    def is_columnar(self):
        protocol = self.session.hs2_protocol_version
        return _is_columnar_protocol(protocol)

    def get_result_schema(self):
        if not self.has_result_set:
            log.debug('get_result_schema: has_result_set=False')
            return None

        req = TGetResultSetMetadataReq(operationHandle=self.handle)
        resp = self._rpc('GetResultSetMetadata', req, True)

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
