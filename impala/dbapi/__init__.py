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
from impala.util import warn_deprecate_hs2, warn_deprecate


AUTH_MECHANISMS = ['NOSASL', 'PLAIN', 'GSSAPI', 'LDAP']


# PEP 249 module globals
apilevel = '2.0'
threadsafety = 1  # Threads may share the module, but not connections
paramstyle = 'pyformat'

def connect(host='localhost', port=21050, protocol='hiveserver2', database=None,
            timeout=45, use_ssl=False, ca_cert=None,
            auth_mechanism='NOSASL', user=None, password=None,
            kerberos_service_name='impala', use_ldap=None, ldap_user=None,
            ldap_password=None, use_kerberos=None):
    if use_kerberos is not None:
        warn_deprecate('use_kerberos', 'auth_mechanism="GSSAPI"')
        if use_kerberos:
            auth_mechanism = 'GSSAPI'

    if use_ldap is not None:
        warn_deprecate('use_ldap', 'auth_mechanism="LDAP"')
        if use_ldap:
            auth_mechanism = 'LDAP'

    if auth_mechanism:
        auth_mechanism = auth_mechanism.upper()
    else:
        auth_mechanism = 'NOSASL'

    if auth_mechanism not in AUTH_MECHANISMS:
        raise NotSupportedError(
            'Unsupported authentication mechanism: {0}'.format(auth_mechanism))

    if ldap_user is not None:
        warn_deprecate('ldap_user', 'user')
        user = ldap_user

    if ldap_password is not None:
        warn_deprecate('ldap_password', 'password')
        password = ldap_password

    # PEP 249
    if protocol.lower() == 'beeswax':
        warn_deprecate_hs2()
        service = connect_to_beeswax(host=host, port=port, timeout=timeout,
                                     use_ssl=use_ssl, ca_cert=ca_cert,
                                     user=user, password=password,
                                     kerberos_service_name=kerberos_service_name,
                                     auth_mechanism=auth_mechanism)
        return BeeswaxConnection(service, default_db=database)
    elif protocol.lower() == 'hiveserver2':
        service = connect_to_hiveserver2(host=host, port=port, timeout=timeout,
                                         use_ssl=use_ssl, ca_cert=ca_cert,
                                         user=user, password=password,
                                         kerberos_service_name=
                                             kerberos_service_name,
                                         auth_mechanism=auth_mechanism)
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
