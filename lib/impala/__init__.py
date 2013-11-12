import sys
import getpass
import logging
import operator
import itertools

from thrift.transport.TSocket import TSocket
from thrift.transport.TTransport import TBufferedTransport
from thrift.protocol.TBinaryProtocol import TBinaryProtocol

from cli_service import TCLIService
from cli_service.ttypes import (TStatusCode, TOpenSessionReq, TGetTablesReq,
        TFetchResultsReq, TCloseOperationReq, TCloseSessionReq,
        TGetOperationStatusReq, TExecuteStatementReq, TGetSchemasReq,
        TGetInfoReq, TGetInfoType, TTypeId, TFetchOrientation,
        TGetResultSetMetadataReq)

import impala.error

# This work builds off of:
# 1. the Hue interface: 
#       hue/apps/beeswax/src/beeswax/server/dbms.py
#       hue/apps/beeswax/src/beeswax/server/hive_server2_lib.py
#       hue/desktop/core/src/desktop/lib/thrift_util.py
# 2. the Impala shell:
#       Impala/shell/impala_shell.py
# 3. PyMongo interface
# 4. PEP 249: http://www.python.org/dev/peps/pep-0249/

LOG = logging.getLogger(__name__)

def err_if_not_success(status, msg="Status returned unsuccessful."):
    if (status.statusCode != TStatusCode._NAMES_TO_VALUES['SUCCESS_STATUS'] and
            status.statusCode != TStatusCode._NAMES_TO_VALUES['SUCCESS_WITH_INFO_STATUS']):
        raise impala.error.OperationalError(msg)


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
    return Connection(sock, transport, protocol, service, user)


class Connection(object):
    
    def __init__(self, sock, transport, protocol, service, user):
        self.user = user
        self.sock = sock
        self.transport = transport
        self.protocol = protocol
        self.service = service
        self.server_protocol_version = None
        self.configuration = None
        self.session_handle = None
        self._open_session()
    
    def close(self):
        """Close the session and the Thrift transport."""
        self.__del__()
    
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
            err_if_not_success(resp.status, "Not connected; GetInfo returned unsuccessful status.")
        except ImpalaException as e:
            return False
        return True
    
    def cursor(self):
        # TODO
        return Cursor(self.service, self.session_handle)
    
    def _open_session(self):
        # open a session with the Impala service
        req = TOpenSessionReq(username=self.user)
        try:
            resp = self.service.OpenSession(req)
            err_if_not_success(resp.status, "OpenSession: failed to open a "
                    "session to Impala. Are you connected to the service?")
        except impala.error.OperationalError as e:
            self.close()
        
        self.server_protocol_version = resp.serverProtocolVersion
        self.configuration = resp.configuration
        self.session_handle = resp.sessionHandle
        LOG.info("Opened a session")
    
    def _close_session(self):
        req = TCloseSessionReq(sessionHandle=self.session_handle)
        resp = self.service.CloseSession(req)
        err_if_not_success(resp.status, "CloseSession: failed to close session.")
    
    def __del__(self):
        if self.service is not None:
            self._close_session()
        if self.transport is not None:
            self.transport.close()


class Cursor(object):
    
    def __init__(self, service, session_handle):
        self.service = service
        self.session_handle = session_handle
        self._last_op_handle = None
        self.arraysize = 100
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
    
    @property
    def has_result_set(self):
        return self._last_op_handle is not None and self._last_op_handle.hasResultSet
    
    def close(self):
        self.__del__()
    
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
    
    def __del__(self):
        # TODO: currently, doesn't need to do anything, since all resources are
        # controlled by the Connection.  However, to agree with PEP 249, I
        # should check if the user has called .close(), and make sure no
        # operations are allowed.
        pass
    
    def _execute_statement_async(self, statement, configuration={}):
        req = TExecuteStatementReq(sessionHandle=self.session_handle, statement=statement, confOverlay=configuration)
        resp = self.service.ExecuteStatement(req)
        err_if_not_success(resp.status, "Failed to execute statement: %s" % statement)
        return resp.operationHandle
    
    def _fetch_schema(self):
        # this assumes that self._last_op_handle.hasResultSet == True
        req = TGetResultSetMetadataReq(operationHandle=self._last_op_handle)
        resp = self.service.GetResultSetMetadata(req)
        err_if_not_success(resp.status, "Failed to get query metadata.")
        
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
        err_if_not_success(resp.status, "Fetch failed.")
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
