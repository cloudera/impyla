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

# This package's main goal in the past was to clean up references to thrift, because
# we were using thriftpy2 for Py3. This is no longer necessary since upgrading to
# Thrift 0.11.0, as Thrift supports Python 3 since 0.10.0. Now there are only some
# leftover utility classes and functions.

# pylint: disable=wrong-import-position

from __future__ import absolute_import

import base64
import datetime
import getpass
import os
import os.path
from collections import namedtuple
from io import BytesIO

from six.moves import urllib, http_client
import warnings

import six
import ssl
import sys

from impala.error import HttpError
from impala.util import get_basic_credentials_for_request_headers
from impala.util import get_logger_and_init_null
from impala.util import get_all_matching_cookies, get_all_cookies, get_cookie_expiry

# Declare namedtuple for Cookie with named fields - cookie and expiry_time
Cookie = namedtuple('Cookie', ['cookie', 'expiry_time'])

log = get_logger_and_init_null(__name__)


# pylint: disable=import-error,unused-import
# import Apache Thrift code
from thrift.transport.TSocket import TSocket
from thrift.transport.TTransport import (
    TBufferedTransport, TTransportException, TTransportBase)

# import HS2 codegen objects
from impala._thrift_gen.ImpalaService import ImpalaHiveServer2Service
ThriftClient = ImpalaHiveServer2Service.Client


# ImpalaHttpClient is copied from Impala Shell.
# The implementations should be kept in sync as much as possible.
class ImpalaHttpClient(TTransportBase):
  """Http implementation of TTransport base."""

  # When sending requests larger than this size, include the 'Expect: 100-continue' header
  # to indicate to the server to validate the request before reading the contents. This
  # value was chosen to match curl's behavior. See Section 8.2.3 of RFC2616.
  MIN_REQUEST_SIZE_FOR_EXPECT = 1024

  def __init__(self, uri_or_host, port=None, path=None, cafile=None, cert_file=None,
               key_file=None, ssl_context=None, http_cookie_names=None,
               get_user_custom_headers_func=None):
    """ImpalaHttpClient supports two different types of construction:

    ImpalaHttpClient(host, port, path) - deprecated
    ImpalaHttpClient(uri, [port=<n>, path=<s>, cafile=<filename>, cert_file=<filename>,
        key_file=<filename>, ssl_context=<context>, http_cookie_names=<cookienamelist>],
        get_user_custom_headers_func=<function_setting_http_headers>)

    Only the second supports https.  To properly authenticate against the server,
    provide the client's identity by specifying cert_file and key_file.  To properly
    authenticate the server, specify either cafile or ssl_context with a CA defined.
    NOTE: if both cafile and ssl_context are defined, ssl_context will override cafile.
    http_cookie_names is used to specify the list of possible cookie names used for
    cookie-based authentication or session management. If there's only one name in the
    cookie name list, a str value can be specified instead of the list. If a cookie with
    one of these names is returned in an http response by the server or an intermediate
    proxy then it will be included in each subsequent request for the same connection. If
    it is set as wildcards, all cookies in an http response will be preserved.
    The optional get_user_custom_headers_func parameter can be used to add http headers
    to outgoing http messages when using hs2-http protocol. The parameter should be a
    function returning a list of tuples, each tuple containing a key-value pair
    representing the header name and value.
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
    if not http_cookie_names:
      # 'http_cookie_names' was explicitly set as an empty value ([], or '') in connect().
      self.__preserve_all_cookies = False
      self.__http_cookie_dict = None
      self.__auth_cookie_names = None
    elif str(http_cookie_names).strip() == "*":
      self.__preserve_all_cookies = True
      self.__http_cookie_dict = dict()
      self.__auth_cookie_names = set()
    else:
      self.__preserve_all_cookies = False
      if isinstance(http_cookie_names, six.string_types):
        http_cookie_names = [http_cookie_names]
      # Build a dictionary that maps cookie name to namedtuple.
      self.__http_cookie_dict = \
          { cn: Cookie(cookie=None, expiry_time=None) for cn in http_cookie_names }
      # Store the auth cookie names in __auth_cookie_names.
      # Assume auth cookie names end with ".auth".
      self.__auth_cookie_names = \
          { cn for cn in http_cookie_names if cn.endswith(".auth") }
    # Set __are_matching_cookies_found as True if matching cookies are found in response.
    self.__are_matching_cookies_found = False
    self.__wbuf = BytesIO()
    self.__http = None
    self.__http_response = None
    self.__timeout = None
    # __custom_headers is used to store HTTP headers which are generated in runtime for
    # new request.
    self.__custom_headers = None
    self.__get_custom_headers_func = None
    # __user_custom_headers is a list of tuples, each tuple contains a key-value pair.
    self.__user_custom_headers = None
    if get_user_custom_headers_func:
        self.__get_user_custom_headers_func = get_user_custom_headers_func
    else:
        self.__get_user_custom_headers_func = None
    # the default user agent if none is provied
    self.__custom_user_agent = 'Python/ImpylaHttpClient'

  @staticmethod
  def basic_proxy_auth_header(proxy):
    if proxy is None or not proxy.username:
      return None
    return "Basic " + get_basic_credentials_for_request_headers(
       user=urllib.parse.unquote(proxy.username),
       password=urllib.parse.unquote(proxy.password),
    )

  def using_proxy(self):
    return self.realhost is not None

  def open(self):
    if self.scheme == 'http':
      self.__http = http_client.HTTPConnection(self.host, self.port,
                                               timeout=self.__timeout)
    elif self.scheme == 'https':
      # (#529) From python 3.12 http_client.HTTPSConnection no longer
      # expects certfile and key_file. Certfile is included in context
      # while key_file can be used in SSLContext.load_verify_locations.
      # As Impyla doesn't support server authentication (#362) both
      # certfile and key_file are expected to be None here.
      if self.certfile or self.keyfile:
        raise NotSupportedError("Server authentication is not supported " +
                                "with HTTP endpoints")
      self.__http = http_client.HTTPSConnection(self.host, self.port,
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

  def setCustomUserAgent(self, user_agent):
    self.__custom_user_agent = user_agent

  # Set callback function which generate HTTP headers for a specific auth mechanism.
  def setGetCustomHeadersFunc(self, func):
    self.__get_custom_headers_func = func

  # Update outgoing HTTP headers.
  # This is done by two callback functions, if present
  # __get_custom_headers_func adds headers based on the saved cookies and auth
  # mechanism.
  # __get_user_custom_headers_func adds custom user-supplied http headers.
  def refreshCustomHeaders(self):
    if self.__get_custom_headers_func:
      cookie_header, has_auth_cookie = self.getHttpCookieHeaderForRequest()
      self.__custom_headers = \
          self.__get_custom_headers_func(cookie_header, has_auth_cookie)
    if self.__get_user_custom_headers_func:
       self.__user_custom_headers = \
          self.__get_user_custom_headers_func()

  # Return first value as a cookie list for Cookie header. It's a list of name-value
  # pairs in the form of <cookie-name>=<cookie-value>. Pairs in the list are separated by
  # a semicolon and a space ('; ').
  # Return second value as True if the cookie list contains auth cookie.
  def getHttpCookieHeaderForRequest(self):
    if (self.__http_cookie_dict is None) or not self.__are_matching_cookies_found:
      return None, False
    cookie_headers = []
    has_auth_cookie = False
    for cn, c_tuple in self.__http_cookie_dict.items():
      if c_tuple.cookie:
        if c_tuple.expiry_time and c_tuple.expiry_time <= datetime.datetime.now():
          self.__http_cookie_dict[cn] = Cookie(cookie=None, expiry_time=None)
        else:
          cookie_header = c_tuple.cookie.output(attrs=['value'], header='').strip()
          cookie_headers.append(cookie_header)
          if not has_auth_cookie and self.__auth_cookie_names \
              and cn in self.__auth_cookie_names:
            has_auth_cookie = True
    if not cookie_headers:
      self.__are_matching_cookies_found = False
      return None, False
    else:
      return '; '.join(cookie_headers), has_auth_cookie

  # Extract cookies from response and save those cookies for which the cookie names
  # are in the cookie name list specified in the connect() API.
  def extractHttpCookiesFromResponse(self):
    if self.__preserve_all_cookies:
       matching_cookies = get_all_cookies(self.path, self.headers)
    elif self.__http_cookie_dict is not None:
      matching_cookies = get_all_matching_cookies(
          self.__http_cookie_dict.keys(), self.path, self.headers)
    else:
      matching_cookies = None

    if matching_cookies:
      self.__are_matching_cookies_found = True
      for c in matching_cookies:
        self.__http_cookie_dict[c.key] = Cookie(c, get_cookie_expiry(c))
        if c.key.endswith(".auth"):
          self.__auth_cookie_names.add(c.key)

  # Return True if there are any saved cookies which are sent in previous request.
  def areHttpCookiesSaved(self):
    return self.__are_matching_cookies_found

  # Clean all saved cookies.
  def cleanHttpCookies(self):
    if (self.__http_cookie_dict is not None) and self.__are_matching_cookies_found:
      self.__are_matching_cookies_found = False
      self.__http_cookie_dict = \
          { cn: Cookie(cookie=None, expiry_time=None) for cn in self.__http_cookie_dict }

  def read(self, sz):
    return self.__http_response.read(sz)

  def readBody(self):
    return self.__http_response.read()

  def write(self, buf):
    self.__wbuf.write(buf)

  def flush(self):
    # Send HTTP request and receive response.
    # Return True if the client should retry this method.
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
        # Add the 'Expect' header to large requests. Note that we do not explicitly wait
        # for the '100 continue' response before sending the data - HTTPConnection simply
        # ignores these types of responses, but we'll get the right behavior anyways.
        self.__http.putheader("Expect", "100-continue")
      if self.using_proxy() and self.scheme == "http" and self.proxy_auth is not None:
        self.__http.putheader("Proxy-Authorization", self.proxy_auth)

      self.refreshCustomHeaders()
      if not self.__custom_headers or 'User-Agent' not in self.__custom_headers:
        user_agent = self.__custom_user_agent
        script = os.path.basename(sys.argv[0])
        if script:
          user_agent = '%s (%s)' % (user_agent, urllib.parse.quote(script))
        self.__http.putheader('User-Agent', user_agent)

      if self.__custom_headers:
        for key, val in six.iteritems(self.__custom_headers):
          self.__http.putheader(key, val)
      if self.__user_custom_headers:
        for key, val in self.__user_custom_headers:
          self.__http.putheader(key, val)

      self.__http.endheaders()

      # Write payload
      self.__http.send(data)

      # Get reply to flush the request
      self.__http_response = self.__http.getresponse()
      self.code = self.__http_response.status
      self.message = self.__http_response.reason
      self.headers = self.__http_response.msg
      # A '401 Unauthorized' response might mean that we tried cookie-based
      # authentication with one or more expired cookies.
      # Delete the cookies and try again.
      if self.code == 401 and self.areHttpCookiesSaved():
        self.cleanHttpCookies()
        return True
      else:
        self.extractHttpCookiesFromResponse()
        return False

    # Pull data out of buffer
    data = self.__wbuf.getvalue()
    self.__wbuf = BytesIO()

    retry = sendRequestRecvResp(data)
    if retry:
      log.debug('Received "401 Unauthorized" response. '
                'Delete HTTP cookies and then retry.')
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
        from thrift.transport.TSSLSocket import TSSLSocket

        # This copies the solution in IMPALA-11343.
        # TODO: remove once Thrit 0.17.0 is released
        class ImpalaTSSLSocket(TSSLSocket):
          # THRIFT-5595: override TSocket.isOpen because it's broken for TSSLSocket
          def isOpen(self):
            return self.handle is not None

        if ca_cert is None:
            return ImpalaTSSLSocket(host, port, validate=False)
        else:
            return ImpalaTSSLSocket(host, port, validate=True, ca_certs=ca_cert)
    else:
        return TSocket(host, port)


def get_http_transport(host, port, http_path, timeout=None, use_ssl=False,
                       ca_cert=None, auth_mechanism='NOSASL', user=None,
                       password=None, kerberos_host=None, kerberos_service_name=None,
                       http_cookie_names=None, jwt=None, user_agent=None,
                       get_user_custom_headers_func=None):
    host_url = "[%s]" % host if ":" in host else host # add brackets for ipv6 address
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

        url = 'https://%s:%s/%s' % (host_url, port, http_path)
        log.debug('get_http_transport url=%s', url)
        # TODO(#362): Add server authentication with thrift 0.12.
        transport = ImpalaHttpClient(
            url, ssl_context=ssl_ctx,
            http_cookie_names=http_cookie_names,
            get_user_custom_headers_func=get_user_custom_headers_func)
    else:
        url = 'http://%s:%s/%s' % (host_url, port, http_path)
        log.debug('get_http_transport url=%s', url)
        transport = ImpalaHttpClient(
            url, http_cookie_names=http_cookie_names,
            get_user_custom_headers_func=get_user_custom_headers_func)

    # set custom user agent if provided by user
    if user_agent:
        transport.setCustomUserAgent(user_agent)

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
        else:
            log.debug('get_http_transport: password=fuggetaboutit')
        auth_mechanism = 'PLAIN'  # sasl doesn't know mechanism LDAP
        # Set the BASIC auth header
        auth = get_basic_credentials_for_request_headers(user, password)

        def get_custom_headers(cookie_header, has_auth_cookie):
            custom_headers = {}
            if cookie_header:
                log.debug('add cookies to HTTP header')
                custom_headers['Cookie'] = cookie_header
            # Add the 'Authorization' header to request even if the auth cookie is
            # present to avoid a round trip in case the cookie is expired when server
            # receive the request. Since the 'auth' value is calculated once, so it
            # won't cause a performance issue.
            custom_headers['Authorization'] = "Basic " + auth
            return custom_headers

        transport.setGetCustomHeadersFunc(get_custom_headers)

    elif auth_mechanism == 'GSSAPI':
        # For GSSAPI over http we need to dynamically generate custom request headers.
        def get_custom_headers(cookie_header, has_auth_cookie):
            import kerberos
            custom_headers = {}
            if cookie_header:
                log.debug('add cookies to HTTP header')
                custom_headers['Cookie'] = cookie_header
            if not has_auth_cookie:
                _, krb_context = kerberos.authGSSClientInit("%s@%s" %
                                    (kerberos_service_name, kerberos_host))
                kerberos.authGSSClientStep(krb_context, "")
                negotiate_details = kerberos.authGSSClientResponse(krb_context)
                custom_headers['Authorization'] = "Negotiate " + negotiate_details
            return custom_headers

        transport.setGetCustomHeadersFunc(get_custom_headers)

    elif auth_mechanism == 'JWT':
        # For JWT authentication, the JWT is sent on the Authorization Bearer
        # HTTP header.
        def get_custom_headers(cookie_header, has_auth_cookie):
            custom_headers = {}
            if cookie_header:
                log.debug('add cookies to HTTP header')
                custom_headers['Cookie'] = cookie_header

            custom_headers['Authorization'] = "Bearer " + jwt
            return custom_headers

        transport.setGetCustomHeadersFunc(get_custom_headers)

    elif auth_mechanism == 'NOSASL':
        def get_custom_headers(cookie_header, has_auth_cookie):
            custom_headers = {}
            if cookie_header:
                log.debug('add cookies to HTTP header')
                custom_headers['Cookie'] = cookie_header
            return custom_headers

        transport.setGetCustomHeadersFunc(get_custom_headers)

    # Without buffering Thrift would call socket.recv() each time it deserializes
    # something (e.g. a member in a struct).
    transport = TBufferedTransport(transport)
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
    from impala.sasl_compat import PureSASLClient

    def sasl_factory():
        return PureSASLClient(host, username=user, password=password,
                              service=kerberos_service_name)

    return TSaslClientTransport(sasl_factory, auth_mechanism, socket)
