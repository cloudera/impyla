# Copyright 2019 Cloudera Inc.
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

import socket
import threading
from contextlib import closing

import pytest
import requests
import six
from six.moves import SimpleHTTPServer
from six.moves import http_client
from six.moves import socketserver

from impala.error import HttpError
from impala.tests.util import ImpylaTestEnv, is_ipv6_only_host

ENV = ImpylaTestEnv()

IS_IPV6_ONLY_HOST = is_ipv6_only_host(ENV.host, ENV.port)
LOCAL_HOST = "::1" if IS_IPV6_ONLY_HOST else "127.0.0.1"

# socketserver.TCPServer cannot listen both on ipv4 and ipv6. Listen to ipv6
# if the hs2-http server has only ipv6 address.
class IPv4or6TcpServer(socketserver.TCPServer):
  address_family = socket.AF_INET6 if IS_IPV6_ONLY_HOST else socket.AF_INET
  def __init__(self, host_port, req_handler):
    socketserver.TCPServer.__init__(self, host_port, req_handler)

@pytest.fixture
def http_503_server():
  class RequestHandler503(SimpleHTTPServer.SimpleHTTPRequestHandler):
    """A custom http handler that checks for duplicate 'Host' headers from the most
    recent http request, and always returns a 503 http code"""

    def do_POST(self):
      # Ensure that only one 'Host' header is contained in the request before responding.
      request_headers = None
      host_hdr_count = 0
      if six.PY2:
        # The unfortunately named self.headers here is an instance of mimetools.Message that
        # contains the request headers.
        request_headers = self.headers.headers
        host_hdr_count = sum([header.startswith('Host:') for header in request_headers])
      if six.PY3:
        # In Python3 self.Headers is an HTTPMessage.
        request_headers = self.headers
        host_hdr_count = sum([header[0] == 'Host' for header in request_headers.items()])
      assert host_hdr_count == 1, "need single 'Host:' header in %s" % request_headers

      # Respond with 503.
      self.send_response(code=http_client.SERVICE_UNAVAILABLE, message="Service Unavailable")
      self.end_headers()
      self.wfile.write("extra text".encode('utf-8'))

  class TestHTTPServer503(object):
    def __init__(self):
      self.HOST = LOCAL_HOST
      self.PORT = get_unused_port()
      self.httpd = IPv4or6TcpServer((self.HOST, self.PORT), RequestHandler503)

      self.http_server_thread = threading.Thread(target=self.httpd.serve_forever)
      self.http_server_thread.start()

  server = TestHTTPServer503()
  yield server

  # Cleanup after test.
  shutdown_server(server)


@pytest.yield_fixture
def http_proxy_server():
  """A fixture that creates a reverse http proxy."""

  class RequestHandlerProxy(SimpleHTTPServer.SimpleHTTPRequestHandler):
    """A custom http handler that acts as a reverse http proxy. This proxy will forward
    http messages to Impala, and copy the responses back to the client. In addition, it
    will save the outgoing http message headers in a class variable so that they can be
    accessed by test code."""

    # This class variable is used to store the most recently seen outgoing http
    # message headers.
    saved_headers=None

    def __init__(self, request, client_address, server):
      SimpleHTTPServer.SimpleHTTPRequestHandler.__init__(self, request, client_address,
                                                    server)

    def do_POST(self):
      # Read the body of the incoming http post message.
      data_string = self.rfile.read(int(self.headers['Content-Length']))
      # Save the http headers from the message in a class variable.
      RequestHandlerProxy.saved_headers = self.decode_raw_headers()
      # Forward the http post message to Impala and get a response message.
      host = "[%s]" % ENV.host  if ":" in ENV.host else ENV.host
      response = requests.post(
        url="http://{0}:{1}/cliservice".format(host, ENV.http_port),
        headers=self.headers, data=data_string)
      # Send the response message back to the client.
      self.send_response(code=response.status_code)
      # Send the http headers.
      # In python3 response.headers is a CaseInsensitiveDict
      # In python2 response.headers is a dict
      for key, value in response.headers.items():
        self.send_header(keyword=key, value=value)
      self.end_headers()
      # Send the message body.
      self.wfile.write(response.content)

    def decode_raw_headers(self):
      """Decode a list of header strings into a list of tuples, each tuple containing a
      key-value pair. The details of how to get the headers differs between Python2
      and Python3"""
      if six.PY2:
        header_list = []
        # In Python2 self.headers is an instance of mimetools.Message and
        # self.headers.headers is a list of raw header strings.
        # An example header string: 'Accept-Encoding: identity\\r\\n'
        for header in self.headers.headers:
          stripped = header.strip()
          key, value = stripped.split(':', 1)
          header_list.append((key.strip(), value.strip()))
        return header_list
      if six.PY3:
        # In Python 3 self.headers._headers is what we need
        return self.headers._headers


  class TestHTTPServerProxy(object):
    def __init__(self, clazz):
      self.clazz = clazz
      self.HOST = LOCAL_HOST
      self.PORT = get_unused_port()
      self.httpd = IPv4or6TcpServer((self.HOST, self.PORT), clazz)
      self.http_server_thread = threading.Thread(target=self.httpd.serve_forever)
      self.http_server_thread.start()

    def get_headers(self):
      """Return the most recently seen outgoing http message headers."""
      return self.clazz.saved_headers

  server = TestHTTPServerProxy(RequestHandlerProxy)
  yield server

  # Cleanup after test.
  shutdown_server(server)


from impala.dbapi import connect

class TestHttpConnect(object):
  def test_simple_connect(self):
    con = connect(ENV.host, ENV.http_port, use_http_transport=True, http_path="cliservice")
    cur = con.cursor()
    cur.execute('select 1')
    rows = cur.fetchall()
    assert rows == [(1,)]

  def test_http_interactions(self, http_503_server):
    """Test interactions with the http server when using hs2-http protocol.
    Check that there is an HttpError exception when the server returns a 503 error."""
    con = connect(ENV.host, http_503_server.PORT, use_http_transport=True)
    try:
      con.cursor()
      assert False, "Should have got exception"
    except HttpError as e:
      assert str(e) == "HTTP code 503: Service Unavailable"
      assert e.code == http_client.SERVICE_UNAVAILABLE
      assert e.body.decode("utf-8") == "extra text"

  def test_duplicate_headers(self, http_proxy_server):
    """Test that we can use 'connect' with the get_user_custom_headers_func parameter
    to add duplicate http message headers to outgoing messages."""
    con = connect(ENV.host, http_proxy_server.PORT, use_http_transport=True,
                  get_user_custom_headers_func=get_user_custom_headers_func)
    cur = con.cursor()
    cur.execute('select 1')
    rows = cur.fetchall()
    assert rows == [(1,)]

    # Get the outgoing message headers from the last outgoing http message.
    headers = http_proxy_server.get_headers()
    # For sanity test the count of a few simple expected headers.
    assert count_tuples_with_key(headers, "Host") == 1
    assert count_tuples_with_key(headers, "User-Agent") == 1
    # Check that the custom headers are present.
    assert count_tuples_with_key(headers, "key1") == 2
    assert count_tuples_with_key(headers, "key2") == 1
    assert count_tuples_with_key(headers, "key3") == 0
    
  def test_basic_auth_headers(self, http_proxy_server):
    con = connect(
      ENV.host,
      http_proxy_server.PORT,
      use_http_transport=True,
      user="thisisaratherlongusername",
      password="very!long!passwordthatcreatesalongbasic64encoding",
      auth_mechanism="PLAIN"
    )
    cur = con.cursor()
    cur.execute('select 1')
    rows = cur.fetchall()
    assert rows == [(1,)]

    headers = http_proxy_server.get_headers()
    assert ('Authorization', "Basic dGhpc2lzYXJhdGhlcmxvbmd1c2VybmFtZTp2ZXJ5IWxvbmchcGFzc3dvcmR0aGF0Y3JlYXRlc2Fsb25nYmFzaWM2NGVuY29kaW5n") in headers

def get_user_custom_headers_func():
  """Insert some custom http headers, including a duplicate."""
  headers = []
  headers.append(('key1', 'value1'))
  headers.append(('key1', 'value2'))
  headers.append(('key2', 'value3'))
  return headers


def get_unused_port():
  """ Find an unused port http://stackoverflow.com/questions/1365265 """
  with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
    s.bind(('', 0))
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    return s.getsockname()[1]

def shutdown_server(server):
  """Helper method to shutdown a http server."""
  if server.httpd is not None:
    server.httpd.shutdown()
  if server.http_server_thread is not None:
    server.http_server_thread.join()

def count_tuples_with_key(tuple_list, key_to_count):
  """Counts the number of tuples in a list that have a specific key.
  Args:
    tuple_list: A list of key-value tuples.
    key_to_count: The key to count occurrences of.
  Returns:
    The number of tuples with the specified key.
  """
  count = 0
  for key, _ in tuple_list:
    if key == key_to_count:
      count += 1
  return count
