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

from six import reraise

from impala.util import _escape
from impala.error import (Error, Warning, InterfaceError, DatabaseError,
                          InternalError, OperationalError, ProgrammingError,
                          IntegrityError, DataError, NotSupportedError)


class Connection(object):
    # PEP 249
    # Connection objects are associated with a TCLIService.Client thrift
    # service
    # it's instantiated with an alive TCLIService.Client

    def close(self):
        # PEP 249
        raise NotImplementedError

    def commit(self):
        # PEP 249
        raise NotImplementedError

    def rollback(self):
        # PEP 249
        raise NotImplementedError

    def cursor(self, session_handle=None, user=None, configuration=None):
        # PEP 249
        raise NotImplementedError

    def reconnect(self):
        raise NotImplementedError

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        if exc_type is not None:
            reraise(exc_type, exc_val, exc_tb)

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


class Cursor(object):
    """Abstract representation of Cursor"""

    def description(self):
        raise NotImplementedError

    def rowcount(self):
        raise NotImplementedError

    def query_string(self):
        raise NotImplementedError

    def get_arraysize(self):
        raise NotImplementedError

    def set_arraysize(self, arraysize):
        raise NotImplementedError

    def buffersize(self):
        raise NotImplementedError

    def has_result_set(self):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError

    def close_operation(self):
        raise NotImplementedError

    def execute(self, operation, parameters=None, configuration=None):
        raise NotImplementedError

    def _execute_sync(self, operation_fn):
        raise NotImplementedError

    def _reset_state(self):
        raise NotImplementedError

    def _wait_to_finish(self):
        raise NotImplementedError

    def executemany(self, operation, seq_of_parameters):
        raise NotImplementedError

    def fetchone(self):
        raise NotImplementedError

    def fetchmany(self, size=None):
        raise NotImplementedError

    def fetchall(self):
        raise NotImplementedError

    def setinputsizes(self, sizes):
        raise NotImplementedError

    def setoutputsize(self, size, column=None):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    def next(self):
        raise NotImplementedError

    def ping(self):
        raise NotImplementedError

    def get_log(self):
        raise NotImplementedError

    def get_profile(self):
        raise NotImplementedError

    def get_summary(self):
        raise NotImplementedError

    def build_summary_table(self, summary, idx, is_fragment_root, indent_level,
                            output):
        raise NotImplementedError

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        if exc_type is not None:
            reraise(exc_type, exc_val, exc_tb)


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
