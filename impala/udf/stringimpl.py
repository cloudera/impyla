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

"""Implementations for the Python string module"""

from __future__ import absolute_import

import string

from numba import cgutils
from numba.targets.imputils import implement, Registry

from impala.udf.types import StringVal, IntVal
from impala.udf.impl_utils import _conv_numba_struct_to_clang, StringValStruct
from impala.udf.abi import raise_return_type

registry = Registry()
register_function = registry.register
register_attribute = registry.register_attr


@register_function
@implement(string.capitalize, StringVal)
def string_capitalize(context, builder, sig, args):
    module = cgutils.get_module(builder)
    precomp_func = context._get_precompiled_function("StringCapitalizeImpl")
    func = module.get_or_insert_function(
        precomp_func.type.pointee, precomp_func.name)
    fnctx_arg = context.get_arguments(cgutils.get_function(builder))[0]
    cfnctx_arg = builder.bitcast(fnctx_arg, func.args[0].type)
    [s] = args
    cs = _conv_numba_struct_to_clang(builder, s, func.args[1].type)
    result = builder.call(func, [cfnctx_arg, cs])
    return raise_return_type(context, builder, StringVal, result)


@register_function
@implement(string.split, StringVal, StringVal)
def string_split_2(context, builder, sig, args):
    module = cgutils.get_module(builder)
    precomp_func = context._get_precompiled_function("StringSplitImpl")
    func = module.get_or_insert_function(
        precomp_func.type.pointee, precomp_func.name)
    fnctx_arg = context.get_arguments(cgutils.get_function(builder))[0]
    cfnctx_arg = builder.bitcast(fnctx_arg, func.args[0].type)
    [s, sep] = args
    maxsplit = context.get_constant_struct(builder, IntVal, -1)
    cs = _conv_numba_struct_to_clang(builder, s, func.args[1].type)
    csep = _conv_numba_struct_to_clang(builder, sep, func.args[2].type)
    cmaxsplit = _conv_numba_struct_to_clang(
        builder, maxsplit, func.args[3].type)
    # result is StringVal with an array of StringVals in the buffer
    array_as_lowered_struct = builder.call(
        func, [cfnctx_arg, cs, csep, cmaxsplit])
    array_as_struct = raise_return_type(
        context, builder, StringVal, array_as_lowered_struct)
    array_as_StringVal = StringValStruct(
        context, builder, value=array_as_struct)
    array_as_numba = context.make_array(sig.return_type)(context, builder)
    data_ptr = builder.bitcast(
        array_as_StringVal.ptr, array_as_numba.data.type)
    array_as_numba.data = data_ptr
    return array_as_numba._getvalue()


# @register_function
# @implement(string.split, StringVal, StringVal, IntVal)
# def string_split_3(context, builder, sig, args):
#     import ipdb
#     ipdb.set_trace()
#     module = cgutils.get_module(builder)
#     precomp_func = context._get_precompiled_function("StringSplitImpl")
#     func = module.get_or_insert_function(precomp_func.type.pointee,
#                                          precomp_func.name)
#     fnctx_arg = context.get_arguments(cgutils.get_function(builder))[0]
#     cfnctx_arg = builder.bitcast(fnctx_arg, func.args[0].type)
#     [s, sep, maxsplit] = args
#     cs = _conv_numba_struct_to_clang(builder, s, func.args[1].type)
#     csep = _conv_numba_struct_to_clang(builder, s, func.args[2].type)
#     cmaxsplit = _conv_numba_struct_to_clang(builder, s, func.args[3].type)
#     array = builder.call(func, [cfnctx_arg, cs, csep, cmaxsplit])
#     pass
#     # allocate array of StringVals
#     # fill the array with splits (up through max space) and return
#     # total splits

#     # count the number of StringVals I need
#     # alloca the array
#     # fill it
