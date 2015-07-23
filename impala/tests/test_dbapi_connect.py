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


if 'IMPALA_HOST' not in os.environ:
    raise ValueError("Please set IMPALA_HOST env variable")
host = os.environ['IMPALA_HOST']
impala_port = 21050
impala_beeswax_port = 21000
hive_port = 10000
hive_beeswax_port = 8002

NO_BEESWAX = False
NO_BEESWAX_REASON = "Beeswax tests are disabled"

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

    @pytest.mark.skipif(NO_BEESWAX, reason=NO_BEESWAX_REASON)
    def test_impala_noldap_beeswax_connect(self):
        self.connection = connect(host, impala_beeswax_port,
                                  protocol="beeswax", use_ldap=False, timeout=5)
        self._execute_queries(self.connection)

    def test_impala_noldap_hiveserver2_connect(self):
        self.connection = connect(host, impala_port,
                                  protocol="hiveserver2", use_ldap=False, timeout=5)
        self._execute_queries(self.connection)

    @pytest.mark.skipif(NO_BEESWAX, reason=NO_BEESWAX_REASON)
    def test_hive_noldap_beeswax_connect(self):
        self.connection = connect(host, hive_beeswax_port,
                                  protocol="beeswax", use_ldap=False, timeout=5)
        self._execute_queries(self.connection)

    def test_hive_noldap_hiveserver2_connect(self):
        self.connection = connect(host, hive_port,
                                  protocol="hiveserver2", use_ldap=False, timeout=5)
        self._execute_queries(self.connection)

    @pytest.mark.skipif(NO_BEESWAX, reason=NO_BEESWAX_REASON)
    def test_impala_ldap_beeswax_connect(self):
        self.connection = connect(host, impala_beeswax_port,
                                  protocol="beeswax", use_ldap=True, timeout=5,
                                  ldap_user="cloudera", ldap_password="cloudera")
        self._execute_queries(self.connection)

    def test_impala_ldap_hiveserver2_connect(self):
        self.connection = connect(host, impala_port,
                                  protocol="hiveserver2", use_ldap=True, timeout=5,
                                  ldap_user="cloudera", ldap_password="cloudera")
        self._execute_queries(self.connection)

    @pytest.mark.skipif(NO_BEESWAX, reason=NO_BEESWAX_REASON)
    def test_hive_ldap_beeswax_connect(self):
        self.connection = connect(host, hive_beeswax_port,
                                  protocol="beeswax", use_ldap=True, timeout=5,
                                  ldap_user="cloudera", ldap_password="cloudera")
        self._execute_queries(self.connection)

    def test_hive_ldap_hiveserver2_connect(self):
        self.connection = connect(host, hive_port,
                                  protocol="hiveserver2", use_ldap=True, timeout=5,
                                  ldap_user="cloudera", ldap_password="cloudera")
        self._execute_queries(self.connection)
