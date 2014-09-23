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

"""Set Numba compiler rules for casting between types"""

from __future__ import absolute_import

import itertools

from numba import types as ntypes

from .types import (AnyVal, BooleanVal, TinyIntVal, SmallIntVal, IntVal,
                    BigIntVal, FloatVal, DoubleVal, StringVal)

def register_impala_numeric_type_conversions(base):
    impala_integral = (BooleanVal, TinyIntVal, SmallIntVal, IntVal, BigIntVal)
    impala_float = (FloatVal, DoubleVal)
    impala_all = impala_integral + impala_float
    numba_integral = (ntypes.boolean, ntypes.int8, ntypes.int16, ntypes.int32, ntypes.int64)
    numba_float = (ntypes.float32, ntypes.float64)
    numba_all = numba_integral + numba_float
    all_numeric = impala_all + numba_all

    # first, all Impala numeric types can cast to all others
    for a, b in itertools.product(impala_all, all_numeric):
        base.tm.set_unsafe_convert(a, b)
        base.tm.set_unsafe_convert(b, a)

    # match Numba-Impala types
    for a, b in zip(impala_all, numba_all):
        # base.tm.set_safe_convert(a, b)
        # base.tm.set_safe_convert(b, a)
        base.tm.set_unsafe_convert(a, b)
        base.tm.set_promote(b, a)

    # set up promotions
    for i in range(len(impala_integral)):
        for j in range(i + 1, len(numba_integral)):
            base.tm.set_promote(impala_integral[i], numba_integral[j])
            base.tm.set_promote(numba_integral[i], impala_integral[j])
            base.tm.set_promote(impala_integral[i], impala_integral[j])
    for i in range(len(impala_float)):
        for j in range(i + 1, len(numba_float)):
            base.tm.set_promote(impala_float[i], numba_float[j])
            base.tm.set_promote(numba_float[i], impala_float[j])
            base.tm.set_promote(impala_float[i], impala_float[j])

    # boolean safely promotes to everything
    for b in impala_all:
        base.tm.set_promote(ntypes.boolean, b)
    for b in all_numeric:
        base.tm.set_promote(BooleanVal, b)

    # int to float conversions
    for a in impala_integral[:-2]:
        base.tm.set_safe_convert(a, ntypes.float32)
        base.tm.set_safe_convert(a, ntypes.float64)
        base.tm.set_safe_convert(a, FloatVal)
        base.tm.set_safe_convert(a, DoubleVal)
    for a in numba_integral[:-2]:
        base.tm.set_safe_convert(a, FloatVal)
        base.tm.set_safe_convert(a, DoubleVal)
    base.tm.set_safe_convert(impala_integral[-2], ntypes.float64)
    base.tm.set_safe_convert(impala_integral[-2], DoubleVal)
    base.tm.set_safe_convert(numba_integral[-2], DoubleVal)

    # *Val to AnyVal (numeric)
    for a in impala_all:
        base.tm.set_unsafe_convert(a, AnyVal)

    for a in impala_all:
        base.tm.set_safe_convert(ntypes.none, a)

def register_impala_other_type_conversions(base):
    # base.tm.set_unsafe_convert(ntypes.CPointer(ntypes.uint8), ntypes.Dummy('void*'))
    base.tm.set_safe_convert(ntypes.string, StringVal)
    base.tm.set_unsafe_convert(StringVal, AnyVal)
    base.tm.set_safe_convert(ntypes.none, StringVal)
    base.tm.set_safe_convert(ntypes.none, AnyVal)