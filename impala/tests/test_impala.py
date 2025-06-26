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

def test_build_summary_table(tmp_db, cur, empty_table):
    """Test build_exec_summary function of impyla.
    """
    tmp_db_lower = tmp_db.lower()
    # Assert column Operator, #Host, #Inst, #Rows, Est. #Rows, Est. Peak Mem, and Detail.
    # Skip column Avg Time, Max Time, and Peak Mem.

    def skip_cols(row):
        assert len(row) == 10, row
        output = list(row)
        del output[7]
        del output[4]
        del output[3]
        return output

    def validate_summary_table(table, expected):
        for i in range(0, len(expected)):
            row = skip_cols(table[i])
            assert expected[i] == row, 'Expect {0} but found {1}'.format(
                str(expected[i]), str(row))

    query = """SELECT * FROM {0} a INNER JOIN {1} b ON (a.i = b.i)""".format(
        empty_table, empty_table)
    cur.execute(query)
    cur.fetchall()
    summary = cur.get_summary()
    output_dop_0 = list()
    cur.build_summary_table(summary, output_dop_0)
    assert len(output_dop_0) == 8, output_dop_0
    expected_dop_0 = [
        ['F02:ROOT', 1, 1, '', '', '4.00 MB', ''],
        ['04:EXCHANGE', 1, 1, '0', '0', '16.00 KB', 'UNPARTITIONED'],
        ['F00:EXCHANGE SENDER', 1, 1, '', '', '64.00 KB', ''],
        ['02:HASH JOIN', 1, 1, '0', '0', '1.94 MB', 'INNER JOIN, BROADCAST'],
        ['|--03:EXCHANGE', 1, 1, '0', '0', '16.00 KB', 'BROADCAST'],
        ['|  F01:EXCHANGE SENDER', 1, 1, '', '', '32.00 KB', ''],
        ['|  01:SCAN HDFS', 1, 1, '0', '0', '0 B',
         '{0}.{1} b'.format(tmp_db_lower, empty_table)],
        ['00:SCAN HDFS', 1, 1, '0', '0', '0 B',
         '{0}.{1} a'.format(tmp_db_lower, empty_table)],
    ]
    validate_summary_table(output_dop_0, expected_dop_0)

    cur.execute(query, configuration={'mt_dop': '2'})
    cur.fetchall()
    summary = cur.get_summary()
    output_dop_2 = list()
    cur.build_summary_table(summary, output_dop_2)
    assert len(output_dop_2) == 9, output_dop_2
    expected_dop_2 = [
        ['F02:ROOT', 1, 1, '', '', '4.00 MB', ''],
        ['04:EXCHANGE', 1, 1, '0', '0', '16.00 KB', 'UNPARTITIONED'],
        ['F00:EXCHANGE SENDER', 1, 1, '', '', '64.00 KB', ''],
        ['02:HASH JOIN', 1, 1, '0', '0', '0 B', 'INNER JOIN, BROADCAST'],
        ['|--F03:JOIN BUILD', 1, 1, '', '', '3.88 MB', ''],
        ['|  03:EXCHANGE', 1, 1, '0', '0', '16.00 KB', 'BROADCAST'],
        ['|  F01:EXCHANGE SENDER', 1, 1, '', '', '32.00 KB', ''],
        ['|  01:SCAN HDFS', 1, 1, '0', '0', '0 B',
         '{0}.{1} b'.format(tmp_db_lower, empty_table)],
        ['00:SCAN HDFS', 1, 1, '0', '0', '0 B',
         '{0}.{1} a'.format(tmp_db_lower, empty_table)],
    ]
    validate_summary_table(output_dop_2, expected_dop_2)
