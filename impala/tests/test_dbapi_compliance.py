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

from __future__ import absolute_import

import os
import sys

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
    print >>sys.stderr, ("Using default Impala HiveServer2 port of 21050, or "
                         "set IMPALA_PORT env variable")
if 'IMPALA_PROTOCOL' not in os.environ:
    print >>sys.stderr, ("Using default Impala protocol of 'hiveserver2', or "
                         "set IMPALA_PROTOCOL env variable")
host = os.environ['IMPALA_HOST']
port = int(os.environ.get('IMPALA_PORT', 21050))
protocol = os.environ.get('IMPALA_PROTOCOL', 'hiveserver2')


@pytest.mark.dbapi_compliance
class ImpalaDBAPI20Test(_dbapi20_tests.DatabaseAPI20Test):
    driver = impala.dbapi
    connect_kw_args = {'host': host,
                       'port': port,
                       'protocol': protocol}
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
