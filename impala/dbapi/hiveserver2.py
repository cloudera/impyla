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

import time
import getpass

from impala.dbapi.interface import Connection, Cursor, _bind_parameters
from impala._rpc import hiveserver2 as rpc
from impala.error import NotSupportedError, OperationalError, ProgrammingError
from impala._thrift_gen.TCLIService.ttypes import TProtocolVersion


class HiveServer2Connection(Connection):
    # PEP 249
    # HiveServer2Connection objects are associated with a TCLIService.Client
    # thrift service
    # it's instantiated with an alive TCLIService.Client

    def __init__(self, service, default_db=None):
        self.service = service
        self.default_db = default_db

    def close(self):
        """Close the session and the Thrift transport."""
        # PEP 249
        rpc.close_service(self.service)

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
        if user is None:
            user = getpass.getuser()
        if session_handle is None:
            (session_handle, default_config, hs2_protocol_version) = (
                rpc.open_session(self.service, user, configuration))
        cursor = HiveServer2Cursor(
            self.service, session_handle, default_config, hs2_protocol_version)
        if self.default_db is not None:
            cursor.execute('USE %s' % self.default_db)
        return cursor

    def reconnect(self):
        rpc.reconnect(self.service)


class HiveServer2Cursor(Cursor):
    # PEP 249
    # HiveServer2Cursor objects are associated with a Session
    # they are instantiated with alive session_handles

    def __init__(self, service, session_handle, default_config=None,
                 hs2_protocol_version=(
                     TProtocolVersion.HIVE_CLI_SERVICE_PROTOCOL_V6)):
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
        rpc.close_session(self.service, self.session_handle)

    def cancel_operation(self):
        if self._last_operation_active:
            rpc.cancel_operation(self.service, self._last_operation_handle)
            self._reset_state()

    def close_operation(self):
        if self._last_operation_active:
            self._reset_state()

    def execute(self, operation, parameters=None, configuration=None):
        # PEP 249
        def op():
            if parameters:
                self._last_operation_string = _bind_parameters(operation,
                                                               parameters)
            else:
                self._last_operation_string = operation
            self._last_operation_handle = rpc.execute_statement(
                self.service, self.session_handle, self._last_operation_string,
                configuration)

        self._execute_sync(op)

    def _execute_sync(self, operation_fn):
        # operation_fn should set self._last_operation_string and
        # self._last_operation_handle
        self._reset_state()
        operation_fn()
        self._last_operation_active = True
        self._wait_to_finish()  # make execute synchronous
        if self.has_result_set:
            schema = rpc.get_result_schema(self.service,
                                           self._last_operation_handle)
            self._description = schema

    def _reset_state(self):
        self._buffer = []
        self._description = None
        if self._last_operation_active:
            self._last_operation_active = False
            rpc.close_operation(self.service, self._last_operation_handle)
        self._last_operation_string = None
        self._last_operation_handle = None

    def _wait_to_finish(self):
        loop_start = time.time()
        while True:
            operation_state = rpc.get_operation_status(
                self.service, self._last_operation_handle)
            if operation_state == 'ERROR_STATE':
                raise OperationalError("Operation is in ERROR_STATE")
            if operation_state in ['FINISHED_STATE', 'CANCELED_STATE',
                                   'CLOSED_STATE', 'UKNOWN_STATE']:
                break
            # I'm in INITIALIZED_STATE or RUNNING_STATE or PENDING_STATE
            # so hang out
            time.sleep(self._get_sleep_interval(loop_start))

    def _get_sleep_interval(self, start_time):
        """Returns a step function of time to sleep in seconds before polling
        again. Maximum sleep is 1s, minimum is 0.1s"""
        elapsed = time.time() - start_time
        if elapsed < 10.0:
            return 0.1
        elif elapsed < 60.0:
            return 0.5
        return 1.0

    def executemany(self, operation, seq_of_parameters):
        # PEP 249
        for parameters in seq_of_parameters:
            self.execute(operation, parameters)
            if self.has_result_set:
                raise ProgrammingError("Operations that have result sets are "
                                       "not allowed with executemany.")

    def fetchone(self):
        # PEP 249
        if not self.has_result_set:
            raise ProgrammingError("Tried to fetch but no results.")
        try:
            return self.next()
        except StopIteration:
            return None

    def fetchmany(self, size=None):
        # PEP 249
        if not self.has_result_set:
            raise ProgrammingError("Tried to fetch but no results.")
        if size is None:
            size = self.arraysize
        local_buffer = []
        i = 0
        while i < size:
            try:
                local_buffer.append(self.next())
                i += 1
            except StopIteration:
                break
        return local_buffer

    def fetchall(self):
        # PEP 249
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

    def next(self):
        if not self.has_result_set:
            raise ProgrammingError(
                "Trying to fetch results on an operation with no results.")
        if len(self._buffer) > 0:
            return self._buffer.pop(0)
        elif self._last_operation_active:
            # self._buffer is empty here and op is active: try to pull more
            # rows
            rows = rpc.fetch_results(self.service, self._last_operation_handle,
                                     self.hs2_protocol_version,
                                     self.description, self.buffersize)
            self._buffer.extend(rows)
            if len(self._buffer) == 0:
                raise StopIteration
            return self._buffer.pop(0)
        else:
            # buffer is already empty
            raise StopIteration

    def ping(self):
        """Checks connection to server by requesting some info from the
        server."""
        return rpc.ping(self.service, self.session_handle)

    def get_log(self):
        return rpc.get_log(self.service, self._last_operation_handle)

    def get_profile(self):
        return rpc.get_profile(
            self.service, self._last_operation_handle, self.session_handle)

    def get_summary(self):
        return rpc.get_summary(
            self.service, self._last_operation_handle, self.session_handle)

    def build_summary_table(self, summary, output, idx=0,
                            is_fragment_root=False, indent_level=0):
        return rpc.build_summary_table(
            summary, idx, is_fragment_root, indent_level, output)

    def get_databases(self):
        def op():
            self._last_operation_string = "RPC_GET_DATABASES"
            self._last_operation_handle = rpc.get_databases(self.service,
                                                            self
                                                            .session_handle)
        self._execute_sync(op)

    def database_exists(self, db_name):
        return rpc.database_exists(self.service, self.session_handle,
                                   self.hs2_protocol_version, db_name)

    def get_tables(self, database_name=None):
        if database_name is None:
            database_name = '.*'

        def op():
            self._last_operation_string = "RPC_GET_TABLES"
            self._last_operation_handle = rpc.get_tables(self.service,
                                                         self.session_handle,
                                                         database_name)
        self._execute_sync(op)

    def table_exists(self, table_name, database_name=None):
        if database_name is None:
            database_name = '.*'
        return rpc.table_exists(self.service, self.session_handle,
                                self.hs2_protocol_version, table_name,
                                database_name)

    def get_table_schema(self, table_name, database_name=None):
        if database_name is None:
            database_name = '.*'

        def op():
            self._last_operation_string = "RPC_DESCRIBE_TABLE"
            self._last_operation_handle = rpc.get_table_schema(
                self.service, self.session_handle, table_name, database_name)

        self._execute_sync(op)
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
            self._last_operation_handle = rpc.get_functions(
                self.service, self.session_handle, database_name)

        self._execute_sync(op)
