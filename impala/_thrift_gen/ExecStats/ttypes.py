#
# Autogenerated by Thrift Compiler (0.11.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style,no_utf8strings
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import impala._thrift_gen.Status.ttypes
import impala._thrift_gen.Types.ttypes

from thrift.transport import TTransport
all_structs = []


class TExecState(object):
    REGISTERED = 0
    PLANNING = 1
    QUEUED = 2
    RUNNING = 3
    FINISHED = 4
    CANCELLED = 5
    FAILED = 6

    _VALUES_TO_NAMES = {
        0: "REGISTERED",
        1: "PLANNING",
        2: "QUEUED",
        3: "RUNNING",
        4: "FINISHED",
        5: "CANCELLED",
        6: "FAILED",
    }

    _NAMES_TO_VALUES = {
        "REGISTERED": 0,
        "PLANNING": 1,
        "QUEUED": 2,
        "RUNNING": 3,
        "FINISHED": 4,
        "CANCELLED": 5,
        "FAILED": 6,
    }


class TExecStats(object):
    """
    Attributes:
     - latency_ns
     - cpu_time_ns
     - cardinality
     - memory_used
    """


    def __init__(self, latency_ns=None, cpu_time_ns=None, cardinality=None, memory_used=None,):
        self.latency_ns = latency_ns
        self.cpu_time_ns = cpu_time_ns
        self.cardinality = cardinality
        self.memory_used = memory_used

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.latency_ns = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.cpu_time_ns = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.cardinality = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I64:
                    self.memory_used = iprot.readI64()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('TExecStats')
        if self.latency_ns is not None:
            oprot.writeFieldBegin('latency_ns', TType.I64, 1)
            oprot.writeI64(self.latency_ns)
            oprot.writeFieldEnd()
        if self.cpu_time_ns is not None:
            oprot.writeFieldBegin('cpu_time_ns', TType.I64, 2)
            oprot.writeI64(self.cpu_time_ns)
            oprot.writeFieldEnd()
        if self.cardinality is not None:
            oprot.writeFieldBegin('cardinality', TType.I64, 3)
            oprot.writeI64(self.cardinality)
            oprot.writeFieldEnd()
        if self.memory_used is not None:
            oprot.writeFieldBegin('memory_used', TType.I64, 4)
            oprot.writeI64(self.memory_used)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class TPlanNodeExecSummary(object):
    """
    Attributes:
     - node_id
     - fragment_idx
     - label
     - label_detail
     - num_children
     - estimated_stats
     - exec_stats
     - is_broadcast
    """


    def __init__(self, node_id=None, fragment_idx=None, label=None, label_detail=None, num_children=None, estimated_stats=None, exec_stats=None, is_broadcast=None,):
        self.node_id = node_id
        self.fragment_idx = fragment_idx
        self.label = label
        self.label_detail = label_detail
        self.num_children = num_children
        self.estimated_stats = estimated_stats
        self.exec_stats = exec_stats
        self.is_broadcast = is_broadcast

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.node_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.fragment_idx = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.label = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.label_detail = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.num_children = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRUCT:
                    self.estimated_stats = TExecStats()
                    self.estimated_stats.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.LIST:
                    self.exec_stats = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = TExecStats()
                        _elem5.read(iprot)
                        self.exec_stats.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.BOOL:
                    self.is_broadcast = iprot.readBool()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('TPlanNodeExecSummary')
        if self.node_id is not None:
            oprot.writeFieldBegin('node_id', TType.I32, 1)
            oprot.writeI32(self.node_id)
            oprot.writeFieldEnd()
        if self.fragment_idx is not None:
            oprot.writeFieldBegin('fragment_idx', TType.I32, 2)
            oprot.writeI32(self.fragment_idx)
            oprot.writeFieldEnd()
        if self.label is not None:
            oprot.writeFieldBegin('label', TType.STRING, 3)
            oprot.writeString(self.label)
            oprot.writeFieldEnd()
        if self.label_detail is not None:
            oprot.writeFieldBegin('label_detail', TType.STRING, 4)
            oprot.writeString(self.label_detail)
            oprot.writeFieldEnd()
        if self.num_children is not None:
            oprot.writeFieldBegin('num_children', TType.I32, 5)
            oprot.writeI32(self.num_children)
            oprot.writeFieldEnd()
        if self.estimated_stats is not None:
            oprot.writeFieldBegin('estimated_stats', TType.STRUCT, 6)
            self.estimated_stats.write(oprot)
            oprot.writeFieldEnd()
        if self.exec_stats is not None:
            oprot.writeFieldBegin('exec_stats', TType.LIST, 7)
            oprot.writeListBegin(TType.STRUCT, len(self.exec_stats))
            for iter6 in self.exec_stats:
                iter6.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.is_broadcast is not None:
            oprot.writeFieldBegin('is_broadcast', TType.BOOL, 8)
            oprot.writeBool(self.is_broadcast)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.node_id is None:
            raise TProtocolException(message='Required field node_id is unset!')
        if self.fragment_idx is None:
            raise TProtocolException(message='Required field fragment_idx is unset!')
        if self.label is None:
            raise TProtocolException(message='Required field label is unset!')
        if self.num_children is None:
            raise TProtocolException(message='Required field num_children is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class TExecProgress(object):
    """
    Attributes:
     - total_scan_ranges
     - num_completed_scan_ranges
    """


    def __init__(self, total_scan_ranges=None, num_completed_scan_ranges=None,):
        self.total_scan_ranges = total_scan_ranges
        self.num_completed_scan_ranges = num_completed_scan_ranges

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.total_scan_ranges = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.num_completed_scan_ranges = iprot.readI64()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('TExecProgress')
        if self.total_scan_ranges is not None:
            oprot.writeFieldBegin('total_scan_ranges', TType.I64, 1)
            oprot.writeI64(self.total_scan_ranges)
            oprot.writeFieldEnd()
        if self.num_completed_scan_ranges is not None:
            oprot.writeFieldBegin('num_completed_scan_ranges', TType.I64, 2)
            oprot.writeI64(self.num_completed_scan_ranges)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class TExecSummary(object):
    """
    Attributes:
     - state
     - status
     - nodes
     - exch_to_sender_map
     - error_logs
     - progress
     - is_queued
     - queued_reason
    """


    def __init__(self, state=None, status=None, nodes=None, exch_to_sender_map=None, error_logs=None, progress=None, is_queued=None, queued_reason=None,):
        self.state = state
        self.status = status
        self.nodes = nodes
        self.exch_to_sender_map = exch_to_sender_map
        self.error_logs = error_logs
        self.progress = progress
        self.is_queued = is_queued
        self.queued_reason = queued_reason

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.state = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.status = impala._thrift_gen.Status.ttypes.TStatus()
                    self.status.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.nodes = []
                    (_etype10, _size7) = iprot.readListBegin()
                    for _i11 in range(_size7):
                        _elem12 = TPlanNodeExecSummary()
                        _elem12.read(iprot)
                        self.nodes.append(_elem12)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.MAP:
                    self.exch_to_sender_map = {}
                    (_ktype14, _vtype15, _size13) = iprot.readMapBegin()
                    for _i17 in range(_size13):
                        _key18 = iprot.readI32()
                        _val19 = iprot.readI32()
                        self.exch_to_sender_map[_key18] = _val19
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.LIST:
                    self.error_logs = []
                    (_etype23, _size20) = iprot.readListBegin()
                    for _i24 in range(_size20):
                        _elem25 = iprot.readString()
                        self.error_logs.append(_elem25)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRUCT:
                    self.progress = TExecProgress()
                    self.progress.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.BOOL:
                    self.is_queued = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRING:
                    self.queued_reason = iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('TExecSummary')
        if self.state is not None:
            oprot.writeFieldBegin('state', TType.I32, 1)
            oprot.writeI32(self.state)
            oprot.writeFieldEnd()
        if self.status is not None:
            oprot.writeFieldBegin('status', TType.STRUCT, 2)
            self.status.write(oprot)
            oprot.writeFieldEnd()
        if self.nodes is not None:
            oprot.writeFieldBegin('nodes', TType.LIST, 3)
            oprot.writeListBegin(TType.STRUCT, len(self.nodes))
            for iter26 in self.nodes:
                iter26.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.exch_to_sender_map is not None:
            oprot.writeFieldBegin('exch_to_sender_map', TType.MAP, 4)
            oprot.writeMapBegin(TType.I32, TType.I32, len(self.exch_to_sender_map))
            for kiter27, viter28 in self.exch_to_sender_map.items():
                oprot.writeI32(kiter27)
                oprot.writeI32(viter28)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        if self.error_logs is not None:
            oprot.writeFieldBegin('error_logs', TType.LIST, 5)
            oprot.writeListBegin(TType.STRING, len(self.error_logs))
            for iter29 in self.error_logs:
                oprot.writeString(iter29)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.progress is not None:
            oprot.writeFieldBegin('progress', TType.STRUCT, 6)
            self.progress.write(oprot)
            oprot.writeFieldEnd()
        if self.is_queued is not None:
            oprot.writeFieldBegin('is_queued', TType.BOOL, 7)
            oprot.writeBool(self.is_queued)
            oprot.writeFieldEnd()
        if self.queued_reason is not None:
            oprot.writeFieldBegin('queued_reason', TType.STRING, 8)
            oprot.writeString(self.queued_reason)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.state is None:
            raise TProtocolException(message='Required field state is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(TExecStats)
TExecStats.thrift_spec = (
    None,  # 0
    (1, TType.I64, 'latency_ns', None, None, ),  # 1
    (2, TType.I64, 'cpu_time_ns', None, None, ),  # 2
    (3, TType.I64, 'cardinality', None, None, ),  # 3
    (4, TType.I64, 'memory_used', None, None, ),  # 4
)
all_structs.append(TPlanNodeExecSummary)
TPlanNodeExecSummary.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'node_id', None, None, ),  # 1
    (2, TType.I32, 'fragment_idx', None, None, ),  # 2
    (3, TType.STRING, 'label', None, None, ),  # 3
    (4, TType.STRING, 'label_detail', None, None, ),  # 4
    (5, TType.I32, 'num_children', None, None, ),  # 5
    (6, TType.STRUCT, 'estimated_stats', [TExecStats, None], None, ),  # 6
    (7, TType.LIST, 'exec_stats', (TType.STRUCT, [TExecStats, None], False), None, ),  # 7
    (8, TType.BOOL, 'is_broadcast', None, None, ),  # 8
)
all_structs.append(TExecProgress)
TExecProgress.thrift_spec = (
    None,  # 0
    (1, TType.I64, 'total_scan_ranges', None, None, ),  # 1
    (2, TType.I64, 'num_completed_scan_ranges', None, None, ),  # 2
)
all_structs.append(TExecSummary)
TExecSummary.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'state', None, None, ),  # 1
    (2, TType.STRUCT, 'status', [impala._thrift_gen.Status.ttypes.TStatus, None], None, ),  # 2
    (3, TType.LIST, 'nodes', (TType.STRUCT, [TPlanNodeExecSummary, None], False), None, ),  # 3
    (4, TType.MAP, 'exch_to_sender_map', (TType.I32, None, TType.I32, None, False), None, ),  # 4
    (5, TType.LIST, 'error_logs', (TType.STRING, None, False), None, ),  # 5
    (6, TType.STRUCT, 'progress', [TExecProgress, None], None, ),  # 6
    (7, TType.BOOL, 'is_queued', None, None, ),  # 7
    (8, TType.STRING, 'queued_reason', None, None, ),  # 8
)
fix_spec(all_structs)
del all_structs
