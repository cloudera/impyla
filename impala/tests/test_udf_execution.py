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

from __future__ import absolute_import

import string

from impala.udf import udf, ship_udf
from impala.udf.types import (FunctionContext, BooleanVal, SmallIntVal, IntVal,
                              BigIntVal, StringVal)


def test_return_null(ic):
    @udf(IntVal(FunctionContext, IntVal))
    def return_null(context, a):
        return None

    ship_udf(ic, return_null, overwrite=True)
    ic._cursor.execute('SELECT %s.return_null(10)' % ic._temp_db)
    results = ic._cursor.fetchall()
    assert results[0][0] is None


def test_int_predicates(ic):
    @udf(BooleanVal(FunctionContext, IntVal))
    def int_predicate(context, a):
        if a > 10:
            return True
        else:
            return False

    ship_udf(ic, int_predicate, overwrite=True)
    ic._cursor.execute('SELECT %s.int_predicate(10)' % ic._temp_db)
    results = ic._cursor.fetchall()
    assert results[0][0] is False
    ic._cursor.execute('SELECT %s.int_predicate(11)' % ic._temp_db)
    results = ic._cursor.fetchall()
    assert results[0][0] is True


def test_numeric_literals(ic):
    @udf(BigIntVal(FunctionContext, SmallIntVal))
    def numeric_literals(context, a):
        if a is None:
            return 1729
        elif a < 0:
            return None
        elif a < 10:
            return a + 5
        else:
            return a * 2

    ship_udf(ic, numeric_literals, overwrite=True)
    ic._cursor.execute('SELECT %s.numeric_literals(NULL)' % ic._temp_db)
    results = ic._cursor.fetchall()
    assert results[0][0] == 1729
    ic._cursor.execute('SELECT %s.numeric_literals(-5)' % ic._temp_db)
    results = ic._cursor.fetchall()
    assert results[0][0] is None
    ic._cursor.execute('SELECT %s.numeric_literals(2)' % ic._temp_db)
    results = ic._cursor.fetchall()
    assert results[0][0] == 7
    ic._cursor.execute('SELECT %s.numeric_literals(12)' % ic._temp_db)
    results = ic._cursor.fetchall()
    assert results[0][0] == 24


def test_int_promotion(ic):
    @udf(BigIntVal(FunctionContext, IntVal))
    def int_promotion(context, x):
        return x + 1

    ship_udf(ic, int_promotion, overwrite=True)
    ic._cursor.execute('SELECT %s.int_promotion(2)' % ic._temp_db)
    results = ic._cursor.fetchall()
    assert results[0][0] == 3
    assert ic._cursor.description[0][1] == 'BIGINT'


# test StringVal fns

def test_return_string_literal(ic):
    @udf(StringVal(FunctionContext, StringVal))
    def return_string_literal(context, a):
        return "bar"

    ship_udf(ic, return_string_literal, overwrite=True)
    ic._cursor.execute('SELECT %s.return_string_literal("foo")' % ic._temp_db)
    results = ic._cursor.fetchall()
    assert results[0][0] == 'bar'


def test_return_two_str_literals(ic):
    @udf(StringVal(FunctionContext, IntVal))
    def return_two_str_literals(context, a):
        if a > 5:
            return "foo"
        else:
            return "bar"

    ship_udf(ic, return_two_str_literals, overwrite=True)
    ic._cursor.execute('SELECT %s.return_two_str_literals(2)' % ic._temp_db)
    results = ic._cursor.fetchall()
    assert results[0][0] == 'bar'
    ic._cursor.execute('SELECT %s.return_two_str_literals(20)' % ic._temp_db)
    results = ic._cursor.fetchall()
    assert results[0][0] == 'foo'


def test_return_empty_string(ic):
    @udf(StringVal(FunctionContext, StringVal))
    def return_empty_string(context, a):
        return ""

    ship_udf(ic, return_empty_string, overwrite=True)
    ic._cursor.execute('SELECT %s.return_empty_string("blah")' % ic._temp_db)
    results = ic._cursor.fetchall()
    assert results[0][0] == ''


def test_string_eq(ic):
    @udf(BooleanVal(FunctionContext, StringVal))
    def string_eq(context, a):
        if a == "foo":
            return True
        elif a == "bar":
            return False
        else:
            return None

    ship_udf(ic, string_eq, overwrite=True)
    ic._cursor.execute('SELECT %s.string_eq("foo")' % ic._temp_db)
    results = ic._cursor.fetchall()
    assert results[0][0] is True
    ic._cursor.execute('SELECT %s.string_eq("bar")' % ic._temp_db)
    results = ic._cursor.fetchall()
    assert results[0][0] is False
    ic._cursor.execute('SELECT %s.string_eq("baz")' % ic._temp_db)
    results = ic._cursor.fetchall()
    assert results[0][0] is None


def test_string_len(ic):
    @udf(IntVal(FunctionContext, StringVal))
    def string_len(context, a):
        return len(a)

    ship_udf(ic, string_len, overwrite=True)
    ic._cursor.execute(
        'SELECT %s.string_len("australopithecus")' % ic._temp_db)
    results = ic._cursor.fetchall()
    assert results[0][0] == 16


def test_string_split_comma(ic):
    @udf(StringVal(FunctionContext, StringVal))
    def string_split_comma(context, a):
        return string.split(a, ",")[1]

    ship_udf(ic, string_split_comma, overwrite=True)
    ic._cursor.execute('SELECT %s.string_split_comma("foo,bar")' % ic._temp_db)
    results = ic._cursor.fetchall()
    assert results[0][0] == 'bar'


def test_string_indexing(ic):
    @udf(StringVal(FunctionContext, StringVal, IntVal))
    def string_indexing(context, a, b):
        return a[b]

    ship_udf(ic, string_indexing, overwrite=True)
    ic._cursor.execute('SELECT %s.string_indexing("foo", 1)' % ic._temp_db)
    results = ic._cursor.fetchall()
    assert results[0][0] == 'o'


def test_string_index_concat(ic):
    @udf(StringVal(FunctionContext, StringVal))
    def string_index_concat(context, a):
        return a[0] + a[3]

    ship_udf(ic, string_index_concat, overwrite=True)
    ic._cursor.execute('SELECT %s.string_index_concat("money")' % ic._temp_db)
    results = ic._cursor.fetchall()
    assert results[0][0] == 'me'


def test_string_concat(ic):
    @udf(StringVal(FunctionContext, StringVal, StringVal))
    def string_concat(context, a, b):
        return a + b

    ship_udf(ic, string_concat, overwrite=True)
    ic._cursor.execute(
        'SELECT %s.string_concat("howdy ", "doody")' % ic._temp_db)
    results = ic._cursor.fetchall()
    assert results[0][0] == 'howdy doody'
