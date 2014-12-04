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

from pytest import skip

# set up some special cmd line options for test running

def pytest_addoption(parser):
    parser.addoption('--udf', action='store_true', default=False,
                     help='Only run local, non-database UDF tests '
                          '(compilation)')
    parser.addoption('--dbapi-compliance', action='store_true', default=False,
                     help='Also run DB API 2.0 compliance tests')


def pytest_runtest_setup(item):
    if item.config.getvalue('udf') and not getattr(item.obj, 'udf', None):
        skip('only running non-database udf tests')
    if getattr(item.obj, 'dbapi_compliance', None) and not item.config.getvalue('dbapi_compliance'):
        skip('DB API compliance tests not requested')
