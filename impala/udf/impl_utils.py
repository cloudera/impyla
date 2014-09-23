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

import llvm.core as lc
from numba import types as ntypes
from numba import cgutils

from .types import AnyVal


# struct access utils

# these are necessary because cgutils.Structure assumes no nested types;
# the gep needs a (0, 0, 0) offset

def _get_is_null_pointer(builder, val):
    ptr = builder.gep(val._getpointer(),
                      [lc.Constant.int(lc.Type.int(32), 0)] * 3, # gep(0, 0, 0)
                      inbounds=True)
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


# misc impl utilies

def _conv_numba_struct_to_clang(builder, numba_arg, clang_arg_type):
    stack_var = cgutils.alloca_once(builder, numba_arg.type)
    builder.store(numba_arg, stack_var)
    clang_arg = builder.bitcast(stack_var, clang_arg_type)
    return clang_arg
