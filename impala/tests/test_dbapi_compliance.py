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

import os
import sys
import unittest

import impala.dbapi
import _dbapi20_tests

if 'IMPALA_HOST' not in os.environ:
    raise ValueError("Please set IMPALA_HOST env variable")
if 'IMPALA_PORT' not in os.environ:
    print >>sys.stderr, "Using default Impala HS2 port of 21050, or set IMPALA_PORT env variable"
host = os.environ['IMPALA_HOST']
port = int(os.environ.get('IMPALA_PORT', 21050))

class ImpylaDBAPI20Test(_dbapi20_tests.DatabaseAPI20Test):
    driver = impala.dbapi
    connect_kw_args = {'host': host,
                       'port': port}
    table_prefix = 'dbapi20test_'
    ddl1 = 'create table %sbooze (name string)' % table_prefix
    ddl2 = 'create table %sbarflys (name string)' % table_prefix
    
    def test_nextset(self): pass
    def test_setoutputsize(self): pass


if __name__ == '__main__':
    unittest.main()