# Copyright 2019 Cloudera Inc.
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

BIGGER_TABLE_NUM_ROWS = 100

@yield_fixture(scope='module')
def bigger_table(cur):
    table_name = 'tmp_bigger_table'
    ddl = """CREATE TABLE {0} (s string)
             STORED AS PARQUET""".format(table_name)
    cur.execute(ddl)
    dml = """INSERT INTO {0}
             VALUES {1}""".format(table_name,
                 ",".join(["('row{0}')".format(i) for i in xrange(BIGGER_TABLE_NUM_ROWS)]))
    # Disable codegen and expr rewrites so query runs faster.
    cur.execute("set disable_codegen=1")
    cur.execute("set enable_expr_rewrites=0")
    cur.execute(dml)
    try:
        yield table_name
    finally:
        cur.execute("DROP TABLE {0}".format(table_name))


def test_has_more_rows(cur, bigger_table):
    """Test that impyla correctly handles empty row batches returned with the
    hasMoreRows flag."""
    # Set the fetch timeout very low and add sleeps so that Impala will return
    # empty batches. Run on a single node with a single thread to make as predictable
    # as possible.
    cur.execute("set fetch_rows_timeout_ms=1")
    cur.execute("set num_nodes=1")
    cur.execute("set mt_dop=1")
    cur.execute("""select *
                   from {0}
                   where s != cast(sleep(2) as string)""".format(bigger_table))
    expected_rows = [("row{0}".format(i),) for i in xrange(BIGGER_TABLE_NUM_ROWS)]
    assert sorted(cur.fetchall()) == sorted(expected_rows)
