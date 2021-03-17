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

# This package is here to clean up references to thrift, because we're using
# thriftpy2 for Py3 at the moment.  This should all be temporary, as Apache
# Thrift gains Py3 compatibility.

# pylint: disable=wrong-import-position

from __future__ import absolute_import

import base64
import datetime
import getpass
import os
import os.path
from io import BytesIO

from six.moves import urllib, http_client
import warnings

import six
import ssl
import sys

from impala.error import HttpError
from impala.util import get_logger_and_init_null
from impala.util import get_first_matching_cookie, get_cookie_expiry


log = get_logger_and_init_null(__name__)


if six.PY2:
    # pylint: disable=import-error,unused-import
    # import Apache Thrift code
    from thrift.transport.TSocket import TSocket
    from thrift.transport.TTransport import (
        TBufferedTransport, TTransportException, TTransportBase)
    from thrift.Thrift import TApplicationException
    from thrift.protocol.TBinaryProtocol import (
        TBinaryProtocolAccelerated as TBinaryProtocol)

    # import HS2 codegen objects
    from impala._thrift_gen.TCLIService.ttypes import (
        TOpenSessionReq, TFetchResultsReq, TCloseSessionReq,
        TExecuteStatementReq, TGetInfoReq, TGetInfoType, TTypeId,
        TFetchOrientation, TGetResultSetMetadataReq, TStatusCode,
        TGetColumnsReq, TGetSchemasReq, TGetTablesReq, TGetFunctionsReq,
        TGetOperationStatusReq, TOperationState, TCancelOperationReq,
        TCloseOperationReq, TGetLogReq, TProtocolVersion)
    from impala._thrift_gen.ImpalaService.ImpalaHiveServer2Service import (
        TGetRuntimeProfileReq, TGetExecSummaryReq)
    from impala._thrift_gen.ImpalaService import ImpalaHiveServer2Service
    from impala._thrift_gen.ExecStats.ttypes import TExecStats
    ThriftClient = ImpalaHiveServer2Service.Client
    from impala._thrift_gen.RuntimeProfile.ttypes import TRuntimeProfileFormat


if six.PY3:
    # When using python 3, import from thriftpy2 rather than thrift
    from thriftpy2 import load
    from thriftpy2.thrift import TClient, TApplicationException
    # TODO: reenable cython
    # from thriftpy2.protocol import TBinaryProtocol
    from thriftpy2.protocol.binary import TBinaryProtocol  # noqa
    from thriftpy2.transport import (TSocket, TTransportException, TTransportBase) # noqa
    # TODO: reenable cython
    # from thriftpy2.transport import TBufferedTransport
    from thriftpy2.transport.buffered import TBufferedTransport  # noqa
    thrift_dir = os.path.join(os.path.dirname(__file__), 'thrift')

    # dynamically load the HS2 modules
    # Put them under the impala module to avoid conflicts with PyHive and other packages
    # (see #277).
    ExecStats = load(os.path.join(thrift_dir, 'ExecStats.thrift'),
                     include_dirs=[thrift_dir], module_name="impala.ExecStats_thrift")
    TCLIService = load(os.path.join(thrift_dir, 'TCLIService.thrift'),
                       include_dirs=[thrift_dir], module_name="impala.TCLIService_thrift")
    ImpalaService = load(os.path.join(thrift_dir, 'ImpalaService.thrift'),
                         include_dirs=[thrift_dir], module_name="impala.ImpalaService_thrift")
    RuntimeProfile = load(os.path.join(thrift_dir, 'RuntimeProfile.thrift'),
                          include_dirs=[thrift_dir], module_name="impala.RuntimeProfile_thrift")
    sys.modules[ExecStats.__name__] = ExecStats
    sys.modules[TCLIService.__name__] = TCLIService
    sys.modules[ImpalaService.__name__] = ImpalaService
    sys.modules[RuntimeProfile.__name__] = RuntimeProfile

    # import the HS2 objects
    from impala.TCLIService_thrift import (  # noqa
        TOpenSessionReq, TFetchResultsReq, TCloseSessionReq,
        TExecuteStatementReq, TGetInfoReq, TGetInfoType, TTypeId,
        TFetchOrientation, TGetResultSetMetadataReq, TStatusCode,
        TGetColumnsReq, TGetSchemasReq, TGetTablesReq, TGetFunctionsReq,
        TGetOperationStatusReq, TOperationState, TCancelOperationReq,
        TCloseOperationReq, TGetLogReq, TProtocolVersion)
    from impala.ImpalaService_thrift import (  # noqa
        TGetRuntimeProfileReq, TGetExecSummaryReq, ImpalaHiveServer2Service)
    from impala.ExecStats_thrift import TExecStats  # noqa
    from impala.RuntimeProfile_thrift import TRuntimeProfileFormat
    ThriftClient = TClient

# ImpalaHttpClient is copied from Impala Shell.
# The implementations should be kept in sync as much as possible.
class ImpalaHttpClient(TTransportBase):
  """Http implementation of TTransport base."""

  # When sending requests larger than this size, include the 'Expect: 100-continue' header
  # to indicate to the server to validate the request before reading the contents. This
  # value was chosen to match curl's behavior. See Section 8.2.3 of RFC2616.
  MIN_REQUEST_SIZE_FOR_EXPECT = 1024

  def __init__(self, uri_or_host, port=None, path=None, cafile=None, cert_file=None,
               key_file=None, ssl_context=None, auth_cookie_names=None):
    """ImpalaHttpClient supports two different types of construction:

    ImpalaHttpClient(host, port, path) - deprecated
    ImpalaHttpClient(uri, [port=<n>, path=<s>, cafile=<filename>, cert_file=<filename>,
        key_file=<filename>, ssl_context=<context>, auth_cookie_names=<cookienamelist>])

    Only the second supports https.  To properly authenticate against the server,
    provide the client's identity by specifying cert_file and key_file.  To properly
    authenticate the server, specify either cafile or ssl_context with a CA defined.
    NOTE: if both cafile and ssl_context are defined, ssl_context will override cafile.
    auth_cookie_names is used to specify the list of possible cookie names used for
    cookie-based authentication. If there's only one name in the cookie name list, a str
    value can be specified instead of the list.
    """
    if port is not None:
      warnings.warn(
        "Please use the ImpalaHttpClient('http{s}://host:port/path') constructor",
        DeprecationWarning,
        stacklevel=2)
      self.host = uri_or_host
      self.port = port
      assert path
      self.path = path
      self.scheme = 'http'
    else:
      parsed = urllib.parse.urlparse(uri_or_host)
      self.scheme = parsed.scheme
      assert self.scheme in ('http', 'https')
      if self.scheme == 'http':
        self.port = parsed.port or http_client.HTTP_PORT
      elif self.scheme == 'https':
        self.port = parsed.port or http_client.HTTPS_PORT
        self.certfile = cert_file
        self.keyfile = key_file
        self.context = ssl.create_default_context(cafile=cafile) \
          if (cafile and not ssl_context) else ssl_context
      self.host = parsed.hostname
      self.path = parsed.path
      if parsed.query:
        self.path += '?%s' % parsed.query
    try:
      proxy = urllib.request.getproxies()[self.scheme]
    except KeyError:
      proxy = None
    else:
      if urllib.request.proxy_bypass(self.host):
        proxy = None
    if proxy:
      parsed = urllib.parse.urlparse(proxy)
      self.realhost = self.host
      self.realport = self.port
      self.host = parsed.hostname
      self.port = parsed.port
      self.proxy_auth = self.basic_proxy_auth_header(parsed)
    else:
      self.realhost = self.realport = self.proxy_auth = None
    self.__auth_cookie_names = auth_cookie_names
    self.__auth_cookie = None
    self.__auth_cookie_expiry = None
    self.__wbuf = BytesIO()
    self.__http = None
    self.__http_response = None
    self.__timeout = None
    self.__custom_headers = None
    self.__get_custom_headers_func = None

  @staticmethod
  def basic_proxy_auth_header(proxy):
    if proxy is None or not proxy.username:
      return None
    ap = "%s:%s" % (urllib.parse.unquote(proxy.username),
                    urllib.parse.unquote(proxy.password))
    cr = base64.b64encode(ap).strip()
    return "Basic " + cr

  def using_proxy(self):
    return self.realhost is not None

  def open(self):
    if self.scheme == 'http':
      self.__http = http_client.HTTPConnection(self.host, self.port,
                                               timeout=self.__timeout)
    elif self.scheme == 'https':
      self.__http = http_client.HTTPSConnection(self.host, self.port,
                                                key_file=self.keyfile,
                                                cert_file=self.certfile,
                                                timeout=self.__timeout,
                                                context=self.context)
    if self.using_proxy():
      self.__http.set_tunnel(self.realhost, self.realport,
                             {"Proxy-Authorization": self.proxy_auth})

  def close(self):
    self.__http.close()
    self.__http = None
    self.__http_response = None

  def isOpen(self):
    return self.__http is not None

  def is_open(self):
    return self.__http is not None

  def setTimeout(self, ms):
    if ms is None:
      self.__timeout = None
    else:
      self.__timeout = ms / 1000.0

  def setCustomHeaders(self, headers):
    self.__custom_headers = headers

  def setGetCustomHeadersFunc(self, func):
    self.__get_custom_headers_func = func

  def refreshCustomHeaders(self):
    if self.__get_custom_headers_func:
      self.__custom_headers = self.__get_custom_headers_func(self.getAuthCookie())

  def setAuthCookie(self):
    if self.__auth_cookie_names:
      c = get_first_matching_cookie(self.__auth_cookie_names, self.path, self.headers)
      if c:
        self.__auth_cookie = c
        self.__auth_cookie_expiry = get_cookie_expiry(c)

  def getAuthCookie(self):
    if self.__auth_cookie and self.__auth_cookie_expiry and \
        self.__auth_cookie_expiry <= datetime.datetime.now():
      self.__auth_cookie = None
    return self.__auth_cookie

  def isAuthCookieSet(self):
    return self.__auth_cookie is not None

  def deleteAuthCookie(self):
    self.__auth_cookie = None
    self.__auth_cookie_expiry = None

  def read(self, sz):
    return self.__http_response.read(sz)

  def readBody(self):
    return self.__http_response.read()

  def write(self, buf):
    self.__wbuf.write(buf)

  def flush(self):
    def sendRequestRecvResp(data):
      if self.isOpen():
        self.close()
      self.open()

      # HTTP request
      if self.using_proxy() and self.scheme == "http":
        # need full URL of real host for HTTP proxy here (HTTPS uses CONNECT tunnel)
        self.__http.putrequest('POST', "http://%s:%s%s" %
                               (self.realhost, self.realport, self.path))
      else:
        self.__http.putrequest('POST', self.path)

      # Write headers
      self.__http.putheader('Content-Type', 'application/x-thrift')
      data_len = len(data)
      self.__http.putheader('Content-Length', str(data_len))
      if data_len > ImpalaHttpClient.MIN_REQUEST_SIZE_FOR_EXPECT:
        # Add the 'Expect' header to large requests. Note that we do not explicitly wait for
        # the '100 continue' response before sending the data - HTTPConnection simply
        # ignores these types of responses, but we'll get the right behavior anyways.
        self.__http.putheader("Expect", "100-continue")
      if self.using_proxy() and self.scheme == "http" and self.proxy_auth is not None:
        self.__http.putheader("Proxy-Authorization", self.proxy_auth)

      self.refreshCustomHeaders()
      if not self.__custom_headers or 'User-Agent' not in self.__custom_headers:
        user_agent = 'Python/ImpalaHttpClient'
        script = os.path.basename(sys.argv[0])
        if script:
          user_agent = '%s (%s)' % (user_agent, urllib.parse.quote(script))
        self.__http.putheader('User-Agent', user_agent)

      if self.__custom_headers:
        for key, val in six.iteritems(self.__custom_headers):
          self.__http.putheader(key, val)

      self.__http.endheaders()

      # Write payload
      self.__http.send(data)

      # Get reply to flush the request
      self.__http_response = self.__http.getresponse()
      self.code = self.__http_response.status
      self.message = self.__http_response.reason
      self.headers = self.__http_response.msg
      self.setAuthCookie()

    # Pull data out of buffer
    data = self.__wbuf.getvalue()
    self.__wbuf = BytesIO()

    sendRequestRecvResp(data)

    # A '401 Unauthorized' response might mean that we tried cookie-based authentication
    # with an expired cookie.
    # Delete the cookie and try again.
    if self.code == 401 and self.isAuthCookieSet():
      log.debug('Received "401 Unauthorized" response. '
                'Delete auth cookie and then retry.')
      self.deleteAuthCookie()
      sendRequestRecvResp(data)

    if self.code >= 300:
      # Report any http response code that is not 1XX (informational response) or
      # 2XX (successful).
      body = self.readBody()
      raise HttpError(self.code, self.message, body, self.headers)


def get_socket(host, port, use_ssl, ca_cert):
    # based on the Impala shell impl
    log.debug('get_socket: host=%s port=%s use_ssl=%s ca_cert=%s',
              host, port, use_ssl, ca_cert)

    if use_ssl:
        if six.PY2:
            from thrift.transport.TSSLSocket import TSSLSocket
            if ca_cert is None:
                return TSSLSocket(host, port, validate=False)
            else:
                return TSSLSocket(host, port, validate=True, ca_certs=ca_cert)
        else:
            from thriftpy2.transport.sslsocket import TSSLSocket
            if ca_cert is None:
                return TSSLSocket(host, port, validate=False)
            else:
                return TSSLSocket(host, port, validate=True, cafile=ca_cert)
    else:
        return TSocket(host, port)


def get_http_transport(host, port, http_path, timeout=None, use_ssl=False,
                       ca_cert=None, auth_mechanism='NOSASL', user=None,
                       password=None, kerberos_host=None, kerberos_service_name=None,
                       auth_cookie_names=None):
    # TODO: support timeout
    if timeout is not None:
        log.error('get_http_transport does not support a timeout')
    if use_ssl:
        ssl_ctx = ssl.create_default_context(cafile=ca_cert)
        if ca_cert:
          ssl_ctx.verify_mode = ssl.CERT_REQUIRED
        else:
          ssl_ctx.check_hostname = False  # Mandated by the SSL lib for CERT_NONE mode.
          ssl_ctx.verify_mode = ssl.CERT_NONE

        url = 'https://%s:%s/%s' % (host, port, http_path)
        log.debug('get_http_transport url=%s', url)
        # TODO(#362): Add server authentication with thrift 0.12.
        transport = ImpalaHttpClient(url, ssl_context=ssl_ctx,
                                     auth_cookie_names=auth_cookie_names)
    else:
        url = 'http://%s:%s/%s' % (host, port, http_path)
        log.debug('get_http_transport url=%s', url)
        transport = ImpalaHttpClient(url, auth_cookie_names=auth_cookie_names)

    if auth_mechanism in ['PLAIN', 'LDAP']:
        # Set defaults for PLAIN SASL / LDAP connections.
        if user is None:
            user = getpass.getuser()
            log.debug('get_http_transport: user=%s', user)
        if password is None:
            if auth_mechanism == 'LDAP':
                password = ''
            else:
                # PLAIN always requires a password for HS2.
                password = 'password'
        log.debug('get_http_transport: password=%s', password)
        auth_mechanism = 'PLAIN'  # sasl doesn't know mechanism LDAP
        # Set the BASIC auth header
        user_password = '%s:%s'.encode() % (user.encode(), password.encode())
        try:
            auth = base64.encodebytes(user_password).decode().strip('\n')
        except AttributeError:
            auth = base64.encodestring(user_password).decode().strip('\n')

        transport.setCustomHeaders({'Authorization': 'Basic %s' % auth})

    elif auth_mechanism == 'GSSAPI':
        # For GSSAPI over http we need to dynamically generate custom request headers.
        def get_auth_headers(auth_cookie):
            import kerberos
            if auth_cookie:
                cookie_value = auth_cookie.output(attrs=['value'], header='' ).strip()
                return {'Cookie': cookie_value}
            else:
                _, krb_context = kerberos.authGSSClientInit("%s@%s" %
                                    (kerberos_service_name, kerberos_host))
                kerberos.authGSSClientStep(krb_context, "")
                negotiate_details = kerberos.authGSSClientResponse(krb_context)
                return {"Authorization": "Negotiate " + negotiate_details}

        transport.setGetCustomHeadersFunc(get_auth_headers)

    return transport


def get_transport(socket, host, kerberos_service_name, auth_mechanism='NOSASL',
                  user=None, password=None):
    """
    Creates a new Thrift Transport using the specified auth_mechanism.
    Supported auth_mechanisms are:
    - None or 'NOSASL' - returns simple buffered transport (default)
    - 'PLAIN'  - returns a SASL transport with the PLAIN mechanism
    - 'GSSAPI' - returns a SASL transport with the GSSAPI mechanism
    """
    log.debug('get_transport: socket=%s host=%s kerberos_service_name=%s '
              'auth_mechanism=%s user=%s password=fuggetaboutit', socket, host,
              kerberos_service_name, auth_mechanism, user)

    if auth_mechanism == 'NOSASL':
        return TBufferedTransport(socket)

    # Set defaults for PLAIN SASL / LDAP connections.
    if auth_mechanism in ['LDAP', 'PLAIN']:
        if user is None:
            user = getpass.getuser()
            log.debug('get_transport: user=%s', user)
        if password is None:
            if auth_mechanism == 'LDAP':
                password = ''
            else:
                # PLAIN always requires a password for HS2.
                password = 'password'
            log.debug('get_transport: password=%s', password)
        auth_mechanism = 'PLAIN'  # sasl doesn't know mechanism LDAP
    # Initializes a sasl client
    from thrift_sasl import TSaslClientTransport
    try:
        import sasl  # pylint: disable=import-error

        def sasl_factory():
            sasl_client = sasl.Client()
            sasl_client.setAttr('host', host)
            sasl_client.setAttr('service', kerberos_service_name)
            if auth_mechanism.upper() in ['PLAIN', 'LDAP']:
                sasl_client.setAttr('username', user)
                sasl_client.setAttr('password', password)
            sasl_client.init()
            return sasl_client
    except ImportError:
        log.warn("Unable to import 'sasl'. Fallback to 'puresasl'.")
        from impala.sasl_compat import PureSASLClient

        def sasl_factory():
            return PureSASLClient(host, username=user, password=password,
                                  service=kerberos_service_name)

    return TSaslClientTransport(sasl_factory, auth_mechanism, socket)
