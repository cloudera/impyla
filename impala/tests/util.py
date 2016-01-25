# Copyright 2015 Cloudera Inc.
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
import six


class ImpylaTestEnv(object):

    def __init__(self, host=None, port=None, auth_mech=None):
        if host is not None:
            self.host = host
        elif 'IMPYLA_TEST_HOST' in os.environ:
            self.host = os.environ['IMPYLA_TEST_HOST']
        else:
            sys.stderr.write("IMPYLA_TEST_HOST not set; using 'localhost'")
            self.host = 'localhost'

        if port is not None:
            self.port = port
        elif 'IMPYLA_TEST_PORT' in os.environ:
            self.port = int(os.environ['IMPYLA_TEST_PORT'])
        else:
            sys.stderr.write("IMPYLA_TEST_PORT not set; using 21050")
            self.port = 21050

        if auth_mech is not None:
            self.auth_mech = auth_mech
        elif 'IMPYLA_TEST_AUTH_MECH' in os.environ:
            self.auth_mech = os.environ['IMPYLA_TEST_AUTH_MECH']
        else:
            sys.stderr.write("IMPYLA_TEST_AUTH_MECH not set; using 'NOSASL'")
            self.auth_mech = 'NOSASL'

    def __repr__(self):
        kvs = ['{0}={1}'.format(k, v)
               for (k, v) in six.iteritems(self.__dict__)]
        return 'ImpylaTestEnv(\n    {0})'.format(',\n    '.join(kvs))
