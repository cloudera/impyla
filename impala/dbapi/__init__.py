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

"""Implements the Python DB API 2.0 (PEP 249) for Impala"""

from __future__ import absolute_import

import six
import time
import datetime

from impala._rpc.hiveserver2 import connect_to_impala as connect_to_hiveserver2
from impala._rpc.beeswax import connect_to_impala as connect_to_beeswax
from impala.dbapi.hiveserver2 import HiveServer2Connection
from impala.dbapi.beeswax import BeeswaxConnection
from impala.error import (Error, Warning, InterfaceError, DatabaseError,
                          InternalError, OperationalError, ProgrammingError,
                          IntegrityError, DataError, NotSupportedError)

# PEP 249 module globals
apilevel = '2.0'
threadsafety = 1  # Threads may share the module, but not connections
paramstyle = 'pyformat'

def connect(host='localhost', port=21050, protocol='hiveserver2',
            database=None, timeout=45, use_ssl=False, ca_cert=None,
            use_ldap=False, ldap_user=None, ldap_password=None,
            use_kerberos=False, kerberos_service_name='impala',
            auth_mechanism=None):

    # Supported authentication mechanisms
    auth_mechanisms = ['NOSASL', 'PLAIN', 'GSSAPI', 'LDAP']
    if use_kerberos:
        if auth_mechanism and auth_mechanism.upper() != 'GSSAPI':
            raise ValueError("Kerberos requires authentication mechanism 'GSSAPI'")
        else:
            auth_mechanism = 'GSSAPI'

    if use_ldap:
        if auth_mechanism and auth_mechanism.upper() != 'LDAP':
            raise ValueError("LDAP requires authentication mechanism 'LDAP'")
        else:
            auth_mechanism = 'LDAP'

    # If not specified, authentication mechanism defaults to NOSASL
    if not auth_mechanism: auth_mechanism = 'NOSASL'

    if auth_mechanism.upper() not in auth_mechanisms:
        raise NotSupportedError('Unsupported authentication mechanism: %s' % mechanism)

    # PEP 249
    if protocol.lower() == 'beeswax':
        service = connect_to_beeswax(
            host, port, timeout, use_ssl, ca_cert, ldap_user,
            ldap_password, kerberos_service_name, auth_mechanism)
        return BeeswaxConnection(service, default_db=database)
    elif protocol.lower() == 'hiveserver2':
        service = connect_to_hiveserver2(
            host, port, timeout, use_ssl, ca_cert, ldap_user,
            ldap_password, kerberos_service_name, auth_mechanism)
        return HiveServer2Connection(service, default_db=database)
    else:
        raise NotSupportedError(
            "The specified protocol '%s' is not supported." % protocol)


class _DBAPITypeObject(object):
    # Compliance with Type Objects of PEP 249.

    def __init__(self, *values):
        self.values = values

    def __cmp__(self, other):
        if other in self.values:
            return 0
        else:
            return -1

    def __eq__(self, other):
        # py3 ignores __cmp__
        return other in self.values


STRING = _DBAPITypeObject('STRING')
BINARY = _DBAPITypeObject('BINARY')
NUMBER = _DBAPITypeObject('BOOLEAN', 'TINYINT', 'SMALLINT', 'INT', 'BIGINT',
                          'FLOAT', 'DOUBLE', 'DECIMAL')
DATETIME = _DBAPITypeObject('TIMESTAMP')
ROWID = _DBAPITypeObject()

Date = datetime.date
Time = datetime.time
Timestamp = datetime.datetime


def DateFromTicks(ticks):
    return Date(*time.localtime(ticks)[:3])


def TimeFromTicks(ticks):
    return Time(*time.localtime(ticks)[3:6])


def TimestampFromTicks(ticks):
    return Timestamp(*time.localtime(ticks)[:6])

if six.PY3:
    buffer = memoryview
Binary = buffer
