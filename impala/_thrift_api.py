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
import getpass
import os
from io import BytesIO

from six.moves import urllib
from six.moves import http_client
import warnings

import six
import ssl
import sys

from impala.error import HttpError
from impala.util import get_logger_and_init_null


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
    ExecStats = load(os.path.join(thrift_dir, 'ExecStats.thrift'),
                     include_dirs=[thrift_dir])
    TCLIService = load(os.path.join(thrift_dir, 'TCLIService.thrift'),
                       include_dirs=[thrift_dir])
    ImpalaService = load(os.path.join(thrift_dir, 'ImpalaService.thrift'),
                         include_dirs=[thrift_dir])
    RuntimeProfile = load(os.path.join(thrift_dir, 'RuntimeProfile.thrift'),
                          include_dirs=[thrift_dir])
    sys.modules[ExecStats.__name__] = ExecStats
    sys.modules[TCLIService.__name__] = TCLIService
    sys.modules[ImpalaService.__name__] = ImpalaService
    sys.modules[RuntimeProfile.__name__] = RuntimeProfile

    # import the HS2 objects
    from TCLIService import (  # noqa
        TOpenSessionReq, TFetchResultsReq, TCloseSessionReq,
        TExecuteStatementReq, TGetInfoReq, TGetInfoType, TTypeId,
        TFetchOrientation, TGetResultSetMetadataReq, TStatusCode,
        TGetColumnsReq, TGetSchemasReq, TGetTablesReq, TGetFunctionsReq,
        TGetOperationStatusReq, TOperationState, TCancelOperationReq,
        TCloseOperationReq, TGetLogReq, TProtocolVersion)
    from ImpalaService import (  # noqa
        TGetRuntimeProfileReq, TGetExecSummaryReq, ImpalaHiveServer2Service)
    from ExecStats import TExecStats  # noqa
    from RuntimeProfile import TRuntimeProfileFormat
    ThriftClient = TClient


class ImpalaHttpClient(TTransportBase):
  """Http implementation of TTransport base."""

  # When sending requests larger than this size, include the 'Expect: 100-continue' header
  # to indicate to the server to validate the request before reading the contents. This
  # value was chosen to match curl's behavior. See Section 8.2.3 of RFC2616.
  MIN_REQUEST_SIZE_FOR_EXPECT = 1024

  def __init__(self, uri_or_host, port=None, path=None, cafile=None, cert_file=None,
               key_file=None, ssl_context=None):
    """ImpalaHttpClient supports two different types of construction:

    ImpalaHttpClient(host, port, path) - deprecated
    ImpalaHttpClient(uri, [port=<n>, path=<s>, cafile=<filename>, cert_file=<filename>,
        key_file=<filename>, ssl_context=<context>])

    Only the second supports https.  To properly authenticate against the server,
    provide the client's identity by specifying cert_file and key_file.  To properly
    authenticate the server, specify either cafile or ssl_context with a CA defined.
    NOTE: if both cafile and ssl_context are defined, ssl_context will override cafile.
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
    self.__wbuf = BytesIO()
    self.__http = None
    self.__http_response = None
    self.__timeout = None
    self.__custom_headers = None

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

  def read(self, sz):
    return self.__http_response.read(sz)

  def write(self, buf):
    self.__wbuf.write(buf)

  def flush(self):
    if self.isOpen():
      self.close()
    self.open()

    # Pull data out of buffer
    data = self.__wbuf.getvalue()
    self.__wbuf = BytesIO()

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

    if self.code >= 300:
      # Report any http response code that is not 1XX (informational response) or
      # 2XX (successful).
      raise HttpError(self.code, self.message)


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
                       password=None):
    # TODO: support timeout
    if timeout is not None:
        log.error('get_http_transport does not support a timeout')
    if use_ssl:
        url = 'https://%s:%s/%s' % (host, port, http_path)
        log.debug('get_http_transport url=%s', url)
        # TODO(#362): Add server authentication with thrift 0.12.
        transport = ImpalaHttpClient(url)
    else:
        url = 'http://%s:%s/%s' % (host, port, http_path)
        log.debug('get_http_transport url=%s', url)
        transport = ImpalaHttpClient(url)

    # Set defaults for PLAIN SASL / LDAP connections.
    if auth_mechanism in ['PLAIN', 'LDAP']:
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
