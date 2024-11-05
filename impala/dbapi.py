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
from impala.util import (
    warn_deprecate, warn_protocol_param, warn_nontls_jwt)
import impala.hiveserver2 as hs2


AUTH_MECHANISMS = ['NOSASL', 'PLAIN', 'GSSAPI', 'LDAP', 'JWT']


# PEP 249 module globals
apilevel = '2.0'
threadsafety = 1  # Threads may share the module, but not connections
paramstyle = 'pyformat'


def connect(host='localhost', port=21050, database=None, timeout=None,
            use_ssl=False, ca_cert=None, auth_mechanism='NOSASL', user=None,
            password=None, kerberos_service_name='impala', use_ldap=None,
            ldap_user=None, ldap_password=None, use_kerberos=None,
            protocol=None, krb_host=None, use_http_transport=False,
            http_path='', auth_cookie_names=None, http_cookie_names=None,
            retries=3, jwt=None, user_agent=None,
            get_user_custom_headers_func=None):
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
    auth_mechanism : {'NOSASL', 'PLAIN', 'GSSAPI', 'LDAP', 'JWT'}
        Specify the authentication mechanism. `'NOSASL'` for unsecured Impala.
        `'PLAIN'` for unsecured Hive (because Hive requires the SASL
        transport). `'GSSAPI'` for Kerberos and `'LDAP'` for Kerberos with
        LDAP. `'JWT'` requires providing a JSON Web Token via the jwt parameter
        and only works with use_http_transport=True.
    user : str, optional
        LDAP user, if applicable.
    password : str, optional
        LDAP password, if applicable.
    kerberos_service_name : str, optional
        Authenticate to a particular `impalad` service principal. Uses
        `'impala'` by default.
    use_http_transport: bool optional
        Set it to True to use http transport of False to use binary transport.
    http_path: str, optional
        Specify the path in the http URL. Used only when `use_http_transport` is True.
    http_cookie_names: list of str or str, optional
        Specify the list of possible names for the cookies used for cookie-based
        authentication or session management. If the list of names contains one cookie
        name only, a str value can be specified instead of a list.
        If a cookie with one of these names is returned in an http response by the server
        or an intermediate proxy then it will be included in each subsequent request for
        the same connection. If set to wildcard ('*'), all cookies in an http response
        will be preserved. By default 'http_cookie_names' is set to '*'.
        Used only when `use_http_transport` is True.
        The names of authentication cookies are expected to end with ".auth" string, for
        example, "impala.auth" for Impala authentication cookies.
        If 'http_cookie_names' is explicitly set to a not None empty value ([], or ''),
        Impyla won't attempt to do cookie based authentication or session management.
        Currently cookie retention is supported for GSSAPI/LDAP/SASL/NOSASL/JWT over http.
    jwt: string containing a JSON Web Token
        This is used for auth_mechanism=JWT when using the HTTP transport.
    user_agent: A user specified user agent when HTTP transport is used. If none is specified,
        'Python/ImpylaHttpClient' is used
    use_ldap : bool, optional
        Specify `auth_mechanism='LDAP'` instead.
    get_user_custom_headers_func : function, optional
        Used to add custom headers to the http messages when using hs2-http protocol.
        This is a function returning a list of tuples, each tuple contains a key-value
        pair. This allows duplicate headers to be set.

        .. deprecated:: 0.18.0
    auth_cookie_names : list of str or str, optional
        Use `http_cookie_names` parameter instead.

        .. deprecated:: 0.18.0

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

    if auth_mechanism == 'JWT':
        if jwt is None:
            raise NotSupportedError("JWT authentication requires specifying the 'jwt' argument")
        if not use_http_transport:
            raise NotSupportedError('JWT authentication is only supported for HTTP transport')
        if not use_ssl:
            warn_nontls_jwt()
        if user is not None or ldap_user is not None:
            raise NotSupportedError("'user' argument cannot be specified with '{0}' authentication".format(auth_mechanism))
        if password is not None or ldap_password is not None:
            raise NotSupportedError("'password' argument cannot be specified with '{0}' authentication".format(auth_mechanism))
    else:
        if jwt is not None:
            raise NotSupportedError("'jwt' argument cannot be specified with '{0}' authentication".format(auth_mechanism))

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

    if auth_cookie_names is not None and http_cookie_names is None:
        warn_deprecate('auth_cookie_names', 'http_cookie_names')
        http_cookie_names = auth_cookie_names
    elif http_cookie_names is None:
        # Preserve all cookies.
        http_cookie_names = '*'

    service = hs2.connect(host=host, port=port,
                          timeout=timeout, use_ssl=use_ssl,
                          ca_cert=ca_cert, user=user, password=password,
                          kerberos_service_name=kerberos_service_name,
                          auth_mechanism=auth_mechanism, krb_host=krb_host,
                          use_http_transport=use_http_transport,
                          http_path=http_path,
                          http_cookie_names=http_cookie_names,
                          retries=retries,
                          jwt=jwt, user_agent=user_agent,
                          get_user_custom_headers_func=get_user_custom_headers_func)
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
DATE = _DBAPITypeObject('DATE')
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
