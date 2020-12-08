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

from __future__ import absolute_import


class Error(Exception):
    pass


class Warning(Exception):
    pass


# DB API (PEP 249) exceptions

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


# RPC errors

class RPCError(Error):
    pass


class HiveServer2Error(RPCError):
    pass

class HttpError(RPCError):
    """An error containing an http response code"""
    def __init__(self, code, message, body, http_headers):
        self.code = code
        self.message = message
        self.body = body
        self.http_headers = http_headers

    def __str__(self):
        # Don't try to print the body as we don't know what format it is.
        return "HTTP code {}: {}".format(self.code, self.message)


class BeeswaxError(RPCError):
    pass


class QueryStateError(BeeswaxError):
    pass


class DisconnectedError(BeeswaxError):
    pass
