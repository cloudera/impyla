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

"""ABI handling and type lowering/raising"""

from __future__ import absolute_import

import llvm.core as lc

from .types import (AnyVal, BooleanVal, TinyIntVal, SmallIntVal, IntVal,
                    BigIntVal, FloatVal, DoubleVal, StringVal)
from .impl_utils import (BooleanValStruct, TinyIntValStruct, SmallIntValStruct,
                         IntValStruct, BigIntValStruct, FloatValStruct,
                         DoubleValStruct, StringValStruct)
from .impl_utils import _get_is_null, _set_is_null


class ABIHandling(object):
    """
    Adapt to C++ ABI for x86-64
    """
    def __init__(self, context, func, restype, argtypes):
        self.context = context
        self.func = func
        self.restype = restype
        self.argtypes = argtypes

    def build_wrapper(self, wrappername):
        abi_restype = self.get_abi_return_type(self.restype).pointee # should always ret pointer type
        abi_argtypes = [self.get_abi_argument_type(a)
                        for a in self.argtypes]
        fnty = lc.Type.function(abi_restype, abi_argtypes)
        wrapper = self.func.module.add_function(fnty, name=wrappername)

        builder = lc.Builder.new(wrapper.append_basic_block(''))
        status, res = self.context.call_function(builder, self.func, self.restype,
                                                 self.argtypes, wrapper.args)
        # FIXME ignoring error in function for now
        cres = lower_return_type(self.context, builder, self.restype, res)
        builder.ret(cres)
        return wrapper

    def get_abi_return_type(self, ty):
        # FIXME only work on x86-64 + gcc
        if ty == BooleanVal:
            return lc.Type.pointer(lc.Type.int(16))
        elif ty == TinyIntVal:
            return lc.Type.pointer(lc.Type.int(16))
        elif ty == SmallIntVal:
            return lc.Type.pointer(lc.Type.int(32))
        elif ty == IntVal:
            return lc.Type.pointer(lc.Type.int(64))
        elif ty == BigIntVal:
            return lc.Type.pointer(lc.Type.struct([lc.Type.int(8), lc.Type.int(64)]))
        elif ty == FloatVal:
            return lc.Type.pointer(lc.Type.int(64))
        elif ty == DoubleVal:
            return lc.Type.pointer(lc.Type.struct([lc.Type.int(8), lc.Type.double()]))
        elif ty == StringVal:
            return lc.Type.pointer(lc.Type.struct([lc.Type.int(64), lc.Type.pointer(lc.Type.int(8))]))
        else:
            return self.context.get_return_type(ty)

    def get_abi_argument_type(self, ty):
        return self.context.get_argument_type(ty)


def lower_return_type(context, builder, ty, val):
    """
    Convert value to fit ABI requirement
    """
    if ty == BooleanVal:
        # Pack structure into int16
        # Endian specific
        iv = BooleanValStruct(context, builder, value=val)
        lower = builder.zext(_get_is_null(builder, iv), lc.Type.int(16))
        upper = builder.zext(iv.val, lc.Type.int(16))
        asint16 = builder.shl(upper, lc.Constant.int(lc.Type.int(16), 8))
        asint16 = builder.or_(asint16, lower)
        return asint16
    elif ty == TinyIntVal:
        # Pack structure into int16
        # Endian specific
        iv = TinyIntValStruct(context, builder, value=val)
        lower = builder.zext(_get_is_null(builder, iv), lc.Type.int(16))
        upper = builder.zext(iv.val, lc.Type.int(16))
        asint16 = builder.shl(upper, lc.Constant.int(lc.Type.int(16), 8))
        asint16 = builder.or_(asint16, lower)
        return asint16
    elif ty == SmallIntVal:
        # Pack structure into int32
        # Endian specific
        iv = SmallIntValStruct(context, builder, value=val)
        lower = builder.zext(_get_is_null(builder, iv), lc.Type.int(32))
        upper = builder.zext(iv.val, lc.Type.int(32))
        asint32 = builder.shl(upper, lc.Constant.int(lc.Type.int(32), 16))
        asint32 = builder.or_(asint32, lower)
        return asint32
    elif ty == IntVal:
        # Pack structure into int64
        # Endian specific
        iv = IntValStruct(context, builder, value=val)
        lower = builder.zext(_get_is_null(builder, iv), lc.Type.int(64))
        upper = builder.zext(iv.val, lc.Type.int(64))
        asint64 = builder.shl(upper, lc.Constant.int(lc.Type.int(64), 32))
        asint64 = builder.or_(asint64, lower)
        return asint64
    elif ty == BigIntVal:
        # Pack structure into { int8, int64 }
        # Endian specific
        iv = BigIntValStruct(context, builder, value=val)
        is_null = builder.zext(_get_is_null(builder, iv), lc.Type.int(8))
        asstructi8i64 = builder.insert_value(lc.Constant.undef(lc.Type.struct([lc.Type.int(8), lc.Type.int(64)])),
                                             is_null,
                                             0)
        asstructi8i64 = builder.insert_value(asstructi8i64, iv.val, 1)
        return asstructi8i64
    elif ty == FloatVal:
        # Pack structure into int64
        # Endian specific
        iv = FloatValStruct(context, builder, value=val)
        lower = builder.zext(_get_is_null(builder, iv), lc.Type.int(64))
        asint32 = builder.bitcast(iv.val, lc.Type.int(32))
        upper = builder.zext(asint32, lc.Type.int(64))
        asint64 = builder.shl(upper, lc.Constant.int(lc.Type.int(64), 32))
        asint64 = builder.or_(asint64, lower)
        return asint64
    elif ty == DoubleVal:
        # Pack structure into { int8, double }
        # Endian specific
        iv = DoubleValStruct(context, builder, value=val)
        is_null = builder.zext(_get_is_null(builder, iv), lc.Type.int(8))
        asstructi8double = builder.insert_value(lc.Constant.undef(lc.Type.struct([lc.Type.int(8), lc.Type.double()])),
                                                is_null,
                                                0)
        asstructi8double = builder.insert_value(asstructi8double, iv.val, 1)
        return asstructi8double
    elif ty == StringVal:
        # Pack structure into { int64, int8* }
        # Endian specific
        iv = StringValStruct(context, builder, value=val)
        is_null = builder.zext(_get_is_null(builder, iv), lc.Type.int(64))
        len_ = builder.zext(iv.len, lc.Type.int(64))
        asint64 = builder.shl(len_, lc.Constant.int(lc.Type.int(64), 32))
        asint64 = builder.or_(asint64, is_null)
        asstructi64i8p = builder.insert_value(lc.Constant.undef(lc.Type.struct([lc.Type.int(64), lc.Type.pointer(lc.Type.int(8))])),
                                              asint64,
                                              0)
        asstructi64i8p = builder.insert_value(asstructi64i8p, iv.ptr, 1)
        return asstructi64i8p
    else:
        return val

def raise_return_type(context, builder, ty, val):
    if ty == BooleanVal:
        bv = BooleanValStruct(context, builder)
        is_null = builder.trunc(val, lc.Type.int(8))
        _set_is_null(builder, bv, is_null)
        shifted = builder.lshr(val, lc.Constant.int(lc.Type.int(16), 8))
        bv.val = builder.trunc(shifted, lc.Type.int(8))
        return bv._getvalue()
    elif ty == TinyIntVal:
        tiv = TinyIntValStruct(context, builder)
        is_null = builder.trunc(val, lc.Type.int(8))
        _set_is_null(builder, tiv, is_null)
        shifted = builder.lshr(val, lc.Constant.int(lc.Type.int(16), 8))
        tiv.val = builder.trunc(shifted, lc.Type.int(8))
        return tiv._getvalue()
    elif ty == SmallIntVal:
        siv = SmallIntValStruct(context, builder)
        is_null = builder.trunc(val, lc.Type.int(8))
        _set_is_null(builder, siv, is_null)
        shifted = builder.lshr(val, lc.Constant.int(lc.Type.int(32), 16))
        siv.val = builder.trunc(shifted, lc.Type.int(16))
        return siv._getvalue()
    elif ty == IntVal:
        iv = IntValStruct(context, builder)
        is_null = builder.trunc(val, lc.Type.int(8))
        _set_is_null(builder, iv, is_null)
        shifted = builder.lshr(val, lc.Constant.int(lc.Type.int(64), 32))
        iv.val = builder.trunc(shifted, lc.Type.int(32))
        return iv._getvalue()
    elif ty == BigIntVal:
        biv = BigIntValStruct(context, builder)
        is_null = builder.extract_value(val, 0)
        _set_is_null(builder, biv, is_null)
        biv.val = builder.extract_value(val, 1)
        return biv._getvalue()
    elif ty == FloatVal:
        fv = FloatValStruct(context, builder)
        is_null = builder.trunc(val, lc.Type.int(8))
        _set_is_null(builder, fv, is_null)
        shifted = builder.lshr(val, lc.Constant.int(lc.Type.int(64), 32))
        truncated = builder.trunc(shifted, lc.Type.int(32))
        fv.val = builder.bitcast(truncated, lc.Type.float())
        return fv._getvalue()
    elif ty == DoubleVal:
        dv = DoubleValStruct(context, builder)
        is_null = builder.extract_value(val, 0)
        _set_is_null(builder, dv, is_null)
        dv.val = builder.extract_value(val, 1)
        return dv._getvalue()
    elif ty == StringVal:
        sv = StringValStruct(context, builder)
        packed = builder.extract_value(val, 0)
        is_null = builder.trunc(packed, lc.Type.int(8))
        _set_is_null(builder, sv, is_null)
        shifted = builder.lshr(packed, lc.Constant.int(lc.Type.int(64), 32))
        sv.len = builder.trunc(shifted, lc.Type.int(32))
        sv.ptr = builder.extract_value(val, 1)
        return sv._getvalue()
    else:
        return val
