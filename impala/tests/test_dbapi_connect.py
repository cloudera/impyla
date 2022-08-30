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

from __future__ import absolute_import, print_function

import sys

from impala.error import NotSupportedError

if sys.version_info[:2] <= (2, 6):
    import unittest2 as unittest
else:
    import unittest

import pytest

from impala.dbapi import connect
from impala.util import _random_id
from impala.tests.util import ImpylaTestEnv, SocketTracker


ENV = ImpylaTestEnv()
DEFAULT_AUTH = True
DEFAULT_AUTH_ERROR = "Non-default authorization method"

# JWT tests require the Impala coordinator to have the following startup flags:
# --jwt_token_auth=true --jwt_validate_signature=false --jwt_allow_without_tls=true
JWT_DISABLED = True
JWT_DISABLED_ERROR = "JWT authentication disabled"


# SSL can be enabled in Impala dev environment with the following commands:
# export IMPALA_SSL_CERT_DIR=$IMPALA_HOME/be/src/testutil
# export IMPALA_SSL_ARGS="--ssl_client_ca_certificate=$IMPALA_SSL_CERT_DIR/server-cert.pem --ssl_server_certificate=$IMPALA_SSL_CERT_DIR/server-cert.pem --ssl_private_key=$IMPALA_SSL_CERT_DIR/server-key.pem --hostname=localhost"
# bin/start-impala-cluster.py --impalad_args="$IMPALA_SSL_ARGS" --catalogd_args="$IMPALA_SSL_ARGS" --state_store_args="$IMPALA_SSL_ARGS"
# export IMPYLA_SSL_CERT=$IMPALA_SSL_CERT_DIR/server-cert.pem
SSL_DISABLED = ENV.ssl_cert == ""
SSL_DISABLED_ERROR = "No ssl certificate set."


class ImpalaConnectionTests(unittest.TestCase):

    table_prefix = _random_id(prefix='dbapi20test_')
    tablename = table_prefix + 'contests'

    def setUp(self):
        self.connection = None

    def tearDown(self):
        if self.connection:
            self.connection.close()

    def _execute_queries(self, con):
        ddl = """
            CREATE TABLE {0} (
              f1 INT,
              f2 INT)
        """.format(self.tablename)
        try:
            cur = con.cursor()
            cur.execute(ddl)
            con.commit()
            cur.execute('DROP TABLE {0}'.format(self.tablename))
            con.commit()
        except:
            raise

    def _execute_query_get_username(self, con):
        query = "select user()"
        username_rows = None
        try:
            cur = con.cursor()
            cur.execute(query)
            username_rows = cur.fetchall()
        except:
            raise

        # Expecting the username as a single row with single column
        assert(username_rows is not None)
        assert(len(username_rows) == 1)
        assert(len(username_rows[0]) == 1)
        username = username_rows[0][0]
        return username

    def test_impala_nosasl_connect(self):
        self.connection = connect(ENV.host, ENV.port, timeout=5)
        self._execute_queries(self.connection)

    @pytest.mark.skipif(ENV.skip_hive_tests, reason="Skipping hive tests")
    def test_hive_plain_connect(self):
        self.connection = connect(ENV.host, ENV.hive_port,
                                  auth_mechanism="PLAIN",
                                  timeout=5,
                                  user=ENV.hive_user,
                                  password="cloudera")
        self._execute_queries(self.connection)

    @pytest.mark.skipif(DEFAULT_AUTH, reason=DEFAULT_AUTH_ERROR)
    def test_impala_plain_connect(self):
        self.connection = connect(ENV.host, ENV.port, auth_mechanism="PLAIN",
                                  timeout=5,
                                  user=ENV.hive_user,
                                  password="cloudera")
        self._execute_queries(self.connection)

    @pytest.mark.skipif(DEFAULT_AUTH, reason=DEFAULT_AUTH_ERROR)
    def test_hive_nosasl_connect(self):
        self.connection = connect(ENV.host, ENV.hive_port, timeout=5)
        self._execute_queries(self.connection)

    def test_bad_auth(self):
        """Test some simple error messages"""
        try:
            connect(ENV.host, ENV.port, auth_mechanism="foo")
            assert False, "should have got exception"
        except NotSupportedError as e:
            assert 'Unsupported authentication mechanism: FOO' in str(e)


    @pytest.mark.skipif(JWT_DISABLED, reason=JWT_DISABLED_ERROR)
    def test_jwt_auth(self):
        """Test for connecting via the auth_mechanism=JWT"""
        # This is a JWT generated via jwt.io's online generator
        # The content is:
        # Header:
        # {
        #   "alg": "HS256",
        #   "typ": "JWT"
        # }
        # Payload:
        # {
        #   "sub": "1234567890",
        #   "username": "impylajwttest",
        #   "iat": 1516239022
        # }
        # Signature by key "impylaimpylaimpylaimpylaimpylaimp"
        jwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwidXNlcm5hbWUiOiJpbXB5bGFqd3R0ZXN0IiwiaWF0IjoxNTE2MjM5MDIyfQ.Uvq2TZ9nRtM-JgFEd_fL2Z0kFcflx0Tr5cbJR4yySyc"
        self.connection = connect(ENV.host, ENV.http_port, use_http_transport=True,
                                  http_path="cliservice", auth_mechanism="JWT",
                                  timeout=5, jwt=jwt)
        username = self._execute_query_get_username(self.connection)
        assert(username == "impylajwttest")
        print("Username: {0}".format(username))
        self._execute_queries(self.connection)

    @pytest.mark.skipif(JWT_DISABLED, reason=JWT_DISABLED_ERROR)
    def test_jwt_auth_negative(self):
        """Test negative cases for connecting via the auth_mechanism=JWT"""
        # Case 1: Connect without specifying JWT
        try:
            connect(ENV.host, ENV.http_port, use_http_transport=True,
                    http_path="cliservice", auth_mechanism="JWT",
                    timeout=5)
        except NotSupportedError as e:
            assert "JWT authentication requires specifying the 'jwt' argument" in str(e)

        # Case 2: Connect with JWT to non-HTTP
        try:
            connect(ENV.host, ENV.http_port, http_path="cliservice", auth_mechanism="JWT",
                    timeout=5, jwt="dummy.jwt.arg")
        except NotSupportedError as e:
            assert "JWT authentication is only supported for HTTP transport" in str(e)

    @pytest.mark.skipif(SSL_DISABLED, reason=SSL_DISABLED_ERROR)
    def test_ssl_connection_no_cert(self):
        self.connection = connect(ENV.host, ENV.port, timeout=5, use_ssl=True)
        self._execute_queries(self.connection)


    @pytest.mark.skipif(SSL_DISABLED, reason=SSL_DISABLED_ERROR)
    def test_ssl_connection_with_cert(self):
        self.connection = connect(
            ENV.host, ENV.port, use_ssl=True, timeout=5, ca_cert=ENV.ssl_cert)
        self._execute_queries(self.connection)

class ImpalaSocketTests(unittest.TestCase):

    def run_a_query(self):
        with connect(ENV.host, ENV.port) as connection:
            with connection.cursor() as cursor:
                cursor.execute('select 1 as a_number')
                return cursor.fetchall()

    def test_socket_leak(self):
        with SocketTracker() as sockets:
            # there should be no open sockets prior to running query
            assert len(sockets.open_sockets) == 0, 'Expected 0 open sockets, but saw {}'.format(
                sockets.open_sockets)
            # run a query!
            self.run_a_query()
            # the "run_query" method should have caused all sockets to close
            assert len(sockets.open_sockets) == 0, 'Expected 0 open sockets, but saw {}'.format(
                sockets.open_sockets)
