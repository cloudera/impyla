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
import sys

import pytest
from impala.compat import _xrange as xrange
from pytest import fixture

BIGGER_TABLE_NUM_ROWS = 100

@fixture(scope='module')
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

@fixture(scope='function')
def empty_table(cur):
    table_name = 'tmp_empty_table'
    ddl = """CREATE TABLE {0} (i int)""".format(table_name)
    cur.execute(ddl)
    try:
        yield table_name
    finally:
        cur.execute("DROP TABLE {0}".format(table_name))

def test_dml_rowcount(cur, empty_table):
    """Test that impyla correctly sets rowcount for insert statements."""
    dml = """INSERT INTO {0}
	     VALUES (0)""".format(empty_table)
    cur.execute(dml)
    assert cur.rowcount == 1

def test_row_count_in_empty_result(cur, empty_table):
    """Test that impyla correctly sets rowcount when 0 rows are returned.
       This case is missing from dbapi2 compliance tests.
    """
    query = """SELECT * FROM {0}""".format(empty_table)
    cur.execute(query)
    cur.fetchall()
    assert cur.rowcount == 0

def test_get_log(cur, empty_table):
    """Test that impyla can return the result of get_log after the query
       is closed.
    """
    query = """SELECT * FROM {0}""".format(empty_table)
    for mt_dop in ['0', '2']:
        cur.execute(query, configuration={'mt_dop': mt_dop})
        cur.fetchall()
        validate_log(cur)
        cur.close_operation()

def validate_log(cur):
    # The query should be closed at this point.
    assert not cur._last_operation_active
    log = cur.get_log()
    assert "100% Complete" in log
    # Also check that summary and runtime profile are available
    summary = cur.get_summary()
    assert summary is not None
    for node in summary.nodes:
        assert hasattr(node, 'node_id')
        assert hasattr(node, 'fragment_idx')
        assert hasattr(node, 'label')
        assert hasattr(node, 'label_detail')
        assert hasattr(node, 'num_children')
        assert hasattr(node, 'estimated_stats')
        assert hasattr(node, 'exec_stats')
        assert hasattr(node, 'is_broadcast')
        assert hasattr(node, 'num_hosts')
        assert node.num_hosts > 0
        assert len(node.exec_stats) >= node.num_hosts
    profile = cur.get_profile()
    assert profile is not None
