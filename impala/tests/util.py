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
import socket


identity = lambda x: x


def get_env_var(name, coercer, default):
    if name in os.environ:
        return coercer(os.environ[name])
    else:
        sys.stderr.write("{0} not set; using {1!r}".format(name, default))
        return default


class ImpylaTestEnv(object):

    def __init__(self, host=None, port=None, hive_port=None, auth_mech=None):
        if host is not None:
            self.host = host
        else:
            self.host = get_env_var('IMPYLA_TEST_HOST', identity, 'localhost')

        if port is not None:
            self.port = port
        else:
            self.port = get_env_var('IMPYLA_TEST_PORT', int, 21050)

        if hive_port is not None:
            self.hive_port = hive_port
        else:
            self.hive_port = get_env_var('IMPYLA_TEST_HIVE_PORT', int, 10000)

        self.hive_user = get_env_var('IMPYLA_TEST_HIVE_USER', identity,
                                     'cloudera')

        if auth_mech is not None:
            self.auth_mech = auth_mech
        else:
            self.auth_mech = get_env_var('IMPYLA_TEST_AUTH_MECH', identity,
                                         'NOSASL')

    def __repr__(self):
        kvs = ['{0}={1}'.format(k, v)
               for (k, v) in six.iteritems(self.__dict__)]
        return 'ImpylaTestEnv(\n    {0})'.format(',\n    '.join(kvs))

class SocketTracker(object):
    def __init__(self):
        self.open_sockets = set()
        self.socket_constructor = socket.socket.__init__
        self.socket_close = socket.socket.close

    def __enter__(self):
        def constructor(*args, **kwargs):
            self.open_sockets.add(args[0])
            return self.socket_constructor(*args, **kwargs)

        def close(*args, **kwargs):
            self.open_sockets.remove(args[0])
            return self.socket_close(*args, **kwargs)
        socket.socket.__init__ = constructor
        socket.socket.close = close
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        socket.socket.__init__ = self.socket_constructor
        socket.socket.close = self.socket_close