# Copyright 2013 Cloudera Inc.
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

"""Implements the Python DB API 2.0 (PEP 249) for Impala"""

import getpass
import time
import datetime

import hs2_client, beeswax_client
from impala.cli_service.ttypes import TTypeId
from error import (Error, Warning, InterfaceError, DatabaseError,
                          InternalError, OperationalError, ProgrammingError,
                          IntegrityError, DataError, NotSupportedError)
from beeswaxd.BeeswaxService import QueryState


# PEP 249 module globals
apilevel = '2.0'
threadsafety = 1  # Threads may share the module, but not connections
paramstyle = 'pyformat'

BEESWAX_PORT = '21000'
HIVESERVER2_PORT = '21050'

HIVESERVER2 = "hiveserver2"
BEESWAX = "beeswax"

def connect(host='localhost', port=HIVESERVER2_PORT, protocol=HIVESERVER2, timeout=45,
            use_ssl=False, ca_cert=None, use_ldap=False, ldap_user=None, ldap_password=None,
            use_kerberos=False, kerberos_service_name='impala'):
    # PEP 249
    if protocol.lower() == BEESWAX:
        service = beeswax_client.connect_to_impala(host, port, timeout, use_ssl,
            ca_cert, use_ldap, ldap_user, ldap_password, use_kerberos,
            kerberos_service_name)
        return BeeswaxConnection(service)
    elif protocol.lower() == HIVESERVER2:
        service = hs2_client.connect_to_impala(host, port, timeout, use_ssl,
            ca_cert, use_ldap, ldap_user, ldap_password, use_kerberos,
            kerberos_service_name)
        return HiveServer2Connection(service)
    else:
        raise NotSupportedError("The specified protocol '%s' is not supported." % protocol)


class Connection(object):
    # PEP 249
    # Connection objects are associated with a TCLIService.Client thrift service
    # it's instantiated with an alive TCLIService.Client

    def close(self):
        # PEP 249
        raise NotImplementedError()

    def commit(self):
        # PEP 249
        raise NotImplementedError()

    def rollback(self):
        # PEP 249
        raise NotImplementedError()

    def cursor(self, session_handle=None, user=None, configuration=None):
        # PEP 249
        raise NotImplementedError()

    def reconnect(self):
        raise NotImplementedError()

    # optional DB API addition to make the errors attributes of Connection
    Error = Error
    Warning = Warning
    InterfaceError = InterfaceError
    DatabaseError = DatabaseError
    InternalError = InternalError
    OperationalError = OperationalError
    ProgrammingError = ProgrammingError
    IntegrityError = IntegrityError
    DataError = DataError
    NotSupportedError = NotSupportedError

class BeeswaxConnection(object):
    # PEP 249

    def __init__(self, service):
        self.service = service

        self.default_query_options = {}

    def close(self):
        """Close the session and the Thrift transport."""
        # PEP 249
        beeswax_client.close_service(self.service)

    def commit(self):
        """Impala doesn't support transactions; does nothing."""
        # PEP 249
        pass

    def rollback(self):
        """Impala doesn't support transactions; raises NotSupportedError"""
        # PEP 249
        raise NotSupportedError()

    def cursor(self, session_handle=None, user=None, configuration=None):
        # PEP 249
        if user is None:
            user = getpass.getuser()
        if session_handle is None:
            options = beeswax_client.build_default_query_options_dict(self.service)
            for opt in options:
                self.default_query_options[opt.key.upper()] = opt.value
        return BeeswaxCursor(self.service, user, session_handle)

    def reconnect(self):
        beeswax_client.reconnect(self.service)

class HiveServer2Connection(object):
    # PEP 249
    # HiveServer2Connection objects are associated with a TCLIService.Client thrift service
    # it's instantiated with an alive TCLIService.Client

    def __init__(self, service):
        self.service = service

        self.default_query_options = {}

    def close(self):
        """Close the session and the Thrift transport."""
        # PEP 249
        hs2_client.close_service(self.service)

    def commit(self):
        """Impala doesn't support transactions; does nothing."""
        # PEP 249
        pass

    def rollback(self):
        """Impala doesn't support transactions; raises NotSupportedError"""
        # PEP 249
        raise NotSupportedError()

    def cursor(self, session_handle=None, user=None, configuration=None):
        # PEP 249
        if user is None:
            user = getpass.getuser()
        if session_handle is None:
            session_handle, options = hs2_client.open_session(self.service, user, configuration)
            for opt in options:
                self.default_query_options[opt.upper()] = options[opt]
        return HS2Cursor(self.service, session_handle)

    def reconnect(self):
        hs2_client.reconnect(self.service)

class Cursor(object):
    """Abstract representation of Cursor
    Compatible with pre-python 2.6"""

    def description(self):
        raise NotImplementedError()

    def rowcount(self):
        raise NotImplementedError()

    def query_string(self):
        raise NotImplementedError()

    def get_arraysize(self):
        raise NotImplementedError()

    def set_arraysize(self, arraysize):
        raise NotImplementedError()

    def buffersize(self):
        raise NotImplementedError()

    def has_result_set(self):
        raise NotImplementedError()

    def close(self):
        raise NotImplementedError()

    def close_operation(self):
        raise NotImplementedError()

    def execute(self, operation, parameters=None, configuration=None):
        raise NotImplementedError()

    def _execute_sync(self, operation_fn):
        raise NotImplementedError()

    def _reset_state(self):
        raise NotImplementedError()

    def _wait_to_finish(self):
        raise NotImplementedError()

    def executemany(self, operation, seq_of_parameters=[]):
        raise NotImplementedError()

    def fetchone(self):
        raise NotImplementedError()

    def fetchmany(self, size=None):
        raise NotImplementedError()

    def fetchall(self):
        raise NotImplementedError()

    def setinputsizes(self, sizes):
        raise NotImplementedError()

    def setoutputsize(self, size, column=None):
        raise NotImplementedError()

    def __iter__(self):
        raise NotImplementedError()

    def next(self):
        raise NotImplementedError()

    def ping(self):
        raise NotImplementedError()

    def get_log(self):
        raise NotImplementedError()

    def get_profile(self):
        raise NotImplementedError()

    def get_summary(self):
        raise NotImplementedError()

    def build_summary_table(self, summary, idx, is_fragment_root, indent_level, output):
        raise NotImplementedError()

class BeeswaxCursor(Cursor):
    # PEP 249
    # Beeswax does notsupport sessions

    def __init__(self, service, session_handle, user):
        self.service = service
        self.session_handle = session_handle
        self.user = user

        self._last_operation_string = None
        self._last_operation_handle = None
        self._last_operation_active = False
        self._buffersize = None
        self._buffer = []

        # initial values, per PEP 249
        self._description = None
        self._rowcount = -1

        self.query_state = QueryState._NAMES_TO_VALUES

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
        # rows into a buffer if arraysize hasn't been set.  (otherwise, we'd get
        # an unbuffered impl because the PEP 249 default value of arraysize is 1)
        return self._buffersize if self._buffersize else 1024

    @property
    def has_result_set(self):
        return (self._last_operation_handle is not None and
                beeswax_client.expect_result_metadata(self._last_operation_string))

    def close(self):
        # PEP 249
        pass

    def cancel_operation(self):
        if self._last_operation_active:
            self._last_operation_active = False
            beeswax_client.cancel_query(self.service, self._last_operation_handle)

    def close_operation(self):
        if self._last_operation_active:
            self._last_operation_active = False
            beeswax_client.close_query(self.service, self._last_operation_handle)

    def execute(self, operation, parameters=None, configuration=None):
        # PEP 249
        def op():
            if parameters:
                self._last_operation_string = _bind_parameters(operation, parameters)
            else:
                self._last_operation_string = operation
            self._last_operation_handle = beeswax_client.execute_statement(self.service,
              beeswax_client.create_beeswax_query(self._last_operation_string, self.user, configuration))
        self._execute_sync(op)

    def _execute_sync(self, operation_fn):
        # operation_fn should set self._last_operation_string and
        # self._last_operation_handle
        self._reset_state()
        operation_fn()
        self._last_operation_active = True
        self._rowcount = 0
        self._wait_to_finish()  # make execute synchronous
        if self.has_result_set:
            schema = beeswax_client.get_column_names(self.service,
                    self._last_operation_handle)
            self._description = [tuple([col] + [None, None, None, None, None]) for col in schema]
        else:
            self._last_operation_active = False
            beeswax_client.close_query(self.service, self._last_operation_handle)

    def _reset_state(self):
        self._buffer = []
        self._rowcount = -1
        self._description = None
        if self._last_operation_active:
            self._last_operation_active = False
            beeswax_client.close_query(self.service, self._last_operation_handle)
        self._last_operation_string = None
        self._last_operation_handle = None

    def _wait_to_finish(self):
        loop_start = time.time()
        while True:
            operation_state = beeswax_client.get_query_state(self.service,
                                                             self._last_operation_handle)
            if operation_state == self.query_state["FINISHED"]:
                break
            elif operation_state == self.query_state["EXCEPTION"]:
                raise OperationalError(self.get_log())
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

    def executemany(self, operation, seq_of_parameters=[]):
        # PEP 249
        for parameters in seq_of_parameters:
            self.execute(operation, parameters)
            if self.has_result_set:
                raise ProgrammingError("Operations that have result sets are not allowed with executemany.")

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
        self._rowcount += len(local_buffer)
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
            raise ProgrammingError("Trying to fetch results on an operation with no results.")
        if len(self._buffer) > 0:
            return self._buffer.pop(0)
        elif self._last_operation_active:
            # self._buffer is empty here and op is active: try to pull more rows
            rows = beeswax_client.fetch_internal(self.service,
                    self._last_operation_handle, self.buffersize)
            self._buffer.extend(rows)
            if len(self._buffer) == 0:
                self._last_operation_active = False
                beeswax_client.close_query(self.service, self._last_operation_handle)
                raise StopIteration
            return self._buffer.pop(0)
        else:
            # empty buffer and op is now closed: raise StopIteration
            raise StopIteration

    def ping(self):
        """Checks connection to server by requesting some info from the server."""
        return beeswax_client.ping(self.service)

    def get_log(self):
        return beeswax_client.get_warning_log(self.service, self._last_operation_handle)

    def get_profile(self):
        return beeswax_client.get_runtime_profile(self.service, self._last_operation_handle)

    def get_summary(self):
        return beeswax_client.get_summary(self.service, self._last_operation_handle)

    def build_summary_table(self, summary, idx=0, is_fragment_root=False, indent_level=0, output=[]):
        return beeswax_client.build_summary_table(summary, idx, is_fragment_root, indent_level, output)

class HS2Cursor(Cursor):

    # PEP 249
    # HS2Cursor objects are associated with a Session
    # they are instantiated with alive session_handles

    def __init__(self, service, session_handle):
        self.service = service
        self.session_handle = session_handle

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
        # rows into a buffer if arraysize hasn't been set.  (otherwise, we'd get
        # an unbuffered impl because the PEP 249 default value of arraysize is 1)
        return self._buffersize if self._buffersize else 1024

    @property
    def has_result_set(self):
        return (self._last_operation_handle is not None and
                self._last_operation_handle.hasResultSet)

    def close(self):
        # PEP 249
        hs2_client.close_session(self.service, self.session_handle)

    def cancel_operation(self):
        if self._last_operation_active:
            self._last_operation_active = False
            hs2_client.cancel_operation(self.service, self._last_operation_handle)

    def close_operation(self):
        if self._last_operation_active:
            self._last_operation_active = False
            hs2_client.close_operation(self.service, self._last_operation_handle)

    def execute(self, operation, parameters=None, configuration=None):
        # PEP 249
        def op():
            if parameters:
                self._last_operation_string = _bind_parameters(operation, parameters)
            else:
                self._last_operation_string = operation
            self._last_operation_handle = hs2_client.execute_statement(
                    self.service, self.session_handle, self._last_operation_string)
        self._execute_sync(op)

    def _execute_sync(self, operation_fn):
        # operation_fn should set self._last_operation_string and
        # self._last_operation_handle
        self._reset_state()
        operation_fn()
        self._last_operation_active = True
        self._rowcount = 0
        self._wait_to_finish()  # make execute synchronous
        if self.has_result_set and self._last_operation_active:
            schema = hs2_client.get_result_schema(self.service,
                    self._last_operation_handle)
            self._description = [tup + (None, None, None, None, None) for tup in schema]
        else:
            self._last_operation_active = False
            hs2_client.close_operation(self.service, self._last_operation_handle)

    def _reset_state(self):
        self._buffer = []
        self._rowcount = -1
        self._description = None
        if self._last_operation_active:
            self._last_operation_active = False
            hs2_client.close_operation(self.service, self._last_operation_handle)
        self._last_operation_string = None
        self._last_operation_handle = None

    def _wait_to_finish(self):
        loop_start = time.time()
        while True:
            operation_state = hs2_client.get_operation_status(self.service,
                                                              self._last_operation_handle)
            if operation_state == 'FINISHED_STATE':
                break
            elif operation_state == 'ERROR_STATE':
                raise OperationalError("Cancelled")
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

    def executemany(self, operation, seq_of_parameters=[]):
        # PEP 249
        for parameters in seq_of_parameters:
            self.execute(operation, parameters)
            if self.has_result_set:
                raise ProgrammingError("Operations that have result sets are not allowed with executemany.")

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
        self._rowcount += len(local_buffer)
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
            raise ProgrammingError("Trying to fetch results on an operation with no results.")
        if len(self._buffer) > 0:
            return self._buffer.pop(0)
        elif self._last_operation_active:
            # self._buffer is empty here and op is active: try to pull more rows
            rows = hs2_client.fetch_results(self.service,
                    self._last_operation_handle, self.description,
                    self.buffersize)
            self._buffer.extend(rows)
            if len(self._buffer) == 0:
                self._last_operation_active = False
                hs2_client.close_operation(self.service, self._last_operation_handle)
                raise StopIteration
            return self._buffer.pop(0)
        else:
            # empty buffer and op is now closed: raise StopIteration
            raise StopIteration

    def ping(self):
        """Checks connection to server by requesting some info from the server."""
        if hs2_client.ping(self.service, self.session_handle):
            return "Hive Server 2"
        else:
            return "SERVER NOT FOUND"

    def get_log(self):
        return hs2_client.get_log(self.service, self._last_operation_handle)

    def get_profile(self):
        return hs2_client.get_profile(self.service, self._last_operation_handle, self.session_handle)

    def get_summary(self):
        return hs2_client.get_summary(self.service, self._last_operation_handle, self.session_handle)

    def build_summary_table(self, summary, idx=0, is_fragment_root=False, indent_level=0, output=[]):
        return hs2_client.build_summary_table(summary, idx, is_fragment_root, indent_level, output)

    def get_databases(self):
        def op():
            self._last_operation_string = "RPC_GET_DATABASES"
            self._last_operation_handle = hs2_client.get_databases(self.service,
                        self.session_handle)
        self._execute_sync(op)

    def database_exists(self, db_name):
        return hs2_client.database_exists(self.service, self.session_handle,
                db_name)

    def get_tables(self, database_name=None):
        if database_name is None:
            database_name = '.*'
        def op():
            self._last_operation_string = "RPC_GET_TABLES"
            self._last_operation_handle = hs2_client.get_tables(self.service,
                    self.session_handle, database_name)
        self._execute_sync(op)

    def table_exists(self, table_name, database_name=None):
        if database_name is None:
            database_name = '.*'
        return hs2_client.table_exists(self.service, self.session_handle,
                    table_name, database_name)

    def get_table_schema(self, table_name, database_name=None):
        if database_name is None:
            database_name = '.*'
        def op():
            self._last_operation_string = "RPC_DESCRIBE_TABLE"
            self._last_operation_handle = hs2_client.get_table_schema(self.service,
                    self.session_handle, table_name, database_name)
        self._execute_sync(op)
        results = self.fetchall()
        if len(results) == 0:
            # TODO: the error raised here should be different
            raise OperationalError("no schema results for table %s.%s" % (database_name, table_name))
        # check that results are derived from a unique table
        tables = set()
        for col in results:
            tables.add((col[1], col[2]))
        if len(tables) > 1:
            # TODO: the error raised here should be different
            raise ProgrammingError("db: %s, table: %s is not unique" % (database_name, table_name))
        return [(r[3], hs2_client._PrimitiveType_to_TTypeId[r[5]]) for r in results]

    def get_functions(self, database_name=None):
        if database_name is None:
            database_name = '.*'
        def op():
            self._last_operation_string = "RPC_GET_FUNCTIONS"
            self._last_operation_handle = hs2_client.get_functions(self.service,
                    self.session_handle, database_name)
        self._execute_sync(op)

# Compliance with Type Objects of PEP 249.
class _DBAPITypeObject(object):
    def __init__(self, *values):
        self.values = values
    def __cmp__(self, other):
        if other in self.values:
            return 0
        else:
            return -1

STRING = _DBAPITypeObject(TTypeId._VALUES_TO_NAMES[TTypeId.STRING_TYPE])
BINARY = _DBAPITypeObject(TTypeId._VALUES_TO_NAMES[TTypeId.BINARY_TYPE])
NUMBER = _DBAPITypeObject(TTypeId._VALUES_TO_NAMES[TTypeId.BOOLEAN_TYPE],
                          TTypeId._VALUES_TO_NAMES[TTypeId.TINYINT_TYPE],
                          TTypeId._VALUES_TO_NAMES[TTypeId.SMALLINT_TYPE],
                          TTypeId._VALUES_TO_NAMES[TTypeId.INT_TYPE],
                          TTypeId._VALUES_TO_NAMES[TTypeId.BIGINT_TYPE],
                          TTypeId._VALUES_TO_NAMES[TTypeId.FLOAT_TYPE],
                          TTypeId._VALUES_TO_NAMES[TTypeId.DOUBLE_TYPE],
                          TTypeId._VALUES_TO_NAMES[TTypeId.DECIMAL_TYPE])
DATETIME = _DBAPITypeObject(TTypeId._VALUES_TO_NAMES[TTypeId.TIMESTAMP_TYPE])
ROWID = _DBAPITypeObject()

Date = datetime.date
Time = datetime.time
Timestamp = datetime.datetime

def DateFromTicks(ticks):
    return Date(*time.localtime(ticks)[:3])

def TimeFromTicks(ticks):
    return Time(*time.localtime(ticks)[3:6])

def TimestampFromTicks(ticks):
    return Timestamp(*time.localtime(ticks)[:6])

Binary = buffer

def _bind_parameters(operation, parameters):
    # inspired by MySQL Python Connector (conversion.py)
    string_parameters = {}
    for (name, value) in parameters.iteritems():
        if value is None:
            string_parameters[name] = 'NULL'
        elif isinstance(value, basestring):
            string_parameters[name] = "'" + _escape(value) + "'"
        else:
            string_parameters[name] = str(value)
    return operation % string_parameters

def _escape(s):
    e = s
    e = e.replace('\\', '\\\\')
    e = e.replace('\n', '\\n')
    e = e.replace('\r', '\\r')
    e = e.replace("'", "\\'")
    e = e.replace('"', '\\"')
    return e
