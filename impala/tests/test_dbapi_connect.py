# Copyright 2013 Cloudera Inc.
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

from __future__ import absolute_import, print_function

import os
import sys

if sys.version_info[:2] <= (2, 6):
    import unittest2 as unittest
else:
    import unittest

import pytest

from impala.dbapi import connect
from impala.util import _random_id
from impala.tests.util import ImpylaTestEnv, SocketTracker


ENV = ImpylaTestEnv()
DEFAULT_AUTH = True
DEFAULT_AUTH_ERROR = "Non-default authorization method"


class ImpalaConnectionTests(unittest.TestCase):

    table_prefix = _random_id(prefix='dbapi20test_')
    tablename = table_prefix + 'contests'

    def setUp(self):
        self.connection = None

    def tearDown(self):
        if self.connection:
            self.connection.close()

    def _execute_queries(self, con):
        ddl = """
            CREATE TABLE {0} (
              f1 INT,
              f2 INT)
        """.format(self.tablename)
        try:
            cur = con.cursor()
            cur.execute(ddl)
            con.commit()
            cur.execute('DROP TABLE {0}'.format(self.tablename))
            con.commit()
        except:
            raise

    def test_impala_nosasl_connect(self):
        self.connection = connect(ENV.host, ENV.port, timeout=5)
        self._execute_queries(self.connection)

    def test_hive_plain_connect(self):
        self.connection = connect(ENV.host, ENV.hive_port,
                                  auth_mechanism="PLAIN",
                                  timeout=5,
                                  user=ENV.hive_user,
                                  password="cloudera")
        self._execute_queries(self.connection)

    @pytest.mark.skipif(DEFAULT_AUTH, reason=DEFAULT_AUTH_ERROR)
    def test_impala_plain_connect(self):
        self.connection = connect(ENV.host, ENV.port, auth_mechanism="PLAIN",
                                  timeout=5,
                                  user=ENV.hive_user,
                                  password="cloudera")
        self._execute_queries(self.connection)

    @pytest.mark.skipif(DEFAULT_AUTH, reason=DEFAULT_AUTH_ERROR)
    def test_hive_nosasl_connect(self):
        self.connection = connect(ENV.host, ENV.hive_port, timeout=5)
        self._execute_queries(self.connection)

class ImpalaSocketTests(unittest.TestCase):

    def run_a_query(self):
        with connect(ENV.host, ENV.port) as connection:
            with connection.cursor() as cursor:
                cursor.execute('select 1 as a_number')
                return cursor.fetchall()

    def test_socket_leak(self):
        with SocketTracker() as sockets:
            # there should be no open sockets prior to running query
            assert len(sockets.open_sockets) == 0, 'Expected 0 open sockets, but saw {}'.format(
                sockets.open_sockets)
            # run a query!
            self.run_a_query()
            # the "run_query" method should have caused all sockets to close
            assert len(sockets.open_sockets) == 0, 'Expected 0 open sockets, but saw {}'.format(
                sockets.open_sockets)