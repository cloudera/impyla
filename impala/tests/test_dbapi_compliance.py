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
from six.moves import zip

if sys.version_info[:2] <= (2, 6):
    import unittest2 as unittest
else:
    import unittest

import pytest

import impala.dbapi
from impala.tests import _dbapi20_tests
from impala.util import _random_id

if 'IMPALA_HOST' not in os.environ:
    raise ValueError("Please set IMPALA_HOST env variable")
if 'IMPALA_PORT' not in os.environ:
    print(("Using default Impala HiveServer2 port of 21050, or "
           "set IMPALA_PORT env variable"), file=sys.stderr)
if 'IMPALA_PROTOCOL' not in os.environ:
    print(("Using default Impala protocol of 'hiveserver2', or "
           "set IMPALA_PROTOCOL env variable"), file=sys.stderr)
if 'USE_KERBEROS' not in os.environ:
    print(("Set USE_KERBEROS=True if you want to use Kerberos"),
          file=sys.stderr)
host = os.environ['IMPALA_HOST']
port = int(os.environ.get('IMPALA_PORT', 21050))
protocol = os.environ.get('IMPALA_PROTOCOL', 'hiveserver2')
use_kerberos = os.environ.get('USE_KERBEROS', 'False').lower() == 'true'

connect_kw_args = {'host': host,
                   'port': port,
                   'protocol': protocol,
                   'use_kerberos': use_kerberos}

@pytest.mark.dbapi_compliance
class ImpalaDBAPI20Test(_dbapi20_tests.DatabaseAPI20Test):
    driver = impala.dbapi
    connect_kw_args = connect_kw_args

    table_prefix = _random_id(prefix='dbapi20test_')
    ddl1 = 'create table %sbooze (name string)' % table_prefix
    ddl2 = 'create table %sbarflys (name string)' % table_prefix
    xddl1 = 'drop table %sbooze' % table_prefix
    xddl2 = 'drop table %sbarflys' % table_prefix

    def test_nextset(self):
        pass

    def test_setoutputsize(self):
        pass

    @pytest.mark.skipif(protocol == 'beeswax', reason='Beeswax messes up NULL')
    def test_None(self):
        return super(ImpalaDBAPI20Test, self).test_None()


@pytest.mark.dbapi_compliance
@pytest.mark.skipif(protocol == 'beeswax',
                    reason='Beeswax does not support DECIMAL')
class ImpalaDecimalTests(unittest.TestCase):

    driver = impala.dbapi
    table_prefix = _random_id(prefix='dbapi20test_')
    tablename = table_prefix + 'decimaltests'

    def _connect(self):
        try:
            return self.driver.connect(**connect_kw_args)
        except AttributeError:
            self.fail("No connect method found in self.driver module")

    def setUp(self):
        ddl = """
            CREATE TABLE {0} (
              f1 decimal(10, 2),
              f2 decimal(7, 5),
              f3 decimal(38, 17))
        """.format(self.tablename)
        con = self._connect()
        try:
            cur = con.cursor()
            cur.execute(ddl)
            con.commit()
        except:
            raise
        finally:
            con.close()

    def tearDown(self):
        con = self._connect()
        try:
            cur = con.cursor()
            cur.execute('drop table {0}'.format(self.tablename))
            con.commit()
        except:
            raise
        finally:
            con.close()

    def test_cursor_description_precision_scale(self):
        # According to the DBAPI 2.0, these are the 7 fields of the cursor
        # description
        # - name
        # - type_code
        # - display_size
        # - internal_size
        # - precision
        # - scale
        # - null_ok
        cases = [
            (10, 2),
            (7, 5),
            (38, 17)
        ]

        con = self._connect()
        try:
            cur = con.cursor()
            cur.execute('select * from {0} limit 0'.format(self.tablename))

            desc = cur.description
            for (ex_p, ex_s), val in zip(cases, desc):
                assert val[4] == ex_p
                assert val[5] == ex_s

            con.commit()
        finally:
            con.close()
