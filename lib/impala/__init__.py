import sys
import getpass
import logging
import operator
import itertools

from thrift.transport.TSocket import TSocket
from thrift.transport.TTransport import TBufferedTransport
from thrift.protocol.TBinaryProtocol import TBinaryProtocol

from cli_service.ttypes import (TStatusCode, TOpenSessionReq, TGetTablesReq,
        TFetchResultsReq, TCloseOperationReq, TCloseSessionReq,
        TGetOperationStatusReq, TExecuteStatementReq, TGetSchemasReq,
        TGetInfoReq, TGetInfoType)

from ImpalaService import ImpalaHiveServer2Service



# This work builds off of:
# 1. the Hue interface: 
#       hue/apps/beeswax/src/beeswax/server/dbms.py
#       hue/apps/beeswax/src/beeswax/server/hive_server2_lib.py
#       hue/desktop/core/src/desktop/lib/thrift_util.py
# 2. the Impala shell:
#       Impala/shell/impala_shell.py
# 3. PyMongo interface
# 4. PEP 249: http://www.python.org/dev/peps/pep-0249/



apilevel = '2.0'
threadsafety = 0 # Threads may not share the module.
paramstyle = 'pyformat'



def connect(*args, **kw):
    sock = TSocket(self.host, self.port)
    
    
    
    
    
    
    c = Connection(*args, **kw)
    c.connect()
    return c


def _connect_to_TCLIService(self):
        # if this isn't my first time connecting, make sure I closed the
        # previous transport
        if self.transport is not None:
            self.transport.close()
            self.transport = None
        
        try:
            # get client to HiveServer2 service
            sock = TSocket(self.host, self.port)
            sock.setTimeout(self.timeout * 1000.)
            self.transport = TBufferedTransport(sock)
            self.transport.open()
            protocol = TBinaryProtocol(self.transport)
            self.impala_service = TCLIService.Client(protocol)
            LOG.info("Set up a thrift client to the TCLIService")
    
    def _open_session(self):
        # open a session with the Impala service
        req = TOpenSessionReq(username=self.user)
        try:
            resp = self.impala_service.OpenSession(req)
            err_if_not_success(resp.status, "OpenSession: failed to open a "
                    "session to Impala. Are you connected to the service?")
        except ImpalaException, e:
            logging.error(e.message)
            self.transport.close()
            raise
        
        self.server_protocol_version = resp.serverProtocolVersion
        self.configuration = resp.configuration
        self.session_handle = resp.session_handle
        LOG.info("Opened a session")








class Connection(object):
    
    def __init__(self, host='localhost', port=21050, user=getpass.getuser(), timeout=45):
        """Create a connection to an Impala daemon.
        
        port is the Impala Daemon HiveServer2 Port.
        """
        self.host = host
        self.port = port
        self.user = user
        self.timeout = timeout
        
        self.transport = None
        self.impala_service = None
        self.server_protocol_version = None
        self.configuration = None
        self.session_handle = None
    
    def close(self):
        # TODO
        pass
    
    def commit(self):
        pass
    
    def rollback(self):
        pass
    
    def cursor(self):
        # TODO
        pass

class Cursor(object):
    
    def __init__(self):
        self._description = None
        self._rowcount = -1
    
    @property
    def description(self):
        return self._description
    
    @property
    def rowcount(self):
        return self._rowcount
    
    def __iter__(self):
        return self
    
    def next(self):
        # TODO
        pass
    
    





LOG = logging.getLogger(__name__)












# reference the thrift definitions for TTypeId number mapping
type_getters = {
        0: operator.attrgetter('boolVal'),
        1: operator.attrgetter('byteVal'),
        2: operator.attrgetter('i16Val'),
        3: operator.attrgetter('i32Val'),
        4: operator.attrgetter('i64Val'),
        # 5: this is for floatVal, which is not used in TColumnValue
        6: operator.attrgetter('doubleVal'),
        7: operator.attrgetter('stringVal')
}

def TRowSet2DataFrame(row_set, schema):
    # TODO: this should be Cythoned
    # TODO: this should be factored into a separate interface
    # row_set is TRowSet
    # schema is TTableSchema
    
    # compute the sequence of type accesses
    names = [col_schema.columnName for col_schema in schema.columns]
    getters = [type_getters[col_schema.typeDesc.types[0].primitiveEntry.type]
            for col_schema in schema.columns]
    
    rows_list = []
    for thrift_row in row_set.rows:
        row_dict = {}
        for (i, col_val) in enumerate(thrift_row.colVals):
            row_dict[names[i]] = getters[i](col_val).value
        rows_list.append(row_dict)
    
    return pd.DataFrame(rows_list, columns=names)
            
            
            


class ImpalaException(Exception):
    pass

def err_if_not_success(status, msg="Status returned unsuccessful."):
    if (status.statusCode != TStatusCode._NAMES_TO_VALUES['SUCCESS_STATUS'] and
        status.statusCode != TStatusCode._NAMES_TO_VALUES['SUCCESS_WITH_INFO_STATUS']):
    raise ImpalaException(msg)


class ResultSet(object):
    
    def __init__(self, operation_handle, ):
        pass
    
    # internal buffer of rows
    # iterator over rows
    # separate obj to consume ResultSet and produce, say, DataFrame


class ImpalaClient(object):
    """Low-level client to get a Thrift interface to an Impala server.
    
    Uses the Hive Server 2 TCLIService.
    """ 
  
    def __init__(self, host='localhost', port=21050, user=getpass.getuser(), timeout=45):
        """Instantiate a client.
        
        port is the Impala Daemon HiveServer2 Port.
        """
        self.host = host
        self.port = port
        self.user = user
        self.timeout = timeout
        
        self.transport = None
        self.impala_service = None
        self.server_protocol_version = None
        self.configuration = None
        self.session_handle = None
  
    def connect(self):
        """Connect to an Impala server.
        
        Opens a Thrift transport, sets up a TCLIService client, and opens a
        session.
        """
        self._connect_to_TCLIService(timeout)
        self._open_session()
    
    def close(self):
        """Close the session and the Thrift transport."""
        if self.impala_service is not None:
            self._close_session()
        if self.transport is not None:
            self.transport.close()
    
    def ping(self):
        """Checks connection to server by requesting some info from the server."""
        req = TGetInfoReq(self.session_handle, TGetInfoType.CLI_SERVER_NAME)
        try:
            resp = self.impala_service.GetInfo(req)
        except TTransportException as e:
            return False
        try:
            err_if_not_success(resp.status, "Not connected; GetInfo returned unsuccessful status.")
        except ImpalaException as e:
            return False
        return True
    
    def db_names(self):
        # TODO
        pass
    
    def use_db(self, db_name):
        # TODO
        pass
    
    def _connect_to_TCLIService(self):
        # if this isn't my first time connecting, make sure I closed the
        # previous transport
        if self.transport is not None:
            self.transport.close()
            self.transport = None
        
        try:
            # get client to HiveServer2 service
            sock = TSocket(self.host, self.port)
            sock.setTimeout(self.timeout * 1000.)
            self.transport = TBufferedTransport(sock)
            self.transport.open()
            protocol = TBinaryProtocol(self.transport)
            self.impala_service = TCLIService.Client(protocol)
            LOG.info("Set up a thrift client to the TCLIService")
    
    def _open_session(self):
        # open a session with the Impala service
        req = TOpenSessionReq(username=self.user)
        try:
            resp = self.impala_service.OpenSession(req)
            err_if_not_success(resp.status, "OpenSession: failed to open a "
                    "session to Impala. Are you connected to the service?")
        except ImpalaException, e:
            logging.error(e.message)
            self.transport.close()
            raise
        
        self.server_protocol_version = resp.serverProtocolVersion
        self.configuration = resp.configuration
        self.session_handle = resp.session_handle
        LOG.info("Opened a session")
    
    def _close_session(self):
        req = TCloseSessionReq(session_handle=self.session_handle)
        resp = self.impala_service.CloseSession(req)
        err_if_not_success(resp.status, "CloseSession: failed to close session.")
        self.connected = False
    
    def _fetch_results(self, operation_handle, orientation=TFetchOrientation.FETCH_NEXT, max_rows=1000):
        # this function is primarily for internal use
        # returns (TFetchResultsResp, TGetResultSetMetadataResp)
        if not operation_handle.hasResultSet:
            raise ImpalaException("Trying to fetch results on an operation with no results.")
        fetch_req = TFetchResultsReq(operationHandle=operation_handle, orientation=orientation, maxRows=max_rows)
        results = self.impala_service.FetchResults(fetch_req)
        meta_req = TGetResultSetMetadataReq(operationHandle=operation_handle)
        schema = self.impala_service.GetResultSetMetadata(meta_req)
        return (results, schema)
    
    def _get_databases(self, max_rows=1000):
        # "schema" and "database" is interchangeable in Hive-speak
        req = TGetSchemasReq(sessionHandle=self.session_handle)
        resp = self.impala_service.GetSchemas(req)
        err_if_not_success(resp.status, "Failed to get a list of dbs.")
        return self._fetch_results(resp.operationHandle, max_rows=max_rows)
    
    def _execute_statement_async(self, statement, configuration={}):
        req = TExecuteStatementReq(statement=statement, confOverlay=configuration)
        resp = self.impala_service.ExecuteStatement(req)
        err_if_not_success(resp.status, "Failed to execute statement: %s" % statement)
        return resp.operationHandle
    
    def _execute_statement(self, statement, configuration={}, max_rows=1000):
        operation_handle = self._execute_statement_async(statement, configuration=configuration)
        return self._fetch_results(operation_handle, max_rows=max_rows)
    
    
 class Database(object):
    
    def __init__(self, client, name):
        self.client = client
        self.name = name
    
    def table_names(self):
        pass
    
    def get_table(self, table_name):
        pass
    
    

