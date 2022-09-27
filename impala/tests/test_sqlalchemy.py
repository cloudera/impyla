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
from sqlalchemy import Table, Column, select
from sqlalchemy.schema import MetaData, CreateTable

from impala.sqlalchemy import STRING, INT, DOUBLE, TINYINT, DATE, VARCHAR
from impala.tests.util import ImpylaTestEnv

TEST_ENV = ImpylaTestEnv()


def create_partitioned_test_table(engine):
    metadata = MetaData(engine)
    # TODO: add other types to this table (e.g., functional.all_types)
    return Table("mytable",
                    metadata,
                    Column('col1', STRING),
                    Column('col2', TINYINT),
                    Column('col3', INT),
                    Column('col4', DOUBLE),
                    Column('col5', DATE),
                    Column('col6', VARCHAR(10)),
                    impala_partitioned_by='(part_col STRING)',
                    impala_stored_as='PARQUET',
                    impala_table_properties={
                      'transactional': 'true',
                      'transactional_properties': 'insert_only'
                    })

def create_simple_test_table(engine):
  metadata = MetaData(engine)
  return Table("mytable",
               metadata,
               Column('col1', STRING),
               Column('col2', TINYINT),
               Column('col3', INT),
               Column('col4', DOUBLE)
               )

def create_test_engine(diealect):
    return create_engine('{0}://{1}:{2}'.format(diealect, TEST_ENV.host, TEST_ENV.port))

def test_sqlalchemy_impala_compilation():
    engine = create_test_engine("impala")
    observed = CreateTable(create_partitioned_test_table(engine), bind=engine)
    # The DATE column type of 'col5' will be replaced with TIMESTAMP.
    expected = ('\nCREATE TABLE mytable (\n\tcol1 STRING, \n\tcol2 TINYINT, '
                '\n\tcol3 INT, \n\tcol4 DOUBLE, \n\tcol5 TIMESTAMP, \n\tcol6 VARCHAR(10)\n)'
                '\nPARTITIONED BY (part_col STRING)\nSTORED AS PARQUET\n'
                "TBLPROPERTIES ('transactional' = 'true', "
                "'transactional_properties' = 'insert_only')\n\n")
    assert expected == str(observed)


def test_sqlalchemy_impala4_compilation():
    engine = create_test_engine("impala4")
    observed = CreateTable(create_partitioned_test_table(engine), bind=engine)
    # The DATE column type of 'col5' will be left as is.
    expected = ('\nCREATE TABLE mytable (\n\tcol1 STRING, \n\tcol2 TINYINT, '
                '\n\tcol3 INT, \n\tcol4 DOUBLE, \n\tcol5 DATE, \n\tcol6 VARCHAR(10)\n)'
                '\nPARTITIONED BY (part_col STRING)\nSTORED AS PARQUET\n'
                "TBLPROPERTIES ('transactional' = 'true', "
                "'transactional_properties' = 'insert_only')\n\n")
    assert expected == str(observed)

def test_sqlalchemy_multiinsert():
    engine = create_test_engine("impala4")
    table = create_simple_test_table(engine)
    # TODO: Creating a non partitioned table as I am not sure about how to insert to
    #       a partitioned table in SQL alchemy
    create_table_stmt = CreateTable(table, bind=engine)

    data = [
        {"col1": "a", "col2": 1, "col3": 1, "col4": 1.0},
        {"col1": "b", "col2": 2, "col3": 3, "col4": 2.0}
    ]
    insert_stmt = table.insert(data)
    expected_insert = 'INSERT INTO mytable (col1, col2, col3, col4) VALUES '\
        '(%(col1_m0)s, %(col2_m0)s, %(col3_m0)s, %(col4_m0)s), '\
        '(%(col1_m1)s, %(col2_m1)s, %(col3_m1)s, %(col4_m1)s)'
    assert expected_insert == str(insert_stmt)

    engine.execute(create_table_stmt)
    try:
        engine.execute(insert_stmt)
        result = engine.execute(select(table.c).order_by(table.c.col1)).fetchall()
        expected_result = [('a', 1, 1, 1.0), ('b', 2, 3, 2.0)]
        assert expected_result == result
    finally:
        table.drop()
