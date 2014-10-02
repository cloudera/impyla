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

import os
import pkgutil

import pytest
import pandas as pd

from impala.bdf import from_sql_query, from_sql_table, from_hdfs, from_pandas

small_data = pytest.mark.usefixtures('small_data')
iris_data = pytest.mark.usefixtures('iris_data')

@small_data
def test_from_sql_query(ic):
    bdf = from_sql_query(ic, 'SELECT a, c AS d FROM small_data')
    assert bdf.count() == 3
    df = bdf.collect()
    assert df.shape == (3, 2)
    assert tuple(df.columns) == ('a', 'd')
    assert tuple(df.a) == (3, 777, 1729)

@small_data
def test_from_sql_table(ic):
    bdf = from_sql_table(ic, 'small_data')
    assert bdf.count() == 3
    df = bdf.collect()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 3)

def test_from_hdfs(ic, hdfs_client):
    raw_data = pkgutil.get_data('impala.tests', 'data/iris.data')
    dir_ = os.path.join(ic._temp_dir, 'test_small_data_dir')
    file_ = os.path.join(dir_, 'iris.data')
    hdfs_client.create_file(file_.lstrip('/'), raw_data)
    schema = [('a', 'DOUBLE'), ('b', 'DOUBLE'), ('c', 'DOUBLE'),
              ('d', 'DOUBLE'), ('e', 'STRING')]
    bdf = from_hdfs(ic, dir_, schema)
    assert bdf.count() == 150
    df = bdf.collect()
    assert df.shape == (150, 5)

def test_from_pandas_in_query(ic):
    df1 = pd.DataFrame({'a': (1, 2, 5), 'b': ('foo', 'bar', 'pasta')})
    bdf = from_pandas(ic, df1, method='in_query')
    df2 = bdf.collect()
    assert tuple(df2.columns) == ('a', 'b')
    assert df2.shape == df1.shape
    assert all(df1 == df2)

def test_from_pandas_webhdfs(ic):
    df1 = pd.DataFrame({'a': (1, 2, 5), 'b': ('foo', 'bar', 'pasta')})
    path = os.path.join(ic._temp_dir, 'test_pandas_webhdfs_dir')
    bdf = from_pandas(ic, df1, method='webhdfs', path=path,
            hdfs_host=ic._nn_host, webhdfs_port=ic._webhdfs_port,
            hdfs_user=ic._hdfs_user)
    df2 = bdf.collect()
    assert tuple(df2.columns) == ('a', 'b')
    assert df2.shape == df1.shape
    assert all(df1 == df2)
