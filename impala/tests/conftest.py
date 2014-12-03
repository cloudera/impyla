# Copyright 2014 Cloudera Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
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
import getpass

from pytest import fixture, importorskip, skip

# these are all environment variable-based; primarily for ImpalaContext


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
        sys.stderr.write(
            "IMPALA_PORT not set; using default HiveServer2 port 21050")
        return 21050


@fixture(scope='session')
def protocol():
    if 'IMPALA_PROTOCOL' in os.environ:
        return os.environ['IMPALA_PROTOCOL']
    else:
        sys.stderr.write(
            "IMPALA_PROTOCOL not set; using default 'hiveserver2'")
        return 'hiveserver2'


@fixture(scope='session')
def nn_host():
    if 'NAMENODE_HOST' in os.environ:
        return os.environ['NAMENODE_HOST']
    else:
        sys.stderr.write("NAMENODE_HOST not set; using None")
        return None


@fixture(scope='session')
def webhdfs_port():
    if 'WEBHDFS_PORT' in os.environ:
        return os.environ['WEBHDFS_PORT']
    else:
        sys.stderr.write("WEBHDFS_PORT not set; using default 50070")
        return 50070


@fixture(scope='session')
def hdfs_user():
    if 'HDFS_USER' in os.environ:
        return os.environ['HDFS_USER']
    else:
        user = getpass.getuser()
        sys.stderr.write("HDFS_USER not set; using '%s'" % user)
        return user


@fixture(scope='session')
def temp_hdfs_dir():
    if 'TEMP_HDFS_DIR' in os.environ:
        return os.environ['TEMP_HDFS_DIR']
    else:
        sys.stderr.write("TEMP_HDFS_DIR not set; using default in /tmp/...")
        return None


@fixture(scope='session')
def temp_db():
    if 'TEMP_DB' in os.environ:
        return os.environ['TEMP_DB']
    else:
        sys.stderr.write(
            "TEMP_DB not set; using default prefixed tmp_impyla...")
        return None


# main ImpalaContext fixture; pretty much everything else depends on this
# somehow


@fixture(scope='session')
def ic(request, temp_hdfs_dir, temp_db, nn_host, webhdfs_port, hdfs_user, host,
       port, protocol):
    """Provides an ImpalaContext"""
    from impala.context import ImpalaContext

    ctx = ImpalaContext(temp_dir=temp_hdfs_dir, temp_db=temp_db,
                        nn_host=nn_host,
                        webhdfs_port=webhdfs_port, hdfs_user=hdfs_user,
                        host=host,
                        port=port, protocol=protocol)

    def fin():
        ctx.close()

    request.addfinalizer(fin)
    return ctx


@fixture(scope='session')
def hdfs_client(ic):
    pywebhdfs = importorskip('pywebhdfs')
    if ic._nn_host is None:
        skip("NAMENODE_HOST not set; skipping...")
    from pywebhdfs.webhdfs import PyWebHdfsClient

    hdfs_client = PyWebHdfsClient(host=ic._nn_host, port=ic._webhdfs_port,
                                  user_name=ic._hdfs_user)
    return hdfs_client


@fixture(scope='session')
def cursor(ic):
    """Provides a DB API 2.0 Cursor object"""
    return ic._cursor


@fixture(scope='session')
def iris_data(ic):
    cursor = ic._cursor
    cursor.execute('USE %s' % ic._temp_db)
    cursor.execute("CREATE TABLE iris_data (sepal_length DOUBLE, "
                   "sepal_width DOUBLE, petal_length DOUBLE, "
                   "petal_width DOUBLE, label STRING) ROW FORMAT DELIMITED "
                   "FIELDS TERMINATED BY '\\t' STORED AS TEXTFILE")
    raw_data = pkgutil.get_data('impala.tests', 'data/iris.data')
    lines = filter(lambda x: x != '', raw_data.split('\n'))
    tuples = map(lambda x: tuple(x.split(',')), lines)
    sql_strings = ['(%s, %s, %s, %s, "%s")' % tup for tup in tuples]
    cursor.execute("INSERT INTO iris_data VALUES %s" % ', '.join(sql_strings))


@fixture(scope='session')
def small_data(ic):
    cursor = ic._cursor
    cursor.execute('USE %s' % ic._temp_db)
    cursor.execute("CREATE TABLE small_data (a INT, b DOUBLE, c STRING) "
                   "ROW FORMAT DELIMITED FIELDS TERMINATED BY '\\t' "
                   "STORED AS TEXTFILE")
    cursor.execute("INSERT INTO small_data VALUES (3, 2.718, 'foo'), "
                   "(777, 3.14, 'bar'), (1729, 1.0, 'baz')")
