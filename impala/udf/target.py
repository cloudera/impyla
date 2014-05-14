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

"""Define the Impala target context for Numba and 'builtin' impls"""

from __future__ import absolute_import

import pkgutil

import llvm.core as lc
import llvm.passes as lp
import llvm.ee as le
from numba import types as ntypes
from numba import cgutils, lowering
from numba.targets.base import BaseContext
from numba.targets.imputils import Registry, implement, impl_attribute

from . import stringimpl
from .abi import ABIHandling, raise_return_type
from .types import (FunctionContext, AnyVal, BooleanVal, BooleanValType,
		    TinyIntVal, TinyIntValType, SmallIntVal, SmallIntValType,
		    IntVal, IntValType, BigIntVal, BigIntValType, FloatVal,
		    FloatValType, DoubleVal, DoubleValType, StringVal,
		    StringValType)
from .impl_utils import (AnyValStruct, BooleanValStruct, TinyIntValStruct,
			 SmallIntValStruct, IntValStruct, BigIntValStruct,
			 FloatValStruct, DoubleValStruct, StringValStruct)
from .impl_utils import _get_is_null, _set_is_null, _conv_numba_struct_to_clang


registry = Registry()
register_function = registry.register
register_attribute = registry.register_attr


# ctor impls

def _ctor_factory(Struct, Type, *input_args):
    @implement(Type, *input_args)
    def Val_ctor(context, builder, sig, args):
	[x] = args
	v = Struct(context, builder)
	_set_is_null(builder, v, cgutils.false_bit)
	v.val = x
	return v._getvalue()
    return register_function(Val_ctor)

BooleanVal_ctor = _ctor_factory(BooleanValStruct, BooleanValType, ntypes.int8)
TinyIntVal_ctor = _ctor_factory(TinyIntValStruct, TinyIntValType, ntypes.int8)
SmallIntVal_ctor = _ctor_factory(SmallIntValStruct, SmallIntValType, ntypes.int16)
IntVal_ctor = _ctor_factory(IntValStruct, IntValType, ntypes.int32)
BigIntVal_ctor = _ctor_factory(BigIntValStruct, BigIntValType, ntypes.int64)
FloatVal_ctor = _ctor_factory(FloatValStruct, FloatValType, ntypes.float32)
DoubleVal_ctor = _ctor_factory(DoubleValStruct, DoubleValType, ntypes.float64)

@register_function
@implement(StringValType, ntypes.string)
def StringVal_ctor(context, builder, sig, args):
    """StringVal(ntypes.string)"""
    [x] = args
    iv = StringValStruct(context, builder)
    _set_is_null(builder, iv, cgutils.false_bit)
    fndesc = lowering.describe_external('strlen', ntypes.uintp, [ntypes.CPointer(ntypes.char)])
    func = context.declare_external_function(cgutils.get_module(builder), fndesc)
    strlen_x = context.call_external_function(builder, func, fndesc.argtypes, [x])
    len_x = builder.trunc(strlen_x, lc.Type.int(32))
    iv.len = len_x
    iv.ptr = x
    return iv._getvalue()


# *Val attributes

def _is_null_attr_factory(Struct, Val):
    @impl_attribute(Val, "is_null", ntypes.boolean)
    def Val_is_null(context, builder, typ, value):
	v = Struct(context, builder, value=value)
	is_null = _get_is_null(builder, v)
	return is_null
    return register_attribute(Val_is_null)

def _val_attr_factory(Struct, Val, retty):
    @impl_attribute(Val, "val", retty)
    def Val_val(context, builder, typ, value):
	v = Struct(context, builder, value=value)
	return v.val
    return register_attribute(Val_val)

# *Val.is_null
BooleanVal_is_null = _is_null_attr_factory(BooleanValStruct, BooleanVal)
TinyIntVal_is_null = _is_null_attr_factory(TinyIntValStruct, TinyIntVal)
SmallIntVal_is_null = _is_null_attr_factory(SmallIntValStruct, SmallIntVal)
IntVal_is_null = _is_null_attr_factory(IntValStruct, IntVal)
BigIntVal_is_null = _is_null_attr_factory(BigIntValStruct, BigIntVal)
FloatVal_is_null = _is_null_attr_factory(FloatValStruct, FloatVal)
DoubleVal_is_null = _is_null_attr_factory(DoubleValStruct, DoubleVal)
StringVal_is_null = _is_null_attr_factory(StringValStruct, StringVal)

# *Val.val
BooleanVal_val = _val_attr_factory(BooleanValStruct, BooleanVal, ntypes.int8)
TinyIntVal_val = _val_attr_factory(TinyIntValStruct, TinyIntVal, ntypes.int8)
SmallIntVal_val = _val_attr_factory(SmallIntValStruct, SmallIntVal, ntypes.int16)
IntVal_val = _val_attr_factory(IntValStruct, IntVal, ntypes.int32)
BigIntVal_val = _val_attr_factory(BigIntValStruct, BigIntVal, ntypes.int64)
FloatVal_val = _val_attr_factory(FloatValStruct, FloatVal, ntypes.float32)
DoubleVal_val = _val_attr_factory(DoubleValStruct, DoubleVal, ntypes.float64)

@register_attribute
@impl_attribute(StringVal, "len", ntypes.int32)
def StringVal_len(context, builder, typ, value):
    """StringVal::len"""
    iv = StringValStruct(context, builder, value=value)
    return iv.len

@register_attribute
@impl_attribute(StringVal, "ptr", ntypes.CPointer(ntypes.uint8))
def StringVal_ptr(context, builder, typ, value):
    """StringVal::ptr"""
    iv = StringValStruct(context, builder, value=value)
    return iv.ptr


# impl "builtins"

@register_function
@implement('is', AnyVal, ntypes.none)
def is_none_impl(context, builder, sig, args):
    [x, y] = args
    val = AnyValStruct(context, builder, value=x)
    return val.is_null

@register_function
@implement(ntypes.len_type, StringVal)
def len_stringval_impl(context, builder, sig, args):
    [s] = args
    val = StringValStruct(context, builder, value=s)
    return val.len

@register_function
@implement("==", ntypes.CPointer(ntypes.uint8), ntypes.CPointer(ntypes.uint8))
def eq_ptr_impl(context, builder, sig, args):
    [p1, p2] = args
    return builder.icmp(lc.ICMP_EQ, p1, p2)

@register_function
@implement("==", StringVal, StringVal)
def eq_stringval(context, builder, sig, args):
    module = cgutils.get_module(builder)
    precomp_func = context._get_precompiled_function("EqStringValImpl")
    func = module.get_or_insert_function(precomp_func.type.pointee, precomp_func.name)
    [s1, s2] = args
    cs1 = _conv_numba_struct_to_clang(builder, s1, func.args[0].type)
    cs2 = _conv_numba_struct_to_clang(builder, s2, func.args[1].type)
    result = builder.call(func, [cs1, cs2])
    return result # ret bool so no need to raise type

@register_function
@implement("!=", StringVal, StringVal)
def neq_stringval(context, builder, sig, args):
    eq = eq_stringval(context, builder, sig, args)
    neq = builder.xor(lc.Constant.int(lc.Type.int(1), 1), eq)
    return neq

@register_function
@implement("getitem", StringVal, ntypes.intc)
def getitem_stringval(context, builder, sig, args):
    module = cgutils.get_module(builder)
    precomp_func = context._get_precompiled_function("GetItemStringValImpl")
    func = module.get_or_insert_function(precomp_func.type.pointee, precomp_func.name)
    [s, i] = args
    cs = _conv_numba_struct_to_clang(builder, s, func.args[0].type)
    result = builder.call(func, [cs, i])
    return raise_return_type(context, builder, StringVal, result)

@register_function
@implement("+", StringVal, StringVal)
def add_stringval(context, builder, sig, args):
    module = cgutils.get_module(builder)
    precomp_func = context._get_precompiled_function("AddStringValImpl")
    func = module.get_or_insert_function(precomp_func.type.pointee, precomp_func.name)
    fnctx_arg = context.get_arguments(cgutils.get_function(builder))[0]
    cfnctx_arg = builder.bitcast(fnctx_arg, func.args[0].type)
    [s1, s2] = args
    cs1 = _conv_numba_struct_to_clang(builder, s1, func.args[1].type)
    cs2 = _conv_numba_struct_to_clang(builder, s2, func.args[2].type)
    result = builder.call(func, [cfnctx_arg, cs1, cs2])
    return raise_return_type(context, builder, StringVal, result)


TYPE_LAYOUT = {
    AnyVal: AnyValStruct,
    BooleanVal: BooleanValStruct,
    TinyIntVal: TinyIntValStruct,
    SmallIntVal: SmallIntValStruct,
    IntVal: IntValStruct,
    BigIntVal: BigIntValStruct,
    FloatVal: FloatValStruct,
    DoubleVal: DoubleValStruct,
    StringVal: StringValStruct,
}


class ImpalaTargetContext(BaseContext):
    _impala_types = (AnyVal, BooleanVal, TinyIntVal, SmallIntVal, IntVal,
		     BigIntVal, FloatVal, DoubleVal, StringVal)

    def init(self):
	self.tm = le.TargetMachine.new()

	# insert registered impls
	self.insert_func_defn(registry.functions)
	self.insert_attr_defn(registry.attributes)
	self.insert_func_defn(stringimpl.registry.functions)
	self.insert_attr_defn(stringimpl.registry.attributes)

	self.optimizer = self.build_pass_manager()
	self._load_precompiled()

	# once per context
	self._fnctximpltype = lc.Type.opaque("FunctionContextImpl")
	fnctxbody = [lc.Type.pointer(self._fnctximpltype)]
	self._fnctxtype = lc.Type.struct(fnctxbody,
					 name="class.impala_udf::FunctionContext")

    def _get_precompiled_function(self, name):
	fns = [fn for fn in self.precompiled_module.functions if name in fn.name]
	assert len(fns) == 1
	return fns[0]

    def _load_precompiled(self):
	binary_data = pkgutil.get_data("impala.udf", "precompiled/impala-precompiled.bc")
	self.precompiled_module = lc.Module.from_bitcode(binary_data)

    def cast(self, builder, val, fromty, toty):
	if fromty not in self._impala_types and toty not in self._impala_types:
	    return super(ImpalaTargetContext, self).cast(builder, val, fromty, toty)

	if fromty == toty:
	    return val

	# handle NULLs and Nones
	if fromty == ntypes.none and toty in self._impala_types:
	    iv = TYPE_LAYOUT[toty](self, builder)
	    _set_is_null(builder, iv, cgutils.true_bit)
	    return iv._getvalue()
	if fromty in self._impala_types and toty == AnyVal:
	    iv1 = TYPE_LAYOUT[fromty](self, builder, value=val)
	    is_null = _get_is_null(builder, iv1)
	    iv2 = AnyValStruct(self, builder)
	    # this is equiv to _set_is_null, but changes the GEP bc of AnyVal's structure
	    byte = builder.zext(is_null, lc.Type.int(8))
	    builder.store(byte, builder.gep(iv2._getpointer(),
		    [lc.Constant.int(lc.Type.int(32), 0)] * 2, inbounds=True))
	    return iv2._getvalue()

	if fromty == BooleanVal:
	    v = BooleanValStruct(self, builder, val)
	    return self.cast(builder, v.val, ntypes.boolean, toty)
	if fromty == TinyIntVal:
	    v = TinyIntValStruct(self, builder, val)
	    return self.cast(builder, v.val, ntypes.int8, toty)
	if fromty == SmallIntVal:
	    v = SmallIntValStruct(self, builder, val)
	    return self.cast(builder, v.val, ntypes.int16, toty)
	if fromty == IntVal:
	    v = IntValStruct(self, builder, val)
	    return self.cast(builder, v.val, ntypes.int32, toty)
	if fromty == BigIntVal:
	    v = BigIntValStruct(self, builder, val)
	    return self.cast(builder, v.val, ntypes.int64, toty)
	if fromty == FloatVal:
	    v = FloatValStruct(self, builder, val)
	    return self.cast(builder, v.val, ntypes.float32, toty)
	if fromty == DoubleVal:
	    v = DoubleValStruct(self, builder, val)
	    return self.cast(builder, v.val, ntypes.float64, toty)

	# no way fromty is a *Val starting here
	if toty == BooleanVal:
	    val = super(ImpalaTargetContext, self).cast(builder, val, fromty, ntypes.int8)
	    return BooleanVal_ctor(self, builder, None, [val])
	if toty == TinyIntVal:
	    val = super(ImpalaTargetContext, self).cast(builder, val, fromty, ntypes.int8)
	    return TinyIntVal_ctor(self, builder, None, [val])
	if toty == SmallIntVal:
	    val = super(ImpalaTargetContext, self).cast(builder, val, fromty, ntypes.int16)
	    return SmallIntVal_ctor(self, builder, None, [val])
	if toty == IntVal:
	    val = super(ImpalaTargetContext, self).cast(builder, val, fromty, ntypes.int32)
	    return IntVal_ctor(self, builder, None, [val])
	if toty == BigIntVal:
	    val = super(ImpalaTargetContext, self).cast(builder, val, fromty, ntypes.int64)
	    return BigIntVal_ctor(self, builder, None, [val])
	if toty == FloatVal:
	    val = super(ImpalaTargetContext, self).cast(builder, val, fromty, ntypes.float32)
	    return FloatVal_ctor(self, builder, None, [val])
	if toty == DoubleVal:
	    val = super(ImpalaTargetContext, self).cast(builder, val, fromty, ntypes.float64)
	    return DoubleVal_ctor(self, builder, None, [val])
	if toty == StringVal:
	    return StringVal_ctor(self, builder, None, [val])

	return super(ImpalaTargetContext, self).cast(builder, val, fromty, toty)

    def get_constant_string(self, builder, ty, val):
	assert ty == ntypes.string
	literal = lc.Constant.stringz(val)
	gv = cgutils.get_module(builder).add_global_variable(literal.type, 'str_literal')
	gv.linkage = lc.LINKAGE_PRIVATE
	gv.initializer = literal
	gv.global_constant = True
	# gep gets pointer to first element of the constant byte array
	return gv.gep([lc.Constant.int(lc.Type.int(32), 0)] * 2)

    def get_constant_struct(self, builder, ty, val):
	# override for converting literals to *Vals, incl. None
	if ty in self._impala_types and val is None:
	    iv = TYPE_LAYOUT[ty](self, builder)
	    _set_is_null(builder, iv, cgutils.true_bit)
	    return iv._getvalue()
	elif ty == BooleanVal:
	    const = lc.Constant.int(lc.Type.int(8), val)
	    return BooleanVal_ctor(self, builder, None, [const])
	elif ty == TinyIntVal:
	    const = lc.Constant.int(lc.Type.int(8), val)
	    return TinyIntVal_ctor(self, builder, None, [const])
	elif ty == SmallIntVal:
	    const = lc.Constant.int(lc.Type.int(16), val)
	    return SmallIntVal_ctor(self, builder, None, [const])
	elif ty == IntVal:
	    const = lc.Constant.int(lc.Type.int(32), val)
	    return IntVal_ctor(self, builder, None, [const])
	elif ty == BigIntVal:
	    const = lc.Constant.int(lc.Type.int(64), val)
	    return BigIntVal_ctor(self, builder, None, [const])
	elif ty == FloatVal:
	    const = lc.Constant.real(lc.Type.float(), val)
	    return FloatVal_ctor(self, builder, None, [const])
	elif ty == DoubleVal:
	    const = lc.Constant.real(lc.Type.double(), val)
	    return DoubleVal_ctor(self, builder, None, [const])
	elif ty == StringVal:
	    iv = StringValStruct(self, builder)
	    _set_is_null(builder, iv, cgutils.false_bit)
	    iv.len = lc.Constant.int(lc.Type.int(32), len(val))
	    iv.ptr = self.get_constant_string(builder, ntypes.string, val)
	    return iv._getvalue()
	else:
	    return super(ImpalaTargetContext, self).get_constant_struct(builder, ty, val)

    def get_data_type(self, ty):
	if ty in TYPE_LAYOUT:
	    return self.get_struct_type(TYPE_LAYOUT[ty])
	elif ty == FunctionContext:
	    return lc.Type.pointer(self._fnctxtype)
	else:
	    return super(ImpalaTargetContext, self).get_data_type(ty)

    def get_array(self, builder, itemvals, itemtys):
	# only handle uniform type
	assert all(x == itemtys[0] for x in itemtys)
	if ty not in self._impala_types:
	    raise NotImplementedError("Arrays of non-Impala types not supported")


    def build_pass_manager(self):
	opt = 0 # let Impala optimize
	# opt = 3 # optimize ourselves
	pms = lp.build_pass_managers(tm=self.tm, opt=opt, loop_vectorize=True,
				     fpm=False)
	return pms.pm

    def finalize(self, func, restype, argtypes):
	func.verify()
	func.linkage = lc.LINKAGE_INTERNAL

	module = func.module
	# Generate wrapper to adapt into Impala ABI
	abi = ABIHandling(self, func, restype, argtypes)
	wrapper = abi.build_wrapper("numba_udf." + func.name)
	module.verify()

	self.optimizer.run(module)
	return wrapper
