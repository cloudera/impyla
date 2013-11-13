"""Impala exception classes.  Implements PEP 249."""

import exceptions

from impala.cli_service.ttypes import TStatusCode

class Error(exceptions.StandardError):
    pass

class Warning(exceptions.StandardError):
    pass

class InterfaceError(Error):
    pass

class DatabaseError(Error):
    pass

class InternalError(DatabaseError):
    pass

class OperationalError(DatabaseError):
    pass

class ProgrammingError(DatabaseError):
    pass

class IntegrityError(DatabaseError):
    pass

class DataError(DatabaseError):
    pass

class NotSupportedError(DatabaseError):
    pass

def err_if_rpc_not_ok(resp):
    if (resp.status.statusCode != TStatusCode._NAMES_TO_VALUES['SUCCESS_STATUS'] and
            resp.status.statusCode != TStatusCode._NAMES_TO_VALUES['SUCCESS_WITH_INFO_STATUS']):
        raise OperationalError("RPC failed: %s" % resp.__class__.__name__)