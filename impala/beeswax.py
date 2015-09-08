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

from __future__ import absolute_import, print_function

import getpass
import time
import six

from impala.interface import Connection, Cursor, _bind_parameters
from impala.error import NotSupportedError, ProgrammingError, OperationalError
from impala._thrift_api.beeswax import QueryState

from six.moves import map
from six.moves import range

from impala.error import RPCError, QueryStateError, DisconnectedError
from impala._thrift_api import (
    get_socket, get_transport, TTransportException, TBinaryProtocol)
from impala._thrift_api.beeswax import (
    TApplicationException, BeeswaxService, ImpalaService, TStatus, TStatusCode,
    TExecStats, ThriftClient)


class BeeswaxConnection(Connection):
    # PEP 249

    def __init__(self, service, default_db=None):
        self.service = service
        self.default_db = default_db
        self.default_query_options = {}

    def close(self):
        """Close the session and the Thrift transport."""
        # PEP 249
        close_service(self.service)

    def commit(self):
        """Impala doesn't support transactions; does nothing."""
        # PEP 249
        pass

    def rollback(self):
        """Impala doesn't support transactions; raises NotSupportedError"""
        # PEP 249
        raise NotSupportedError

    def cursor(self, session_handle=None, user=None, configuration=None):
        # PEP 249
        if user is None:
            user = getpass.getuser()
        options = build_default_query_options_dict(self.service)
        for opt in options:
            self.default_query_options[opt.key.upper()] = opt.value
        cursor = BeeswaxCursor(self.service, user)
        if self.default_db is not None:
            cursor.execute('USE %s' % self.default_db)
        return cursor

    def reconnect(self):
        reconnect(self.service)


class BeeswaxCursor(Cursor):
    # PEP 249
    # Beeswax does not support sessions

    def __init__(self, service, user):
        # pylint: disable=protected-access
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
                expect_result_metadata(self._last_operation_string))

    def close(self):
        # PEP 249
        pass

    def cancel_operation(self):
        if self._last_operation_active:
            self._last_operation_active = False
            cancel_query(self.service, self._last_operation_handle)

    def close_operation(self):
        if self._last_operation_active:
            self._last_operation_active = False
            close_query(self.service, self._last_operation_handle)

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
            query = create_beeswax_query(self._last_operation_string,
                                         self.user, configuration)
            self._last_operation_handle = execute_statement(self.service,
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
            schema = get_results_metadata(
                self.service, self._last_operation_handle)
            self._description = [tuple([tup.name, tup.type.upper()] +
                                 [None, None, None, None, None])
                                 for tup in schema]
        else:
            self._last_operation_active = False
            close_query(self.service, self._last_operation_handle)

    def _reset_state(self):
        self._buffer = []
        self._rowcount = -1
        self._description = None
        if self._last_operation_active:
            self._last_operation_active = False
            close_query(self.service, self._last_operation_handle)
        self._last_operation_string = None
        self._last_operation_handle = None

    def _wait_to_finish(self):
        loop_start = time.time()
        while True:
            operation_state = get_query_state(
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
            rows = fetch_internal(self.service, self._last_operation_handle,
                                  self.buffersize)
            self._buffer.extend(rows)
            if len(self._buffer) == 0:
                self._last_operation_active = False
                close_query(self.service, self._last_operation_handle)
                raise StopIteration
            return self._buffer.pop(0)
        else:
            # empty buffer and op is now closed: raise StopIteration
            raise StopIteration

    def ping(self):
        """Checks connection to server by requesting some info
        from the server.
        """
        return ping(self.service)

    def get_log(self):
        return get_warning_log(self.service, self._last_operation_handle)

    def get_profile(self):
        return get_runtime_profile(
            self.service, self._last_operation_handle)

    def get_summary(self):
        return get_summary(self.service, self._last_operation_handle)

    def build_summary_table(self, summary, output, idx=0,
                            is_fragment_root=False, indent_level=0):
        return build_summary_table(
            summary, idx, is_fragment_root, indent_level, output)


class RpcStatus(object):
    """Convenience enum to describe Rpc return statuses"""
    OK = 0
    ERROR = 1


def __options_to_string_list(set_query_options):
    return ["%s=%s" % (k, v) for (k, v) in six.iteritems(set_query_options)]


def build_default_query_options_dict(service):
    # The default query options are retrieved from a hs2_client call, and are
    # dependent on the impalad to which a connection has been established. They
    # need to be refreshed each time a connection is made. This is particularly
    # helpful when there is a version mismatch between the shell and the
    # impalad.
    try:
        get_default_query_options = service.get_default_configuration(False)
    except:  # pylint: disable=bare-except
        return {}
    rpc_result = __do_rpc(lambda: get_default_query_options)
    options, status = rpc_result
    if status != RpcStatus.OK:
        raise RPCError("Unable to retrieve default query options")
    return options


def build_summary_table(summary, idx, is_fragment_root, indent_level, output):
    """Direct translation of Coordinator::PrintExecSummary() to recursively
    build a list of rows of summary statistics, one per exec node

    summary: the TExecSummary object that contains all the summary data

    idx: the index of the node to print

    is_fragment_root: true if the node to print is the root of a fragment (and
    therefore feeds into an exchange)

    indent_level: the number of spaces to print before writing the node's
    label, to give the appearance of a tree. The 0th child of a node has the
    same indent_level as its parent. All other children have an indent_level of
    one greater than their parent.

    output: the list of rows into which to append the rows produced for this
    node and its children.

    Returns the index of the next exec node in summary.exec_nodes that should
    be processed, used internally to this method only.
    """
    # pylint: disable=too-many-locals

    attrs = ["latency_ns", "cpu_time_ns", "cardinality", "memory_used"]

    # Initialise aggregate and maximum stats
    agg_stats, max_stats = TExecStats(), TExecStats()
    for attr in attrs:
        setattr(agg_stats, attr, 0)
        setattr(max_stats, attr, 0)

    node = summary.nodes[idx]
    for stats in node.exec_stats:
        for attr in attrs:
            val = getattr(stats, attr)
            if val is not None:
                setattr(agg_stats, attr, getattr(agg_stats, attr) + val)
                setattr(max_stats, attr, max(getattr(max_stats, attr), val))

    if len(node.exec_stats) > 0:
        avg_time = agg_stats.latency_ns / len(node.exec_stats)
    else:
        avg_time = 0

    # If the node is a broadcast-receiving exchange node, the cardinality of
    # rows produced is the max over all instances (which should all have
    # received the same number of rows). Otherwise, the cardinality is the sum
    # over all instances which process disjoint partitions.
    if node.is_broadcast and is_fragment_root:
        cardinality = max_stats.cardinality
    else:
        cardinality = agg_stats.cardinality

    est_stats = node.estimated_stats
    label_prefix = ""
    if indent_level > 0:
        label_prefix = "|"
        if is_fragment_root:
            label_prefix += "    " * indent_level
        else:
            label_prefix += "--" * indent_level

    def prettyprint(val, units, divisor):
        for unit in units:
            if val < divisor:
                if unit == units[0]:
                    return "%d%s" % (val, unit)
                else:
                    return "%3.2f%s" % (val, unit)
            val /= divisor

    def prettyprint_bytes(byte_val):
        return prettyprint(
            byte_val, [' B', ' KB', ' MB', ' GB', ' TB'], 1024.0)

    def prettyprint_units(unit_val):
        return prettyprint(unit_val, ["", "K", "M", "B"], 1000.0)

    def prettyprint_time(time_val):
        return prettyprint(time_val, ["ns", "us", "ms", "s"], 1000.0)

    row = [label_prefix + node.label,
           len(node.exec_stats),
           prettyprint_time(avg_time),
           prettyprint_time(max_stats.latency_ns),
           prettyprint_units(cardinality),
           prettyprint_units(est_stats.cardinality),
           prettyprint_bytes(max_stats.memory_used),
           prettyprint_bytes(est_stats.memory_used),
           node.label_detail]

    output.append(row)
    try:
        sender_idx = summary.exch_to_sender_map[idx]
        # This is an exchange node, so the sender is a fragment root, and
        # should be printed next.
        build_summary_table(summary, sender_idx, True, indent_level, output)
    except (KeyError, TypeError):
        # Fall through if idx not in map, or if exch_to_sender_map itself is
        # not set
        pass

    idx += 1
    if node.num_children > 0:
        first_child_output = []
        idx = build_summary_table(summary, idx, False, indent_level,
                                  first_child_output)
        # pylint: disable=unused-variable
        # TODO: is child_idx supposed to be unused?  See #120
        for child_idx in range(1, node.num_children):
            # All other children are indented (we only have 0, 1 or 2 children
            # for every exec node at the moment)
            idx = build_summary_table(summary, idx, False, indent_level + 1,
                                      output)
        output += first_child_output
    return idx


def connect(host, port, timeout=None, use_ssl=False, ca_cert=None,
            user=None, password=None, kerberos_service_name='impala',
            auth_mechanism=None):
    sock = get_socket(host, port, use_ssl, ca_cert)
    if timeout is not None:
        timeout = timeout * 1000.  # TSocket expects millis
    if six.PY2:
        sock.setTimeout(timeout)
    elif six.PY3:
        sock.set_timeout(timeout)
    transport = get_transport(sock, host, kerberos_service_name,
                              auth_mechanism, user, password)
    transport.open()
    protocol = TBinaryProtocol(transport)
    if six.PY2:
        # ThriftClient == ImpalaService.Client
        service = ThriftClient(protocol)
    elif six.PY3:
        # ThriftClient == TClient
        service = ThriftClient(ImpalaService, protocol)
    return service
    # We get a TApplicationException if the transport is valid, but the RPC
    # does not exist.


def ping(service):
    result = service.PingImpalaService()
    return result.version


def close_service(service):
    service._iprot.trans.close()  # pylint: disable=protected-access


def reconnect(service):
    # pylint: disable=protected-access
    service._iprot.trans.close()
    service._iprot.trans.open()


def create_beeswax_query(query_str, user, set_query_options):
    """Create a beeswax query object from a query string"""
    # TODO: Pass is actual set_query_options
    query = BeeswaxService.Query()
    query.hadoop_user = user
    query.query = query_str
    query.configuration = __options_to_string_list(set_query_options)
    return query


def execute_statement(service, query):
    rpc_result = __do_rpc(lambda: service.query(query))
    last_query_handle, status = rpc_result
    if status != RpcStatus.OK:
        raise RPCError("Error executing the query")
    return last_query_handle


def fetch_internal(service, last_query_handle, buffer_size):
    """Fetch all the results.

    This function serves a generator to create an iterable of the results.
    Result rows are passed to the shell.
    """
    result_rows = []
    while True:
        rpc_result = __do_rpc(
            lambda: service.fetch(last_query_handle, False, buffer_size))

        result, status = rpc_result

        if status != RpcStatus.OK:
            raise RPCError()

        result_rows.extend(result.data)

        if len(result_rows) >= buffer_size or not result.has_more:
            rows = [row.split('\t') for row in result_rows]
            return rows


def close_insert(service, last_query_handle):
    """Fetches the results of an INSERT query"""
    rpc_result = __do_rpc(
        lambda: service.CloseInsert(last_query_handle))
    insert_result, status = rpc_result

    if status != RpcStatus.OK:
        raise RPCError()

    num_rows = sum([int(k) for k in
                    list(insert_result.rows_appended.values())])
    return num_rows


def close_query(service, last_query_handle):
    """Close the query handle"""
    # Make closing a query handle idempotent
    rpc_result = __do_rpc(lambda: service.close(last_query_handle))
    _, status = rpc_result
    return status == RpcStatus.OK


def cancel_query(service, last_query_handle):
    """Cancel a query on a keyboard interrupt from the shell."""
    # Cancel sets query_state to EXCEPTION before calling cancel() in the
    # co-ordinator, so we don't need to wait.
    rpc_result = __do_rpc(lambda: service.Cancel(last_query_handle))
    _, status = rpc_result
    return status == RpcStatus.OK


def get_query_state(service, last_query_handle):
    rpc_result = __do_rpc(
        lambda: service.get_state(last_query_handle))
    state, status = rpc_result
    if status != RpcStatus.OK:
        return "EXCEPTION"
    return state


def get_runtime_profile(service, last_query_handle):
    rpc_result = __do_rpc(
        lambda: service.GetRuntimeProfile(last_query_handle))
    profile, status = rpc_result
    if status == RpcStatus.OK and profile:
        return profile


def get_summary(service, last_query_handle):
    """Calls GetExecSummary() for the last query handle"""
    rpc_result = __do_rpc(
        lambda: service.GetExecSummary(last_query_handle))
    summary, status = rpc_result
    if status == RpcStatus.OK and summary:
        return summary
    return None


def __do_rpc(rpc):
    """Executes the provided callable."""
    # if not self.connected:
    #     raise DisconnectedError(
    #         "Not connected (use CONNECT to establish a connection)")
    #     return None, RpcStatus.ERROR
    try:
        ret = rpc()
        status = RpcStatus.OK
        # TODO: In the future more advanced error detection/handling can be
        # done based on the TStatus return value. For now, just print any
        # error(s) that were encountered and validate the result of the
        # operation was a success.
        if ret is not None and isinstance(ret, TStatus):
            if ret.status_code != TStatusCode.OK:
                print((ret.error_msgs))
                if ret.error_msgs:
                    raise RPCError('RPC Error: %s' % '\n'.join(ret.error_msgs))
                status = RpcStatus.ERROR
        return ret, status
    except BeeswaxService.QueryNotFoundException:
        raise QueryStateError('Error: Stale query handle')
    # beeswaxException prints out the entire object, printing
    # just the message is far more readable/helpful.
    except BeeswaxService.BeeswaxException as b:
        raise RPCError("ERROR: %s" % (b.message))
    except TTransportException as e:
        # issue with the connection with the impalad
        raise DisconnectedError("Error communicating with impalad: %s" % e)
    except TApplicationException as t:
        raise RPCError("Application Exception : %s" % (t))
    return None, RpcStatus.ERROR


def get_column_names(service, last_query_handle):
    rpc_result = __do_rpc(
        lambda: service.get_results_metadata(last_query_handle))
    metadata, _ = rpc_result
    if metadata is not None:
        return [fs.name for fs in metadata.schema.fieldSchemas]


def get_results_metadata(service, last_query_handle):
    rpc_result = __do_rpc(
        lambda: service.get_results_metadata(last_query_handle))
    metadata, _ = rpc_result
    if metadata is not None:
        return metadata.schema.fieldSchemas


def expect_result_metadata(query_str):
    """ Given a query string, return True if impalad expects result metadata"""
    excluded_query_types = ['use', 'alter', 'drop', 'create', 'insert']
    if True in set(map(query_str.startswith, excluded_query_types)):
        return False
    return True


def get_warning_log(service, last_query_handle):
    if last_query_handle is None:
        return "Query could not be executed"
    rpc_result = __do_rpc(
        lambda: service.get_log(last_query_handle.log_context))
    log, status = rpc_result
    if status != RpcStatus.OK:
        return "Failed to get warning log: %s" % status
    if log and log.strip():
        return "WARNINGS: %s" % log
    return ""
