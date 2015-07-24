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

"""Implements all necessary Impala HiveServer 2 RPC functionality."""

# This work builds off of:
# 1. the Hue interface:
#       hue/apps/beeswax/src/beeswax/server/dbms.py
#       hue/apps/beeswax/src/beeswax/server/hive_server2_lib.py
#       hue/desktop/core/src/desktop/lib/thrift_util.py
# 2. the Impala shell:
#       Impala/shell/original_impala_shell.py

from __future__ import absolute_import, division

import datetime
import socket
import operator
import os
import re
import six
import sys
from decimal import Decimal
from six.moves import range

from impala.error import HiveServer2Error
from impala._rpc import thrift_util
from impala._thrift_api.hiveserver2 import (
    TTransportException, TBinaryProtocol,
    TOpenSessionReq, TFetchResultsReq, TCloseSessionReq, TExecuteStatementReq,
    TGetInfoReq, TGetInfoType, TTypeId, TFetchOrientation,
    TGetResultSetMetadataReq, TStatusCode, TGetColumnsReq, TGetSchemasReq,
    TGetTablesReq, TGetFunctionsReq, TGetOperationStatusReq, TOperationState,
    TCancelOperationReq, TCloseOperationReq, TGetLogReq, TProtocolVersion,
    TGetRuntimeProfileReq, TGetExecSummaryReq, ImpalaHiveServer2Service,
    TExecStats, ThriftClient)


# mapping between the schema types (based on
# com.cloudera.impala.catalog.PrimitiveType) and TColumnValue (in returned
# rows) helper object for converting from TRow to something friendlier
_TTypeId_to_TColumnValue_getters = {
    'BOOLEAN': operator.attrgetter('boolVal'),
    'TINYINT': operator.attrgetter('byteVal'),
    'SMALLINT': operator.attrgetter('i16Val'),
    'INT': operator.attrgetter('i32Val'),
    'BIGINT': operator.attrgetter('i64Val'),
    'TIMESTAMP': operator.attrgetter('stringVal'),
    'FLOAT': operator.attrgetter('doubleVal'),
    'DOUBLE': operator.attrgetter('doubleVal'),
    'STRING': operator.attrgetter('stringVal'),
    'DECIMAL': operator.attrgetter('stringVal'),
    'BINARY': operator.attrgetter('binaryVal'),
    'VARCHAR': operator.attrgetter('stringVal'),
    'CHAR': operator.attrgetter('stringVal'),
}

_pre_columnar_protocols = [
    TProtocolVersion.HIVE_CLI_SERVICE_PROTOCOL_V1,
    TProtocolVersion.HIVE_CLI_SERVICE_PROTOCOL_V2,
    TProtocolVersion.HIVE_CLI_SERVICE_PROTOCOL_V3,
    TProtocolVersion.HIVE_CLI_SERVICE_PROTOCOL_V4,
    TProtocolVersion.HIVE_CLI_SERVICE_PROTOCOL_V5,
]


def err_if_rpc_not_ok(resp):
    if (resp.status.statusCode != TStatusCode.SUCCESS_STATUS and
            resp.status.statusCode != TStatusCode.SUCCESS_WITH_INFO_STATUS and
            resp.status.statusCode != TStatusCode.STILL_EXECUTING_STATUS):
        raise HiveServer2Error(resp.status.errorMessage)


# datetime only supports 6 digits of microseconds but Impala supports 9.
# If present, the trailing 3 digits will be ignored without warning.
_TIMESTAMP_PATTERN = re.compile(r'(\d+-\d+-\d+ \d+:\d+:\d+(\.\d{,6})?)')


def _parse_timestamp(value):
    if value:
        match = _TIMESTAMP_PATTERN.match(value)
        if match:
            if match.group(2):
                format = '%Y-%m-%d %H:%M:%S.%f'
                # use the pattern to truncate the value
                value = match.group()
            else:
                format = '%Y-%m-%d %H:%M:%S'
            value = datetime.datetime.strptime(value, format)
        else:
            raise Exception(
                'Cannot convert "{}" into a datetime'.format(value))
    else:
        value = None
    return value


# TODO: Add another decorator that runs the function in its own thread
def threaded(func):
    raise NotImplementedError


def retry(func):
    # Retries RPCs after closing/reopening transport
    # `service` must be the first arg in args or must be a kwarg

    def wrapper(*args, **kwargs):
        # get the thrift transport
        if 'service' in kwargs:
            transport = kwargs['service']._iprot.trans
        elif len(args) > 0 and isinstance(args[0], ThriftClient):
            transport = args[0]._iprot.trans
        else:
            raise HiveServer2Error(
                "RPC function does not have expected 'service' arg")

        tries_left = 3
        while tries_left > 0:
            try:
                if six.PY2 and not transport.isOpen():
                    transport.open()
                elif six.PY3 and not transport.is_open():
                    transport.open()
                return func(*args, **kwargs)
            except socket.error:
                pass
            except TTransportException:
                pass
            except Exception:
                raise
            transport.close()
            tries_left -= 1
        raise

    return wrapper


def connect_to_impala(host, port, timeout=45, use_ssl=False, ca_cert=None,
                      username=None, password=None, kerberos_service_name='impala',
                      auth_mechanism=None):
    sock = thrift_util.get_socket(host, port, use_ssl, ca_cert)
    if six.PY2:
        sock.setTimeout(timeout * 1000.)
    elif six.PY3:
        sock.set_timeout(timeout * 1000.)
    transport = thrift_util.get_transport(sock, host, kerberos_service_name, auth_mechanism,
        username, password)
    transport.open()
    protocol = TBinaryProtocol(transport)
    if six.PY2:
        # ThriftClient == ImpalaHiveServer2Service.Client
        service = ThriftClient(protocol)
    elif six.PY3:
        # ThriftClient == TClient
        service = ThriftClient(ImpalaHiveServer2Service, protocol)
    return service


def close_service(service):
    service._iprot.trans.close()


def reconnect(service):
    service._iprot.trans.close()
    service._iprot.trans.open()


@retry
def open_session(service, user, configuration=None):
    req = TOpenSessionReq(
        client_protocol=TProtocolVersion.HIVE_CLI_SERVICE_PROTOCOL_V6,
        username=user, configuration=configuration)
    resp = service.OpenSession(req)
    err_if_rpc_not_ok(resp)
    return (resp.sessionHandle, resp.configuration, resp.serverProtocolVersion)


@retry
def close_session(service, session_handle):
    req = TCloseSessionReq(sessionHandle=session_handle)
    resp = service.CloseSession(req)
    err_if_rpc_not_ok(resp)


@retry
def execute_statement(service, session_handle, statement, configuration=None,
                      async=False):
    req = TExecuteStatementReq(sessionHandle=session_handle,
                               statement=statement, confOverlay=configuration,
                               runAsync=async)
    resp = service.ExecuteStatement(req)
    err_if_rpc_not_ok(resp)
    return resp.operationHandle


@retry
def get_result_schema(service, operation_handle):
    if not operation_handle.hasResultSet:
        return None
    req = TGetResultSetMetadataReq(operationHandle=operation_handle)
    resp = service.GetResultSetMetadata(req)
    err_if_rpc_not_ok(resp)

    schema = []
    for column in resp.schema.columns:
        name = column.columnName
        entry = column.typeDesc.types[0].primitiveEntry
        type_ = TTypeId._VALUES_TO_NAMES[entry.type].split('_')[0]
        if type_ == 'DECIMAL':
            qualifiers = entry.typeQualifiers.qualifiers
            precision = qualifiers['precision'].i32Value
            scale = qualifiers['scale'].i32Value
            schema.append((name, type_, None, None,
                           precision, scale, None))
        else:
            schema.append((name, type_, None, None, None, None, None))


    return schema


@retry
def fetch_results(service, operation_handle, hs2_protocol_version, schema=None,
                  max_rows=1024, orientation=TFetchOrientation.FETCH_NEXT):
    if not operation_handle.hasResultSet:
        return None

    # the schema is necessary to pull the proper values (i.e., coalesce)
    if schema is None:
        schema = get_result_schema(service, operation_handle)

    req = TFetchResultsReq(operationHandle=operation_handle,
                           orientation=orientation,
                           maxRows=max_rows)
    resp = service.FetchResults(req)
    err_if_rpc_not_ok(resp)

    if hs2_protocol_version == TProtocolVersion.HIVE_CLI_SERVICE_PROTOCOL_V6:
        tcols = [_TTypeId_to_TColumnValue_getters[schema[i][1]](col)
                 for (i, col) in enumerate(resp.results.columns)]
        num_cols = len(tcols)
        num_rows = len(tcols[0].values)
        rows = []
        for i in range(num_rows):
            row = []
            for j in range(num_cols):
                type_ = schema[j][1]
                values = tcols[j].values
                nulls = tcols[j].nulls
                # i // 8 is the byte, i % 8 is position in the byte; get the
                # int repr and pull out the bit at the corresponding pos
                is_null = False
                # Ref HUE-2722, HiveServer2 sometimes does not add not put
                # trailing '\x00'.
                if len(values) != len(nulls):
                    nulls = nulls + ('\x00' * (len(values) - len(nulls)))
                # Hive encodes nulls differently than Impala
                # (\x00 vs \x00\x00 ...)
                if not re.match('^(\x00)+$', nulls):
                    is_null = ord(nulls[i // 8]) & (1 << (i % 8))
                if is_null:
                    row.append(None)
                elif type_ == 'TIMESTAMP':
                    row.append(_parse_timestamp(values[i]))
                elif type_ == 'DECIMAL':
                    row.append(Decimal(values[i]))
                else:
                    row.append(values[i])
            rows.append(tuple(row))
    elif hs2_protocol_version in _pre_columnar_protocols:
        rows = []
        for trow in resp.results.rows:
            row = []
            for (i, col_val) in enumerate(trow.colVals):
                type_ = schema[i][1]
                value = _TTypeId_to_TColumnValue_getters[type_](col_val).value
                if type_ == 'TIMESTAMP':
                    value = _parse_timestamp(value)
                elif type_ == 'DECIMAL':
                    if value:
                        value = Decimal(value)
                row.append(value)
            rows.append(tuple(row))
    else:
        raise HiveServer2Error(
            ("Got HiveServer2 version %s. " %
                TProtocolVersion._VALUES_TO_NAMES[hs2_protocol_version]) +
            "Expected V1 - V6")
    return rows


@retry
def get_current_database(service, session_handle):
    raise NotImplementedError


@retry
def get_databases(service, session_handle):
    req = TGetSchemasReq(sessionHandle=session_handle, schemaName='.*')
    resp = service.GetSchemas(req)
    err_if_rpc_not_ok(resp)
    return resp.operationHandle


@retry
def database_exists(service, session_handle, hs2_protocol_version, db_name):
    req = TGetSchemasReq(sessionHandle=session_handle, schemaName=db_name)
    resp = service.GetSchemas(req)
    err_if_rpc_not_ok(resp)
    operation_handle = resp.operationHandle
    # this only fetches default max_rows, but there should only be one row
    # ideally
    results = fetch_results(service=service, operation_handle=operation_handle,
                            hs2_protocol_version=hs2_protocol_version)
    exists = False
    for result in results:
        if result[0].lower() == db_name.lower():
            exists = True
    close_operation(service, operation_handle)
    return exists


@retry
def get_tables(service, session_handle, database_name='.*'):
    req = TGetTablesReq(sessionHandle=session_handle, schemaName=database_name,
                        tableName='.*')
    resp = service.GetTables(req)
    err_if_rpc_not_ok(resp)
    return resp.operationHandle


@retry
def table_exists(service, session_handle, hs2_protocol_version, table_name,
                 database_name='.*'):
    req = TGetTablesReq(sessionHandle=session_handle, schemaName=database_name,
                        tableName=table_name)
    resp = service.GetTables(req)
    err_if_rpc_not_ok(resp)
    operation_handle = resp.operationHandle
    # this only fetches default max_rows, but there should only be one row
    # ideally
    results = fetch_results(service=service, operation_handle=operation_handle,
                            hs2_protocol_version=hs2_protocol_version)
    exists = False
    for result in results:
        if result[2].lower() == table_name.lower():
            exists = True
    close_operation(service, operation_handle)
    return exists


@retry
def get_table_schema(service, session_handle, table_name, database_name='.*'):
    req = TGetColumnsReq(sessionHandle=session_handle,
                         schemaName=database_name, tableName=table_name,
                         columnName='.*')
    resp = service.GetColumns(req)
    err_if_rpc_not_ok(resp)
    return resp.operationHandle


@retry
def get_functions(service, session_handle, database_name='.*'):
    # TODO: need to test this one especially
    req = TGetFunctionsReq(sessionHandle=session_handle,
                           schemaName=database_name,
                           functionName='.*')
    resp = service.GetFunctions(req)
    err_if_rpc_not_ok(resp)
    return resp.operationHandle


@retry
def get_operation_status(service, operation_handle):
    req = TGetOperationStatusReq(operationHandle=operation_handle)
    resp = service.GetOperationStatus(req)
    err_if_rpc_not_ok(resp)
    return TOperationState._VALUES_TO_NAMES[resp.operationState]


@retry
def cancel_operation(service, operation_handle):
    req = TCancelOperationReq(operationHandle=operation_handle)
    resp = service.CancelOperation(req)
    err_if_rpc_not_ok(resp)


@retry
def close_operation(service, operation_handle):
    req = TCloseOperationReq(operationHandle=operation_handle)
    resp = service.CloseOperation(req)
    err_if_rpc_not_ok(resp)


@retry
def get_log(service, operation_handle):
    req = TGetLogReq(operationHandle=operation_handle)
    resp = service.GetLog(req)
    err_if_rpc_not_ok(resp)
    return resp.log


def ping(service, session_handle):
    req = TGetInfoReq(sessionHandle=session_handle,
                      infoType=TGetInfoType.CLI_SERVER_NAME)
    try:
        resp = service.GetInfo(req)
    except TTransportException:
        return False

    try:
        err_if_rpc_not_ok(resp)
    except HiveServer2Error:
        return False
    return True


def get_profile(service, operation_handle, session_handle):
    req = TGetRuntimeProfileReq(operationHandle=operation_handle,
                                sessionHandle=session_handle)
    resp = service.GetRuntimeProfile(req)
    err_if_rpc_not_ok(resp)
    return resp.profile


def get_summary(service, operation_handle, session_handle):
    req = TGetExecSummaryReq(operationHandle=operation_handle,
                             sessionHandle=session_handle)
    resp = service.GetExecSummary(req)
    err_if_rpc_not_ok(resp)
    return resp.summary


def build_summary_table(summary, idx, is_fragment_root, indent_level, output):
    """Direct translation of Coordinator::PrintExecSummary() to recursively
    build a list of rows of summary statistics, one per exec node

    summary: the TExecSummary object that contains all the summary data

    idx: the index of the node to print

    is_fragment_root: true if the node to print is the root of a fragment (and
    therefore feeds into an exchange)

    indent_level: the number of spaces to print before writing the node's
    label, to give the appearance of a tree. The 0th child of a node has the
    same indent_level as its parent. All other children have an indent_level
    of one greater than their parent.

    output: the list of rows into which to append the rows produced for this
    node and its children.

    Returns the index of the next exec node in summary.exec_nodes that should
    be processed, used internally to this method only.
    """
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
        for child_idx in range(1, node.num_children):
            # All other children are indented (we only have 0, 1 or 2 children
            # for every exec node at the moment)
            idx = build_summary_table(summary, idx, False, indent_level + 1,
                                      output)
        output += first_child_output
    return idx
