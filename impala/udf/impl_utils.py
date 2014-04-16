
import llvm.core as lc
from numba import types as ntypes
from numba import cgutils

from .types import AnyVal


# struct access utils

# these are necessary because cgutils.Structure assumes no nested types;
# the gep needs a (0, 0, 0) offset

def _get_is_null_pointer(builder, val):
    ptr = cgutils.inbound_gep(builder, val._getpointer(), 0, 0, 0)
    return ptr

def _get_is_null(builder, val):
    byte = builder.load(_get_is_null_pointer(builder, val))
    return builder.trunc(byte, lc.Type.int(1))

def _set_is_null(builder, val, is_null):
    byte = builder.zext(is_null, lc.Type.int(8))
    builder.store(byte, _get_is_null_pointer(builder, val))


# Impala *Val struct impls

class AnyValStruct(cgutils.Structure):
    _fields = [('is_null', ntypes.boolean)]


class BooleanValStruct(cgutils.Structure):
    _fields = [('parent',  AnyVal),
	       ('val',     ntypes.int8),]


class TinyIntValStruct(cgutils.Structure):
    _fields = [('parent',  AnyVal),
	       ('val',     ntypes.int8),]


class SmallIntValStruct(cgutils.Structure):
    _fields = [('parent',  AnyVal),
	       ('val',     ntypes.int16),]


class IntValStruct(cgutils.Structure):
    _fields = [('parent',  AnyVal),
	       ('val',     ntypes.int32),]


class BigIntValStruct(cgutils.Structure):
    _fields = [('parent',  AnyVal),
	       ('val',     ntypes.int64),]


class FloatValStruct(cgutils.Structure):
    _fields = [('parent',  AnyVal),
	       ('val',     ntypes.float32),]


class DoubleValStruct(cgutils.Structure):
    _fields = [('parent',  AnyVal),
	       ('val',     ntypes.float64),]


class StringValStruct(cgutils.Structure):
    _fields = [('parent',  AnyVal),
	       ('len',     ntypes.int32),
	       ('ptr',     ntypes.CPointer(ntypes.uint8))]
