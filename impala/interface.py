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

from __future__ import absolute_import

import datetime
import re
import six
from six import reraise

from impala.util import _escape
from impala.error import (  # pylint: disable=unused-import
    Error, Warning, InterfaceError, DatabaseError, InternalError,
    OperationalError, ProgrammingError, IntegrityError, DataError,
    NotSupportedError)


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

    def cursor(self, user=None, configuration=None, convert_types=True):
        # PEP 249
        raise NotImplementedError

    def reconnect(self):
        raise NotImplementedError

    def kerberized(self):
        # pylint: disable=protected-access
        # returns bool whether underlying service is kerberized or not
        from thrift_sasl import TSaslClientTransport
        if isinstance(self.service._iprot.trans, TSaslClientTransport):
            if self.service._iprot.trans.mechanism == 'GSSAPI':
                return True
        return False

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

    def lastrowid(self):
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

    def __next__(self):
        raise NotImplementedError

    def next(self):
        # for py2 compat
        return self.__next__()

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


def _replace_numeric_markers(operation, string_parameters, paramstyle):
    """
    Replaces qname, format, and numeric markers in the given operation, from
    the string_parameters list.

    Raises ProgrammingError on wrong number of parameters or bindings
    when using qmark. There is no error checking on numeric parameters.
    """
    def replace_markers(marker, op, parameters):
        param_count = len(parameters)
        marker_index = 0
        start_offset = 0
        while True:
            found_offset = op.find(marker, start_offset)
            if not found_offset > -1:
                break
            if marker_index < param_count:
                op = op[:found_offset]+op[found_offset:].replace(marker, parameters[marker_index], 1)
                start_offset = found_offset + len(parameters[marker_index])
                marker_index += 1
            else:
                raise ProgrammingError("Incorrect number of bindings "
                                       "supplied. The current statement uses "
                                       "%d or more, and there are %d "
                                       "supplied." % (marker_index + 1,
                                                      param_count))
        if marker_index != 0 and marker_index != param_count:
            raise ProgrammingError("Incorrect number of bindings "
                                   "supplied. The current statement uses "
                                   "%d or more, and there are %d supplied." %
                                   (marker_index + 1, param_count))
        return op

    # replace qmark parameters and format parameters
    # If paramstyle is explicitly specified don't try to substitue them all
    if paramstyle == 'qmark' or paramstyle is None:
        operation = replace_markers('?', operation, string_parameters)
    if paramstyle == 'format' or paramstyle is None:
        operation = replace_markers(r'%s', operation, string_parameters)

    # replace numbered parameters
    if paramstyle == 'numeric' or paramstyle is None:
        operation = re.sub(r'(:)(\d+)', r'{\2}', operation)
        # offset by one
        operation = operation.format(*[''] + string_parameters)

    if paramstyle in ['named', 'pyformat']:
        raise ProgrammingError(
            "paramstyle '%s' is not compatible with parameters passed as List."
            "please use a dict for you parameters instead or specify"
            " a different paramstyle",
            paramstyle
        )

    return operation


def _bind_parameters_list(operation, parameters, paramstyle):
    string_parameters = []
    for value in parameters:
        if value is None:
            string_parameters.append('NULL')
        elif isinstance(value, six.string_types):
            string_parameters.append("'" + _escape(value) + "'")
        else:
            string_parameters.append(str(value))

    # replace qmark and numeric parameters
    return _replace_numeric_markers(operation, string_parameters, paramstyle)


def _bind_parameters_dict(operation, parameters):
    string_parameters = {}
    for (name, value) in six.iteritems(parameters):
        if value is None:
            string_parameters[name] = 'NULL'
        elif isinstance(value, six.string_types):
            string_parameters[name] = "'" + _escape(value) + "'"
        elif isinstance(value, datetime.date):
            string_parameters[name] = "'{0}'".format(value)
        else:
            string_parameters[name] = str(value)

    # replace named parameters by their pyformat equivalents
    operation = re.sub(":([^\d\W]\w*)", "%(\g<1>)s", operation)

    # replace pyformat parameters
    return operation % string_parameters


def _bind_parameters(operation, parameters, paramstyle=None):
    # If parameters is a list, assume either qmark, format, or numeric
    # format. If not, assume either named or pyformat parameters
    if isinstance(parameters, (list, tuple)):
        return _bind_parameters_list(operation, parameters, paramstyle)
    elif isinstance(parameters, dict):
        return _bind_parameters_dict(operation, parameters)
    else:
        raise ProgrammingError("Query parameters argument should be a "
                               "list, tuple, or dict object")
