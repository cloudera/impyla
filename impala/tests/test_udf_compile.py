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

import string

from numba import cffi_support
from numba import boolean, int32, int64
import pytest

from impala.udf import udf
from impala.udf.types import (FunctionContext, BooleanVal, SmallIntVal, IntVal,
                              BigIntVal, StringVal)

skipif = pytest.mark.skipif

def test_bool_literals():
    @udf(BooleanVal(FunctionContext, IntVal))
    def fn(context, a):
        if a > 5:
            return True
        else:
            return False

def test_numeric_literals():
    @udf(BigIntVal(FunctionContext, SmallIntVal))
    def fn(context, a):
        if a is None:
            return 1729
        elif a < 0:
            return None
        elif a < 10:
            return a + 5
        else:
            return a * 2

def test_numba_to_impala_conv():
    @udf(BigIntVal(FunctionContext, int32))
    def fn(context, x):
        return x + 1

def test_impala_to_numba_conv():
    @udf(int64(FunctionContext, IntVal))
    def fn(context, x):
        return x + 1

@skipif(True, reason="passthrough numba bug #409")
def test_numba_to_impala_pass_through():
    @udf(BigIntVal(FunctionContext, int32))
    def fn(context, x):
        return x

@skipif(True, reason="passthrough numba bug #409")
def test_impala_to_numba_pass_through():
    @udf(int64(FunctionContext, IntVal))
    def fn(context, x):
        return x

def test_promotion():
    @udf(BigIntVal(FunctionContext, IntVal))
    def fn(context, x):
        return x + 1

def test_null():
    @udf(IntVal(FunctionContext, IntVal))
    def fn(context, a):
        return None
    

@skipif(True, reason="cffi_support.ExternCFunction not yet committed to numba")
def test_call_extern_c_fn():
    global memcmp
    memcmp = cffi_support.ExternCFunction('memcmp', 'int memcmp ( const uint8_t * ptr1, const uint8_t * ptr2, size_t num )')
    
    @udf(BooleanVal(FunctionContext, StringVal, StringVal))
    def fn(context, a, b):
        if a.is_null != b.is_null:
            return False
        if a is None:
            return True
        if len(a) != b.len:
            return False
        if a.ptr == b.ptr:
            return True
        return memcmp(a.ptr, b.ptr, a.len) == 0

@skipif(True, reason="cffi_support.ExternCFunction not yet committed to numba")
def test_call_extern_c_fn_twice():
    global memcmp
    memcmp = cffi_support.ExternCFunction('memcmp', 'int memcmp ( const uint8_t * ptr1, const uint8_t * ptr2, size_t num )')
    
    @udf(boolean(FunctionContext, StringVal, StringVal))
    def fn(context, a, b):
        c = memcmp(a.ptr, a.ptr, a.len) == 0
        d = memcmp(a.ptr, b.ptr, a.len) == 0
        return c or d

def test_return_two_str_literals():
    @udf(StringVal(FunctionContext, IntVal))
    def fn(context, a):
        if a > 5:
            return "foo"
        else:
            return "bar"

def test_string_eq():
    @udf(BooleanVal(FunctionContext, StringVal))
    def fn(context, a):
        if a == "foo":
            return True
        elif a == "bar":
            return False
        else:
            return None

def test_return_string_literal():
    @udf(StringVal(FunctionContext, StringVal))
    def fn(context, a):
        return "foo"

def test_return_empty_string():
    @udf(StringVal(FunctionContext, StringVal))
    def fn(context, a):
        return ""

def test_string_len():
    @udf(IntVal(FunctionContext, StringVal))
    def fn(context, a):
        return len(a)

def test_string_concat():
    @udf(StringVal(FunctionContext, StringVal, StringVal))
    def fn(context, a, b):
        return a + b

def test_string_index_concat():
    @udf(StringVal(FunctionContext, StringVal))
    def fn(context, a):
        return a[0] + a[3]

def test_string_indexing():
    @udf(StringVal(FunctionContext, StringVal, IntVal))
    def fn(context, a, b):
        return a[b]

def test_string_array():
    @udf(StringVal(FunctionContext, StringVal))
    def fn(context, a):
        b = "foo"
        c = "bar"
        d = [b, c]
        return d[1]

def test_string_split():
    @udf(StringVal(FunctionContext, StringVal))
    def fn(context, a):
        return string.split(a, ",")[0]
