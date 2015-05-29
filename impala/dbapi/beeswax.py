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

import getpass
import time
import sys
import six
import os

from impala.dbapi.interface import Connection, Cursor, _bind_parameters
from impala._rpc import beeswax as rpc
from impala.error import NotSupportedError, ProgrammingError, OperationalError
if six.PY2:
    from impala._thrift_gen.beeswax.BeeswaxService import QueryState
elif six.PY3:
    # dynamically load the thrift modules
    from thriftpy import load
    thrift_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                              'thrift')
    beeswax = load(os.path.join(thrift_dir, 'beeswax.thrift'),
                   include_dirs=[thrift_dir])
    sys.modules[beeswax.__name__] = beeswax
    from beeswax import QueryState


class BeeswaxConnection(Connection):
    # PEP 249

    def __init__(self, service, default_db=None):
        self.service = service
        self.default_db = default_db
        self.default_query_options = {}

    def close(self):
        """Close the session and the Thrift transport."""
        # PEP 249
        rpc.close_service(self.service)

    def commit(self):
        """Impala doesn't support transactions; does nothing."""
        # PEP 249
        pass

    def rollback(self):
        """Impala doesn't support transactions; raises NotSupportedError"""
        # PEP 249
        raise NotSupportedError

    def cursor(self, user=None, configuration=None):
        # PEP 249
        if user is None:
            user = getpass.getuser()
        options = rpc.build_default_query_options_dict(self.service)
        for opt in options:
            self.default_query_options[opt.key.upper()] = opt.value
        cursor = BeeswaxCursor(self.service, user)
        if self.default_db is not None:
            cursor.execute('USE %s' % self.default_db)
        return cursor

    def reconnect(self):
        rpc.reconnect(self.service)


class BeeswaxCursor(Cursor):
    # PEP 249
    # Beeswax does not support sessions

    def __init__(self, service, user):
        self.service = service
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
        # rows into a buffer if arraysize hasn't been set.  (otherwise, we'd
        # get an unbuffered impl because the PEP 249 default value of arraysize
        # is 1)
        return self._buffersize if self._buffersize else 1024

    @property
    def has_result_set(self):
        return (self._last_operation_handle is not None and
                rpc.expect_result_metadata(self._last_operation_string))

    def close(self):
        # PEP 249
        pass

    def cancel_operation(self):
        if self._last_operation_active:
            self._last_operation_active = False
            rpc.cancel_query(self.service, self._last_operation_handle)

    def close_operation(self):
        if self._last_operation_active:
            self._last_operation_active = False
            rpc.close_query(self.service, self._last_operation_handle)

    def execute(self, operation, parameters=None, configuration=None):
        # PEP 249
        if configuration is None:
            configuration = {}

        def op():
            if parameters:
                self._last_operation_string = _bind_parameters(operation,
                                                               parameters)
            else:
                self._last_operation_string = operation
            query = rpc.create_beeswax_query(self._last_operation_string,
                                             self.user, configuration)
            self._last_operation_handle = rpc.execute_statement(self.service,
                                                                query)

        self._execute_sync(op)

    def _execute_sync(self, operation_fn):
        # operation_fn should set self._last_operation_string and
        # self._last_operation_handle
        self._reset_state()
        operation_fn()
        self._last_operation_active = True
        self._wait_to_finish()  # make execute synchronous
        if self.has_result_set:
            schema = rpc.get_results_metadata(
                self.service, self._last_operation_handle)
            self._description = [tuple([tup.name, tup.type.upper()] +
                                 [None, None, None, None, None])
                                 for tup in schema]
        else:
            self._last_operation_active = False
            rpc.close_query(self.service, self._last_operation_handle)

    def _reset_state(self):
        self._buffer = []
        self._rowcount = -1
        self._description = None
        if self._last_operation_active:
            self._last_operation_active = False
            rpc.close_query(self.service, self._last_operation_handle)
        self._last_operation_string = None
        self._last_operation_handle = None

    def _wait_to_finish(self):
        loop_start = time.time()
        while True:
            operation_state = rpc.get_query_state(
                self.service, self._last_operation_handle)
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

    def executemany(self, operation, seq_of_parameters):
        # PEP 249
        for parameters in seq_of_parameters:
            self.execute(operation, parameters)
            if self.has_result_set:
                raise ProgrammingError("Operations that have result sets are "
                                       "not allowed with executemany.")

    def fetchone(self):
        # PEP 249
        if not self.has_result_set:
            raise ProgrammingError("Tried to fetch but no results.")
        try:
            return next(self)
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
                local_buffer.append(next(self))
                i += 1
            except StopIteration:
                break
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

    def __next__(self):
        if not self.has_result_set:
            raise ProgrammingError(
                "Trying to fetch results on an operation with no results.")
        if len(self._buffer) > 0:
            return self._buffer.pop(0)
        elif self._last_operation_active:
            # self._buffer is empty here and op is active: try to pull
            # more rows
            rows = rpc.fetch_internal(self.service,
                                      self._last_operation_handle,
                                      self.buffersize)
            self._buffer.extend(rows)
            if len(self._buffer) == 0:
                self._last_operation_active = False
                rpc.close_query(self.service, self._last_operation_handle)
                raise StopIteration
            return self._buffer.pop(0)
        else:
            # empty buffer and op is now closed: raise StopIteration
            raise StopIteration

    def ping(self):
        """Checks connection to server by requesting some info
        from the server.
        """
        return rpc.ping(self.service)

    def get_log(self):
        return rpc.get_warning_log(self.service, self._last_operation_handle)

    def get_profile(self):
        return rpc.get_runtime_profile(
            self.service, self._last_operation_handle)

    def get_summary(self):
        return rpc.get_summary(self.service, self._last_operation_handle)

    def build_summary_table(self, summary, output, idx=0,
                            is_fragment_root=False, indent_level=0):
        return rpc.build_summary_table(
            summary, idx, is_fragment_root, indent_level, output)
