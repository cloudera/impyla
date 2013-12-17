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

"""Implements the Python DB API 2.0 for Impala (PEP 249)"""

import getpass
from time import sleep

from impala.cli_service.ttypes import TTypeId

import impala.error
import impala.rpc


# PEP 249 module globals
apilevel = '2.0'
threadsafety = 0 # Threads may not share the module.
paramstyle = 'pyformat'


def connect(host='localhost', port=21050, timeout=45):
    # PEP 249
    service = impala.rpc.connect_to_impala(host, port, timeout)
    return Connection(service)


class Connection(object):
    # PEP 249
    # Connection objects are associated with a TCLIService.Client thrift service
    # it's instantiated with an alive TCLIService.Client
    
    def __init__(self, service):
        self.service = service
    
    def close(self):
        """Close the session and the Thrift transport."""
        # PEP 249
        impala.rpc.close_service(self.service)
    
    def commit(self):
        """Impala doesn't support transactions; does nothing."""
        # PEP 249
        pass
    
    def rollback(self):
        """Impala doesn't support transactions; raises NotSupportedError"""
        # PEP 249
        raise impala.error.NotSupportedError()
    
    def cursor(self, session_handle=None, user=None):
        # PEP 249
        if user is None:
            user = getpass.getuser()
        if session_handle is None:
            session_handle = impala.rpc.open_session(self.service, user)
        return Cursor(self.service, session_handle)


class Cursor(object):
    # PEP 249
    # Cursor objects are associated with a Session
    # they are instantiated with alive session_handles
    
    def __init__(self, service, session_handle):
        self.service = service
        self.session_handle = session_handle
        
        self._last_operation_string = None
        self._last_operation_handle = None
        self._arraysize = 100
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
    
    def set_arraysize(self, arraysize):
        # PEP 249
        self._arraysize = arraysize
    arraysize = property(lambda self: self._arraysize, set_arraysize)
    
    @property
    def has_result_set(self):
        return (self._last_operation_handle is not None and 
                self._last_operation_handle.hasResultSet)
    
    def close(self):
        # PEP 249
        impala.rpc.close_session(self.service, self.session_handle)
    
    def execute(self, operation, parameters={}):
        # PEP 249
        self._buffer = []
        self._description = None
        self._last_operation_string = operation % parameters
        self._last_operation_handle = impala.rpc.execute_statement(
                self.service, self.session_handle, self._last_operation_string)
        # make execute synchronous: check whether operation finished
        while True:
            operation_state = impala.rpc.get_operation_status(self.service,
                    self._last_operation_handle)
            if operation_state not in ['INITIALIZED_STATE', 'RUNNING_STATE']:
                break
            sleep(0.1)
        if self.has_result_set:
            schema = impala.rpc.get_result_schema(self.service,
                    self._last_operation_handle)
            self._description = [tup + (None, None, None, None, None) for tup in schema]
    
    def executemany(self, operation, seq_of_parameters=[]):
        # PEP 249
        for parameters in seq_of_parameters:
            self.execute(operation, parameters)
            if self.has_result_set:
                raise impala.error.ProgrammingError("Operations that have result sets are not allowed with executemany.")
        
    def fetchone(self):
        # PEP 249
        if not self.has_result_set:
            raise impala.error.ProgrammingError("Tried to fetch but no results.")
        try:
            return self.next()
        except StopIteration:
            return None
    
    def fetchmany(self, size=None):
        # PEP 249
        if not self.has_result_set:
            raise impala.error.ProgrammingError("Tried to fetch but no results.")
        if size is None:
            size = self.arraysize
        local_buffer = []
        for (i, row) in enumerate(self):
            if i >= size:
                break
            local_buffer.append(row)
        return local_buffer
    
    def fetchall(self):
        # PEP 249
        return list(self)
    
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
            raise impala.error.ProgrammingError("Trying to fetch results on an operation with no results.")
        if len(self._buffer) > 0:
            return self._buffer.pop(0)
        else:
            rows = impala.rpc.fetch_results(self.service,
                    self._last_operation_handle, self.description,
                    self.arraysize)
            self._buffer.extend(rows)
            if len(self._buffer) == 0:
                raise StopIteration
            return self._buffer.pop(0)
    
    def ping(self):
        """Checks connection to server by requesting some info from the server."""
        return impala.rpc.ping(self.service, self.session_handle)
    
    def table_exists(self, table_name, database_name=None):
        if database_name is None:
            database_name = '.*'
        return impala.rpc.table_exists(self.service, self.session_handle,
                    table_name, database_name)
    
    def get_table_schema(self, table_name, database_name=None):
        if database_name is None:
            database_name = '.*'
        return impala.rpc.get_table_schema(self.service, self.session_handle,
                table_name, database_name)


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
                         TTypeId._VALUES_TO_NAMES[TTypeId.DOUBLE_TYPE],)
DATETIME = _DBAPITypeObject(TTypeId._VALUES_TO_NAMES[TTypeId.TIMESTAMP_TYPE])
ROWID = _DBAPITypeObject()
