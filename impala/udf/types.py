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

"""Core Impala *Val types for Numba"""

from __future__ import absolute_import

from numba import types as ntypes
from numba.typing.templates import Registry


registry = Registry()
register_global = registry.register_global


class ImpalaValue(ntypes.Type):
    pass

# FunctionContext = ntypes.OpaqueType('class.impala_udf::FunctionContext')
FunctionContext = ntypes.Type('class.impala_udf::FunctionContext')

AnyVal = ImpalaValue('AnyVal')

BooleanVal = ImpalaValue('BooleanVal')
BooleanValType = ntypes.Dummy('BooleanValType')
register_global(BooleanVal, BooleanValType)

TinyIntVal = ImpalaValue('TinyIntVal')
TinyIntValType = ntypes.Dummy('TinyIntValType')
register_global(TinyIntVal, TinyIntValType)

SmallIntVal = ImpalaValue('SmallIntVal')
SmallIntValType = ntypes.Dummy('SmallIntValType')
register_global(SmallIntVal, SmallIntValType)

IntVal = ImpalaValue('IntVal')
IntValType = ntypes.Dummy('IntValType')
register_global(IntVal, IntValType)

BigIntVal = ImpalaValue('BigIntVal')
BigIntValType = ntypes.Dummy('BigIntValType')
register_global(BigIntVal, BigIntValType)

FloatVal = ImpalaValue('FloatVal')
FloatValType = ntypes.Dummy('FloatValType')
register_global(FloatVal, FloatValType)

DoubleVal = ImpalaValue('DoubleVal')
DoubleValType = ntypes.Dummy('DoubleValType')
register_global(DoubleVal, DoubleValType)

StringVal = ImpalaValue('StringVal')
StringValType = ntypes.Dummy('StringValType')
register_global(StringVal, StringValType)
