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

from sqlalchemy.engine import create_engine
from sqlalchemy import Table, Column
from sqlalchemy.schema import MetaData, CreateTable

from impala.sqlalchemy import STRING, INT, DOUBLE, TINYINT

def table_metadata_from_ddl_template(con, ddl, table_name):
    """
    Helper for loading table metadata from ddl create table.
    """
    cur = con.cursor()
    cur.execute(ddl.format(table=table_name))
    cur.close()
    engine = create_engine('impala://', creator=lambda x: con)
    metadata = MetaData()
    return Table(table_name, metadata, autoload=True, autoload_with=engine)

def test_no_partitions_no_indexes(con):
    """
    Assert that table with no partitions contains no indices.
    """
    ddl = 'CREATE TABLE {table} (a STRING)'
    table = table_metadata_from_ddl_template(con, ddl, 'no_partitions')
    assert len(table.indexes) == 0

def test_one_partitions_indexes(con):
    """
    Assert that table with one partition has one index with one column.
    """
    ddl = 'CREATE TABLE {table} (a STRING) PARTITIONED BY (b INT);'
    table = table_metadata_from_ddl_template(con, ddl, 'one_partition')
    assert len(table.indexes) == 1
    assert str(list(table.indexes)[0].columns) == "['one_partition.b']"

def test_two_partitions_indexes(con):
    """
    Assert that table with two partitions has one index with two columns.
    """
    ddl = 'CREATE TABLE {table} (a STRING) PARTITIONED BY (b INT, c INT);'
    table = table_metadata_from_ddl_template(con, ddl, 'two_partitions')
    assert len(table.indexes) == 1
    assert str(list(table.indexes)[0].columns) == "['two_partitions.b', 'two_partitions.c']"

def test_sqlalchemy_compilation():
    engine = create_engine('impala://localhost')
    metadata = MetaData(engine)
    # TODO: add other types to this table (e.g., functional.all_types)
    mytable = Table("mytable",
                    metadata,
                    Column('col1', STRING),
                    Column('col2', TINYINT),
                    Column('col3', INT),
                    Column('col4', DOUBLE))
    observed = str(CreateTable(mytable, bind=engine))
    expected = ('\nCREATE TABLE mytable (\n\tcol1 STRING, \n\tcol2 TINYINT, '
                '\n\tcol3 INT, \n\tcol4 DOUBLE\n)\n\n')
    assert expected == observed
