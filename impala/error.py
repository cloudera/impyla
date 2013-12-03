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

"""Impala exception classes.  Also implements PEP 249."""

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

class RPCError(Error):
    pass

def err_if_rpc_not_ok(resp):
    if (resp.status.statusCode != TStatusCode._NAMES_TO_VALUES['SUCCESS_STATUS'] and
            resp.status.statusCode != TStatusCode._NAMES_TO_VALUES['SUCCESS_WITH_INFO_STATUS']):
        raise RPCError("RPC failed: %s" % resp.__class__.__name__)