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

from impala.error import (  # noqa
    Error, Warning, InterfaceError, DatabaseError, InternalError,
    OperationalError, ProgrammingError, IntegrityError, DataError,
    NotSupportedError)
from impala.util import warn_deprecate, warn_protocol_param
import impala.hiveserver2 as hs2


AUTH_MECHANISMS = ['NOSASL', 'PLAIN', 'GSSAPI', 'LDAP']


# PEP 249 module globals
apilevel = '2.0'
threadsafety = 1  # Threads may share the module, but not connections
paramstyle = 'pyformat'


def connect(host='localhost', port=21050, database=None, timeout=None,
            use_ssl=False, ca_cert=None, auth_mechanism='NOSASL', user=None,
            password=None, kerberos_service_name='impala', use_ldap=None,
            ldap_user=None, ldap_password=None, use_kerberos=None,
            protocol=None, krb_host=None, use_http_transport=False,
            http_path=''):
    """Get a connection to HiveServer2 (HS2).

    These options are largely compatible with the impala-shell command line
    arguments. See those docs for more information.

    Parameters
    ----------
    host : str
        The hostname for HS2. For Impala, this can be any of the `impalad`s.
    port : int, optional
        The port number for HS2. The Impala default is 21050. The Hive port is
        likely different.
    database : str, optional
        The default database. If `None`, the result is
        implementation-dependent.
    timeout : int, optional
        Connection timeout in seconds. Default is no timeout.
    use_ssl : bool, optional
        Enable SSL.
    ca_cert : str, optional
        Local path to the the third-party CA certificate. If SSL is enabled but
        the certificate is not specified, the server certificate will not be
        validated.
    auth_mechanism : {'NOSASL', 'PLAIN', 'GSSAPI', 'LDAP'}
        Specify the authentication mechanism. `'NOSASL'` for unsecured Impala.
        `'PLAIN'` for unsecured Hive (because Hive requires the SASL
        transport). `'GSSAPI'` for Kerberos and `'LDAP'` for Kerberos with
        LDAP.
    user : str, optional
        LDAP user, if applicable.
    password : str, optional
        LDAP password, if applicable.
    kerberos_service_name : str, optional
        Authenticate to a particular `impalad` service principal. Uses
        `'impala'` by default.
    use_ldap : bool, optional
        Specify `auth_mechanism='LDAP'` instead.

        .. deprecated:: 0.11.0
    ldap_user : str, optional
        Use `user` parameter instead.

        .. deprecated:: 0.11.0
    ldap_password : str, optional
        Use `password` parameter instead.

        .. deprecated:: 0.11.0
    use_kerberos : bool, optional
        Specify `auth_mechanism='GSSAPI'` instead.

        .. deprecated:: 0.11.0
    protocol : str, optional
        Do not use.  HiveServer2 is the only protocol currently supported.

        .. deprecated:: 0.11.0


    Returns
    -------
    HiveServer2Connection
        A `Connection` object (DB API 2.0-compliant).
    """
    # pylint: disable=too-many-locals
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

    if protocol is not None:
        if protocol.lower() == 'hiveserver2':
            warn_protocol_param()
        else:
            raise NotSupportedError(
                "'{0}' is not a supported protocol; only HiveServer2 is "
                "supported".format(protocol))

    service = hs2.connect(host=host, port=port,
                          timeout=timeout, use_ssl=use_ssl,
                          ca_cert=ca_cert, user=user, password=password,
                          kerberos_service_name=kerberos_service_name,
                          auth_mechanism=auth_mechanism, krb_host=krb_host,
                          use_http_transport=use_http_transport,
                          http_path=http_path)
    return hs2.HiveServer2Connection(service, default_db=database)


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
