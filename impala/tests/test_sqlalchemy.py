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


def test_sqlalchemy_compilation():
    engine = create_engine('impala://localhost')
    metadata = MetaData(engine)
    # TODO: add other types to this table (e.g., functional.all_types)
    mytable = Table("mytable",
                    metadata,
                    Column('col1', STRING),
                    Column('col2', TINYINT),
                    Column('col3', INT),
                    Column('col4', DOUBLE),
                    impala_partition_by='HASH PARTITIONS 16',
                    impala_stored_as='KUDU',
                    impala_table_properties={
                        'kudu.table_name': 'my_kudu_table',
                        'kudu.master_addresses': 'kudu-master.example.com:7051'
                    })
    observed = str(CreateTable(mytable, bind=engine))
    expected = ('\nCREATE TABLE mytable (\n\tcol1 STRING, \n\tcol2 TINYINT, '
                '\n\tcol3 INT, \n\tcol4 DOUBLE\n)'
                '\nPARTITION BY HASH PARTITIONS 16\nSTORED AS KUDU\n'
                "TBLPROPERTIES ('kudu.table_name' = 'my_kudu_table', "
                "'kudu.master_addresses' = 'kudu-master.example.com:7051')\n\n")
    assert expected == observed
