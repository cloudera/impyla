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

import pytest
from pytest import yield_fixture


@yield_fixture(scope='module')
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
