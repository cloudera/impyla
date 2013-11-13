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

import sys
import getpass
import logging
import operator
import itertools

from thrift.transport.TSocket import TSocket
from thrift.transport.TTransport import TBufferedTransport
from thrift.protocol.TBinaryProtocol import TBinaryProtocol

from impala.cli_service import TCLIService
from impala.cli_service.ttypes import (TOpenSessionReq, TFetchResultsReq,
        TCloseSessionReq, TExecuteStatementReq, TGetInfoReq, TGetInfoType,
        TTypeId, TFetchOrientation, TGetResultSetMetadataReq)

import impala.error
from impala.error import err_if_rpc_not_ok

# This work builds off of:
# 1. the Hue interface: 
#       hue/apps/beeswax/src/beeswax/server/dbms.py
#       hue/apps/beeswax/src/beeswax/server/hive_server2_lib.py
#       hue/desktop/core/src/desktop/lib/thrift_util.py
# 2. the Impala shell:
#       Impala/shell/impala_shell.py
# 3. PyMongo interface
# 4. PEP 249: http://www.python.org/dev/peps/pep-0249/


# PEP 249 module globals
apilevel = '2.0'
threadsafety = 0 # Threads may not share the module.
paramstyle = 'pyformat'


def connect(host='localhost', port=21050, user=getpass.getuser(), timeout=45):
    sock = TSocket(host, port)
    sock.setTimeout(timeout * 1000.)
    transport = TBufferedTransport(sock)
    transport.open()
    protocol = TBinaryProtocol(transport)
    service = TCLIService.Client(protocol)
    return Connection(service)


class Connection(object):
    # Connection objects are associated with a TCLIService.Client thrift service
    # it's instantiated with an alive TCLIService.Client
    
    def __init__(self, service):
        self.service = service
    
    def close(self):
        """Close the session and the Thrift transport."""
        self.service._iprot.trans.close()
    
    def commit(self):
        """Impala doesn't support transactions; does nothing."""
        pass
    
    def rollback(self):
        """Impala doesn't support transactions; raises NotSupportedError"""
        raise impala.error.NotSupportedError()
    
    def ping(self):
        """Checks connection to server by requesting some info from the server."""
        req = TGetInfoReq(self.session_handle, TGetInfoType.CLI_SERVER_NAME)
        try:
            resp = self.service.GetInfo(req)
        except TTransportException as e:
            return False
        try:
            err_if_rpc_not_ok(resp.status)
        except ImpalaException as e:
            return False
        return True
    
    def cursor(self, session_handle=None, user=None):
        if user is None:
            user = getpass.getuser()
        if session_handle is None:
            session_handle = self._open_session(user)
        return Cursor(self.service, session_handle)
    
    def _open_session(self, user):
        # open a session with the Impala service
        req = TOpenSessionReq(username=user)
        try:
            resp = self.service.OpenSession(req)
            err_if_rpc_not_ok(resp.status)
        except impala.error.OperationalError as e:
            self.close()
        return resp.sessionHandle


class Cursor(object):
    # Cursor objects are associated with a Session
    # they are instantiated with alive session_handles
    
    def __init__(self, service, session_handle):
        self.service = service
        self.session_handle = session_handle
        
        self._last_op_handle = None
        self._arraysize = 100
        self._buffer = []
        self._orientation=TFetchOrientation.FETCH_NEXT
        
        # initial values, per PEP 249
        self._description = None
        self._rowcount = -1
    
    @property
    def description(self):
        return self._description
    
    @property
    def rowcount(self):
        return self._rowcount
    
    def set_arraysize(self, arraysize):
        self._arraysize = arraysize
    arraysize = property(lambda self: self._arraysize, set_arraysize)
    
    @property
    def has_result_set(self):
        return self._last_op_handle is not None and self._last_op_handle.hasResultSet
    
    def close(self):
        req = TCloseSessionReq(sessionHandle=self.session_handle)
        resp = self.service.CloseSession(req)
        err_if_rpc_not_ok(resp.status)
    
    def execute(self, operation, parameters={}):
        self._buffer = []
        self._description = None
        self._last_op_handle = self._execute_statement_async(operation % parameters)
        if self.has_result_set:
            self._fetch_schema()
    
    def executemany(self, operation, seq_of_parameters=[]):
        for parameters in seq_of_parameters:
            self.execute(operation, parameters)
            if self.has_result_set:
                raise impala.error.ProgrammingError("Operations that have result sets are not allowed with executemany.")
        
    def fetchone(self):
        if not self.has_result_set:
            raise impala.error.ProgrammingError("Tried to fetch but no results.")
        try:
            return self.next()
        except StopIteration:
            return None
    
    def fetchmany(self, size=None):
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
        return list(self)
    
    def setinputsizes(self, sizes):
        pass
    
    def setoutputsize(self, size, column=None):
        pass
    
    def __iter__(self):
        return self
    
    def next(self):
        if len(self._buffer) > 0:
            return self._buffer.pop(0)
        else:
            self._fetch_results()
            if len(self._buffer) == 0:
                raise StopIteration
            return self._buffer.pop(0)
    
    def _execute_statement_async(self, statement, configuration={}):
        req = TExecuteStatementReq(sessionHandle=self.session_handle, statement=statement, confOverlay=configuration)
        resp = self.service.ExecuteStatement(req)
        err_if_rpc_not_ok(resp.status)
        return resp.operationHandle
    
    def _fetch_schema(self):
        # this assumes that self._last_op_handle.hasResultSet == True
        req = TGetResultSetMetadataReq(operationHandle=self._last_op_handle)
        resp = self.service.GetResultSetMetadata(req)
        err_if_rpc_not_ok(resp.status)
        
        self._description = []
        for column in resp.schema.columns:
            name = column.columnName
            type_ = TTypeId._VALUES_TO_NAMES[column.typeDesc.types[0].primitiveEntry.type]
            # per PEP 249:
            self._description.append((name, type_, None, None, None, None, None))

    def _fetch_results(self):
        # this function is primarily for internal use
        # fills the buffer with up to self.arraysize rows
        # may fill it with zero rows if there are no more results
        if not self.has_result_set:
            raise impala.error.ProgrammingError("Trying to fetch results on an operation with no results.")
        req = TFetchResultsReq(operationHandle=self._last_op_handle, orientation=self._orientation, maxRows=self.arraysize)
        resp = self.service.FetchResults(req)
        err_if_rpc_not_ok(resp.status)
        for trow in resp.results.rows:
            row = []
            for (i, col_val) in enumerate(trow.colVals):
                row.append(_primitive_type_getters[self.description[i][1]](col_val).value)
            self._buffer.append(tuple(row))

# mapping between Thrift TTypeId (in schema) and TColumnValue (in returned rows)
# helper object for converting from TRow to something friendlier
_primitive_type_getters = {
        'BOOLEAN_TYPE': operator.attrgetter('boolVal'),
        'TINYINT_TYPE': operator.attrgetter('byteVal'),
        'SMALLINT_TYPE': operator.attrgetter('i16Val'),
        'INT_TYPE': operator.attrgetter('i32Val'),
        'BIGINT_TYPE': operator.attrgetter('i64Val'),
        'TIMESTAMP_TYPE': operator.attrgetter('i64Val'),
        'FLOAT_TYPE': operator.attrgetter('doubleVal'),
        'DOUBLE_TYPE': operator.attrgetter('doubleVal'),
        'STRING_TYPE': operator.attrgetter('stringVal')
}

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
