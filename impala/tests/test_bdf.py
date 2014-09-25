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

import pandas as pd

import pytest

example_tables = pytest.mark.usefixtures('iris_data', 'small_data')

def test_from_sql_query(ic):
    pass

@example_tables
def test_from_sql_table(ic):
    bdf = ic.from_sql_table('test_small')
    assert bdf.count() == 3
    df = bdf.collect()
    assert df.shape[0] == 3
    assert isinstance(df, pd.DataFrame)

def test_from_hdfs(ic):
    pass

def test_from_pandas(ic):
    pass
