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
import sys
import pkgutil

from pytest import fixture, skip

from impala.context import ImpalaContext

# set up some special cmd line options for test running

def pytest_addoption(parser):
    parser.addoption('--udf', action='store_true', default=False,
            help='Only run local, non-database UDF tests (compilation)')
    parser.addoption('--dbapi-compliance', action='store_true', default=False,
            help='Also run DB API 2.0 compliance tests')

def pytest_runtest_setup(item):
    if item.config.getvalue('udf') and not getattr(item.obj, 'udf', None):
        skip('only running non-database udf tests')
    if getattr(item.obj, 'dbapi_compliance', None) and not item.config.getvalue('dbapi_compliance'):
        skip('DB API compliance tests not requested')


# project-wide fixtures

@fixture(scope='session')
def host():
    if 'IMPALA_HOST' in os.environ:
        return os.environ['IMPALA_HOST']
    else:
        raise ValueError('IMPALA_HOST not set')

@fixture(scope='session')
def port():
    if 'IMPALA_PORT' in os.environ:
        return int(os.environ['IMPALA_PORT'])
    else:
        sys.stderr.write("IMPALA_PORT not set; using default HiveServer2 port 21050")
        return 21050

@fixture(scope='session')
def protocol():
    if 'IMPALA_PROTOCOL' in os.environ:
        return os.environ['IMPALA_PROTOCOL']
    else:
        sys.stderr.write("IMPALA_PROTOCOL not set; using default 'hiveserver2'")
        return 'hiveserver2'

@fixture(scope='session')
def nn_host():
    if 'NAMENODE_HOST' in os.environ:
        return os.environ['NAMENODE_HOST']
    else:
        sys.stderr.write("NAMENODE_HOST not set; using None")
        return None

@fixture(scope='session')
def ic(request, host, port, protocol):
    """Provides an ImpalaContext"""
    ctx = ImpalaContext(host=host, port=port, protocol=protocol)
    def fin():
        ctx.close()
    request.addfinalizer(fin)
    return ctx

@fixture(scope='session')
def cursor(ic):
    """Provides a DB API 2.0 Cursor object"""
    return ic._cursor

@fixture(scope='session')
def iris_data(ic):
    cursor = ic._cursor
    cursor.execute('USE %s' % ic._temp_db)
    cursor.execute("CREATE TABLE test_iris (sepal_length DOUBLE, "
                       "sepal_width DOUBLE, petal_length DOUBLE, "
                       "petal_width DOUBLE, label STRING) ROW FORMAT DELIMITED "
                       "FIELDS TERMINATED BY '\\t' STORED AS TEXTFILE")
    raw_data = pkgutil.get_data('impala.tests', 'data/iris.data')
    lines = filter(lambda x: x != '', raw_data.split('\n'))
    tuples = map(lambda x: tuple(x.split(',')), lines)
    sql_strings = ['(%s, %s, %s, %s, "%s")' % tup for tup in tuples]
    cursor.execute("INSERT INTO test_iris VALUES %s" % ', '.join(sql_strings))

@fixture(scope='session')
def small_data(ic):
    cursor = ic._cursor
    cursor.execute('USE %s' % ic._temp_db)
    cursor.execute("CREATE TABLE test_small (a INT, b DOUBLE, c STRING) "
                       "ROW FORMAT DELIMITED FIELDS TERMINATED BY '\\t' "
                       "STORED AS TEXTFILE")
    cursor.execute("INSERT INTO test_small VALUES (3, 2.718, 'foo'), "
                       "(777, 3.14, 'bar'), (1729, 1.0, 'baz')")
