# -*- coding: UTF-8 -*-
# Copyright 2015 Cloudera Inc.
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

import datetime
import pytest
import sys
from pytest import fixture
from decimal import Decimal

@fixture(scope='module')
def decimal_table(cur):
    table_name = 'tmp_decimal_table'
    ddl = """CREATE TABLE {0} (
                 f1 decimal(10, 2),
                 f2 decimal(7, 5),
                 f3 decimal(38, 17))""".format(table_name)
    cur.execute(ddl)
    try:
        yield table_name
    finally:
        cur.execute("DROP TABLE {0}".format(table_name))


@pytest.mark.connect
def test_cursor_description_precision_scale(cur, decimal_table):
    # According to the DBAPI 2.0, these are the 7 fields of cursor.description
    # - name
    # - type_code
    # - display_size
    # - internal_size
    # - precision
    # - scale
    # - null_ok
    expected = [(10, 2),
                (7, 5),
                (38, 17)]
    cur.execute('select * from {0} limit 0'.format(decimal_table))
    observed = [(t[4], t[5]) for t in cur.description]
    for (exp, obs) in zip(expected, observed):
        assert exp == obs


@fixture(scope='module')
def decimal_table2(cur):
    table_name = 'tmp_decimal_table2'
    ddl = """CREATE TABLE {0} (val decimal(18, 9))""".format(table_name)
    cur.execute(ddl)
    cur.execute('''insert into {0}
                   values (cast(123456789.123456789 as decimal(18, 9))),
                          (cast(-123456789.123456789 as decimal(18, 9))),
                          (cast(0.000000001 as decimal(18, 9))),
                          (cast(-0.000000001 as decimal(18, 9))),
                          (cast(999999999.999999999 as decimal(18, 9))),
                          (cast(-999999999.999999999 as decimal(18, 9))),
                          (NULL)'''.format(table_name))
    try:
        yield table_name
    finally:
        cur.execute("DROP TABLE {0}".format(table_name))


def common_test_decimal(cur, decimal_table):
    """Read back a few decimal values in a wide range."""
    cur.execute('select val from {0} order by val'.format(decimal_table))
    results = cur.fetchall()
    assert results == [(Decimal('-999999999.999999999'),),
                       (Decimal('-123456789.123456789'),),
                       (Decimal('-0.000000001'),),
                       (Decimal('0.000000001'),),
                       (Decimal('123456789.123456789'),),
                       (Decimal('999999999.999999999'),),
                       (None,)]


@pytest.mark.connect
def test_decimal_basic(cur, decimal_table2):
    common_test_decimal(cur, decimal_table2)


@pytest.mark.connect
def test_decimal_no_string_conv(cur_no_string_conv, decimal_table2):
    common_test_decimal(cur_no_string_conv, decimal_table2)


@fixture(scope='module')
def date_table(cur):
    table_name = 'tmp_date_table'
    ddl = """CREATE TABLE {0} (d date)""".format(table_name)
    cur.execute(ddl)
    cur.execute('''insert into {0}
                   values (date "0001-01-01"), (date "1999-9-9")'''.format(table_name))
    try:
        yield table_name
    finally:
        cur.execute("DROP TABLE {0}".format(table_name))


def common_test_date(cur, date_table):
    """Read back a couple of data values in a wide range."""
    cur.execute('select d from {0} order by d'.format(date_table))
    results = cur.fetchall()
    assert results == [(datetime.date(1, 1, 1),), (datetime.date(1999, 9, 9),)]


@pytest.mark.connect
def test_date_basic(cur, date_table):
    common_test_date(cur, date_table)


@pytest.mark.connect
def test_date_no_string_conv(cur_no_string_conv, date_table):
    common_test_date(cur_no_string_conv, date_table)


@fixture(scope='module')
def timestamp_table(cur):
    table_name = 'tmp_timestamp_table'
    ddl = """CREATE TABLE {0} (ts timestamp)""".format(table_name)
    cur.execute(ddl)
    cur.execute('''insert into {0}
                   values (cast("1400-01-01 00:00:00" as timestamp)),
                          (cast("2014-06-23 13:30:51" as timestamp)),
                          (cast("2014-06-23 13:30:51.123" as timestamp)),
                          (cast("2014-06-23 13:30:51.123456" as timestamp)),
                          (cast("2014-06-23 13:30:51.123456789" as timestamp)),
                          (cast("9999-12-31 23:59:59" as timestamp))'''.format(table_name))
    try:
        yield table_name
    finally:
        cur.execute("DROP TABLE {0}".format(table_name))


def common_test_timestamp(cur, timestamp_table):
    """Read back a few timestamp values in a wide range."""
    cur.execute('select ts from {0} order by ts'.format(timestamp_table))
    results = cur.fetchall()
    assert results == [(datetime.datetime(1400, 1, 1, 0, 0),),
                       (datetime.datetime(2014, 6, 23, 13, 30, 51),),
                       (datetime.datetime(2014, 6, 23, 13, 30, 51, 123000),),
                       (datetime.datetime(2014, 6, 23, 13, 30, 51, 123456),),
                       (datetime.datetime(2014, 6, 23, 13, 30, 51, 123456),),
                       (datetime.datetime(9999, 12, 31, 23, 59, 59),)]


@pytest.mark.connect
def test_timestamp_basic(cur, timestamp_table):
    common_test_timestamp(cur, timestamp_table)


@pytest.mark.connect
def test_timestamp_no_string_conv(cur_no_string_conv, timestamp_table):
    common_test_timestamp(cur_no_string_conv, timestamp_table)


@pytest.mark.connect
def test_utf8_strings(cur):
    """Use STRING/VARCHAR/CHAR values  with multi byte unicode code points in a query."""
    cur.execute('select "引擎", cast("引擎" as varchar(6)), cast("引擎" as char(6))')
    result = cur.fetchone()
    assert result == ("引擎",) * 3

    # Tests returning STRING/VARCHAR/CHAR strings that are not valid UTF-8.
    # With Python 3 and Thrift 0.11.0 these tests needed TCLIService.thrift to be
    # modified. Syncing thrift files from Hive/Impala is likely to break these tests.
    cur.execute('select substr("引擎", 1, 4), cast("引擎" as varchar(4)), cast("引擎" as char(4))')
    result = cur.fetchone()
    assert result == (b"\xe5\xbc\x95\xe6",) * 3
    assert result[0].decode("UTF-8", "replace") == u"引�"

    cur.execute('select unhex("AA")')
    result = cur.fetchone()[0]
    assert result == b"\xaa"
    assert result.decode("UTF-8", "replace") == u"�"


@pytest.mark.connect
def test_string_conv(cur):
    cur.execute('select "Test string"')
    result = cur.fetchone()
    is_unicode = isinstance(result[0], str)


@pytest.mark.connect
def test_string_no_string_conv(cur_no_string_conv):
    cur = cur_no_string_conv
    cur.execute('select "Test string"')
    result = cur.fetchone()

    if sys.version_info[0] < 3:
        assert isinstance(result[0], str)
    else:
        assert isinstance(result[0], bytes)
