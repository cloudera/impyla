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

"""Define the Impala typing context for Numba"""

from __future__ import absolute_import

from numba import types as ntypes
from numba.typing import Context
from numba.typing.templates import (AttributeTemplate, ConcreteTemplate,
                                    Registry, signature)

from . import types
from . import typeconv
from . import stringdecl
from .types import (FunctionContext, AnyVal, BooleanVal, BooleanValType,
                    TinyIntVal, TinyIntValType, SmallIntVal, SmallIntValType,
                    IntVal, IntValType, BigIntVal, BigIntValType, FloatVal,
                    FloatValType, DoubleVal, DoubleValType, StringVal,
                    StringValType)


registry = Registry()
register_function = registry.register
register_attribute = registry.register_attr
register_global = registry.register_global


# *Val ctors

def _ctor_factory(Val, ValType, argty):
    class ValCtor(ConcreteTemplate):
        key = ValType
        cases = [signature(Val, argty)]
    return register_function(ValCtor)

BooleanValCtor = _ctor_factory(BooleanVal, BooleanValType, ntypes.int8)
TinyIntValCtor = _ctor_factory(TinyIntVal, TinyIntValType, ntypes.int8)
SmallIntValCtor = _ctor_factory(SmallIntVal, SmallIntValType, ntypes.int16)
IntValCtor = _ctor_factory(IntVal, IntValType, ntypes.int32)
BigIntValCtor = _ctor_factory(BigIntVal, BigIntValType, ntypes.int64)
FloatValCtor = _ctor_factory(FloatVal, FloatValType, ntypes.float32)
DoubleValCtor = _ctor_factory(DoubleVal, DoubleValType, ntypes.float64)
StringValCtor = _ctor_factory(StringVal, StringValType, ntypes.CPointer(ntypes.char))


# *Val attributes

def _attr_factory(Val, ValType, retty):
    class ValAttr(AttributeTemplate):
        key = Val

        def resolve_is_null(self, val):
            # *Val::is_null
            return ntypes.boolean

        def resolve_val(self, val):
            # *Val::val
            return retty
    return register_attribute(ValAttr)

BooleanValAttr = _attr_factory(BooleanVal, BooleanValType, ntypes.int8)
TinyIntValAttr = _attr_factory(TinyIntVal, TinyIntValType, ntypes.int8)
SmallIntValAttr = _attr_factory(SmallIntVal, SmallIntValType, ntypes.int16)
IntValAttr = _attr_factory(IntVal, IntValType, ntypes.int32)
BigIntValAttr = _attr_factory(BigIntVal, BigIntValType, ntypes.int64)
FloatValAttr = _attr_factory(FloatVal, FloatValType, ntypes.float32)
DoubleValAttr = _attr_factory(DoubleVal, DoubleValType, ntypes.float64)

@register_attribute
class StringValAttr(AttributeTemplate):
    key = StringVal

    def resolve_is_null(self, val):
        # StringVal::is_null
        return ntypes.boolean

    def resolve_len(self, val):
        # StringVal::len
        return ntypes.int32

    def resolve_ptr(self, val):
        # StringVal::ptr
        return ntypes.CPointer(ntypes.uint8)


# register "builtins"

@register_function
class LenStringVal(ConcreteTemplate):
    key = ntypes.len_type
    cases = [signature(ntypes.int32, StringVal)]


@register_function
class CmpOpEqPtr(ConcreteTemplate):
    key = '=='
    cases = [signature(ntypes.boolean, ntypes.CPointer(ntypes.uint8), ntypes.CPointer(ntypes.uint8))]


@register_function
class CmpOpEqStringVal(ConcreteTemplate):
    key = '=='
    cases = [signature(ntypes.boolean, StringVal, StringVal)]


@register_function
class CmpOpNEqStringVal(ConcreteTemplate):
    key = '!='
    cases = [signature(ntypes.boolean, StringVal, StringVal)]


@register_function
class BinOpIs(ConcreteTemplate):
    key = 'is'
    cases = [signature(ntypes.int8, AnyVal, ntypes.none)]


@register_function
class GetItemStringVal(ConcreteTemplate):
    key = "getitem"
    cases = [signature(StringVal, StringVal, ntypes.intc)]


@register_function
class BinOpAddStringVal(ConcreteTemplate):
    key = "+"
    cases = [signature(StringVal, StringVal, StringVal)]

def impala_typing_context():
    base = Context()

    typeconv.register_impala_numeric_type_conversions(base)
    typeconv.register_impala_other_type_conversions(base)

    base.install(types.registry)
    base.install(registry)
    base.install(stringdecl.registry)

    return base
