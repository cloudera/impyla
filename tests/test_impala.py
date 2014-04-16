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

import  unittest

# from numba import cffi_support
from numba import boolean, int32, int64

from impala.udf import udf
from impala.udf.types import (FunctionContext, BooleanVal, SmallIntVal, IntVal,
			      BigIntVal, StringVal)


class TestImpala(unittest.TestCase):

    def test_bool_literals(self):
	@udf(BooleanVal(FunctionContext, IntVal))
	def fn(context, a):
	    if a > 5:
		return True
	    else:
		return False

    def test_numeric_literals(self):
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

    def test_numba_to_impala_conv(self):
	@udf(BigIntVal(FunctionContext, int32))
	def fn(context, x):
	    return x + 1

    def test_impala_to_numba_conv(self):
	@udf(int64(FunctionContext, IntVal))
	def fn(context, x):
	    return x + 1

    @unittest.skip("passthrough numba bug #409")
    def test_numba_to_impala_pass_through(self):
	@udf(BigIntVal(FunctionContext, int32))
	def fn(context, x):
	    return x

    @unittest.skip("passthrough numba bug #409")
    def test_impala_to_numba_pass_through(self):
	@udf(int64(FunctionContext, IntVal))
	def fn(context, x):
	    return x

    def test_promotion(self):
	@udf(BigIntVal(FunctionContext, IntVal))
	def fn(context, x):
	    return x + 1

    def test_null(self):
	@udf(IntVal(FunctionContext, IntVal))
	def test_null(context, a):
	    return None

    @unittest.skip("cffi_support.ExternCFunction not yet committed to numba")
    def test_call_extern_c_fn(self):
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

    @unittest.skip("cffi_support.ExternCFunction not yet committed to numba")
    def test_call_extern_c_fn_twice(self):
	global memcmp
	memcmp = cffi_support.ExternCFunction('memcmp', 'int memcmp ( const uint8_t * ptr1, const uint8_t * ptr2, size_t num )')

	@udf(boolean(FunctionContext, StringVal, StringVal))
	def fn(context, a, b):
	    c = memcmp(a.ptr, a.ptr, a.len) == 0
	    d = memcmp(a.ptr, b.ptr, a.len) == 0
	    return c or d

    def test_return_two_str_literals(self):
	@udf(StringVal(FunctionContext, IntVal))
	def fn(context, a):
	    if a > 5:
		return "foo"
	    else:
		return "bar"

    def test_string_eq(self):
	@udf(BooleanVal(FunctionContext, StringVal))
	def fn(context, a):
	    if a == "foo":
		return True
	    elif a == "bar":
		return False
	    else:
		return None

    def test_return_string_literal(self):
	@udf(StringVal(FunctionContext, StringVal))
	def fn(context, a):
	    return "foo"

    def test_return_empty_string(self):
	@udf(StringVal(FunctionContext, StringVal))
	def fn(context, a):
	    return ""

    def test_string_len(self):
	@udf(IntVal(FunctionContext, StringVal))
	def fn(context, a):
	    return len(a)

    def test_string_concat(self):
	@udf(StringVal(FunctionContext, StringVal, StringVal))
	def fn(context, a, b):
	    return a + b

    def test_string_index_concat(self):
	@udf(StringVal(FunctionContext, StringVal))
	def fn(context, a):
	    return a[0] + a[3]

    def test_string_indexing(self):
	@udf(StringVal(FunctionContext, StringVal, IntVal))
	def fn(context, a, b):
	    return a[b]


if __name__ == '__main__':
    unittest.main(verbosity=2)
