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
import time

from impala.error import NotSupportedError

if sys.version_info[:2] <= (2, 6):
    import unittest2 as unittest
else:
    import unittest

import pytest

from impala.dbapi import connect, AUTH_MECHANISMS
from impala.util import _random_id
from impala.tests.util import ImpylaTestEnv, SocketTracker

from thrift.transport.TTransport import TTransportException

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

# Table loading / DDLs can take several seconds in Impala. Use a larger timeout to avoid flaky tests.
TIMEOUT_S = 10

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
        self.connection = connect(ENV.host, ENV.port, timeout=TIMEOUT_S)
        self._execute_queries(self.connection)

    @pytest.mark.skipif(ENV.skip_hive_tests, reason="Skipping hive tests")
    def test_hive_plain_connect(self):
        self.connection = connect(ENV.host, ENV.hive_port,
                                  auth_mechanism="PLAIN",
                                  timeout=TIMEOUT_S,
                                  user=ENV.hive_user,
                                  password="cloudera")
        self._execute_queries(self.connection)

    @pytest.mark.skipif(DEFAULT_AUTH, reason=DEFAULT_AUTH_ERROR)
    def test_impala_plain_connect(self):
        self.connection = connect(ENV.host, ENV.port, auth_mechanism="PLAIN",
                                  timeout=TIMEOUT_S,
                                  user=ENV.hive_user,
                                  password="cloudera")
        self._execute_queries(self.connection)

    @pytest.mark.skipif(DEFAULT_AUTH, reason=DEFAULT_AUTH_ERROR)
    def test_impala_ldap_connect_user_agent(self):
        self.connection = connect(ENV.host, ENV.port, auth_mechanism="LDAP",
                                  timeout=TIMEOUT_S,
                                  user=ENV.hive_user,
                                  password="cloudera",
                                  http_path="http-path",
                                  use_http_transport=True,
                                  use_ssl=True,
                                  user_agent="cloudera/impyla")
        self._execute_queries(self.connection)

    @pytest.mark.skipif(DEFAULT_AUTH, reason=DEFAULT_AUTH_ERROR)
    def test_hive_nosasl_connect(self):
        self.connection = connect(ENV.host, ENV.hive_port, timeout=TIMEOUT_S)
        self._execute_queries(self.connection)

    @pytest.mark.params_neg
    def test_bad_auth(self):
        """Test some simple error messages"""
        try:
            connect(ENV.host, ENV.port, auth_mechanism="foo")
            assert False, "'connect' method should have thrown an exception but did not"
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
                                  timeout=TIMEOUT_S, jwt=jwt)
        username = self._execute_query_get_username(self.connection)
        assert(username == "impylajwttest")
        print("Username: {0}".format(username))
        self._execute_queries(self.connection)

    @pytest.mark.params_neg
    def test_jwt_auth_missing_jwt(self):
        """Test for the expected error when JWT auth is used and a JWT is not provided"""
        try:
            connect(use_http_transport=True, auth_mechanism="JWT")
            assert False, "'connect' method should have thrown an exception but did not"
        except NotSupportedError as e:
            assert "JWT authentication requires specifying the 'jwt' argument" in str(e)

    @pytest.mark.params_neg
    def test_jwt_auth_invalid_transport(self):
        """Test for the expected error when JWT auth is used without the HTTP transport"""
        try:
            connect(auth_mechanism="JWT", jwt="dummy.jwt.arg")
            assert False, "'connect' method should have thrown an exception but did not"
        except NotSupportedError as e:
            assert "JWT authentication is only supported for HTTP transport" in str(e)

    @pytest.mark.params_neg
    def test_non_jwt_auth_with_jwt(self):
        """Test for the expected error when authentication is anything other than JWT and the 'jwt' parameter is specified"""
        def run_test(auth_mechanism):
            try:
                connect(auth_mechanism=auth_mechanism, jwt="dummy.jwt.arg")
                assert False, "'connect' method should have thrown an exception but did not"
            except NotSupportedError as e:
                assert "'jwt' argument cannot be specified with '{0}' authentication".format(auth_mechanism) in str(e)

        for auth_mech in AUTH_MECHANISMS:
            if auth_mech is not "JWT":
                run_test(auth_mech)

    @pytest.mark.params_neg
    def test_jwt_auth_with_user(self):
        """Test for the expected error when authentication is JWT and the 'user' parameter is specified"""
        try:
            connect(auth_mechanism="JWT", jwt="dummy.jwt.arg", use_http_transport=True, user="any_user")
            assert False, "'connect' method should have thrown an exception but did not"
        except NotSupportedError as e:
            assert "'user' argument cannot be specified with 'JWT' authentication" in str(e)

    @pytest.mark.params_neg
    def test_jwt_auth_with_ldap_user(self):
        """Test for the expected error when authentication is JWT and the 'ldap_user' parameter is specified"""
        try:
            connect(auth_mechanism="JWT", jwt="dummy.jwt.arg", use_http_transport=True, ldap_user="any_user")
            assert False, "'connect' method should have thrown an exception but did not"
        except NotSupportedError as e:
            assert "'user' argument cannot be specified with 'JWT' authentication" in str(e)

    @pytest.mark.params_neg
    def test_jwt_auth_with_password(self):
        """Test for the expected error when authentication is JWT and the 'password' parameter is specified"""
        try:
            connect(auth_mechanism="JWT", jwt="dummy.jwt.arg", use_http_transport=True, password="any_password")
            assert False, "'connect' method should have thrown an exception but did not"
        except NotSupportedError as e:
            assert "'password' argument cannot be specified with 'JWT' authentication" in str(e)

    @pytest.mark.params_neg
    def test_jwt_auth_with_ldap_password(self):
        """Test for the expected error when authentication is JWT and the 'ldap_password' parameter is specified"""
        try:
            connect(auth_mechanism="JWT", jwt="dummy.jwt.arg", use_http_transport=True, ldap_password="any_password")
            assert False, "'connect' method should have thrown an exception but did not"
        except NotSupportedError as e:
            assert "'password' argument cannot be specified with 'JWT' authentication" in str(e)

    @pytest.mark.skipif(SSL_DISABLED, reason=SSL_DISABLED_ERROR)
    def test_ssl_connection_no_cert(self):
        self.connection = connect(ENV.host, ENV.port, timeout=TIMEOUT_S, use_ssl=True)
        self._execute_queries(self.connection)


    @pytest.mark.skipif(SSL_DISABLED, reason=SSL_DISABLED_ERROR)
    def test_ssl_connection_with_cert(self):
        self.connection = connect(
            ENV.host, ENV.port, use_ssl=True, timeout=TIMEOUT_S, ca_cert=ENV.ssl_cert)
        self._execute_queries(self.connection)

    @pytest.mark.skipif(SSL_DISABLED, reason=SSL_DISABLED_ERROR)
    def test_https_connection(self):
        self.connection = connect(ENV.host, ENV.http_port, use_http_transport=True,
                                  http_path="cliservice", use_ssl=True, timeout=TIMEOUT_S)
        self._execute_queries(self.connection)

    def test_retry_dml(self):
        """Regression test for #549.
        Checks the INSERT statements are not retried when the client disconnects due to timeout
        during execute()."""
        # Connection with higher timeout to avoid errors.
        self.connection = connect(ENV.host, ENV.port, timeout=TIMEOUT_S)
        create = "CREATE TABLE {0} (f1 INT)".format(self.tablename)
        refresh = "REFRESH {0}".format(self.tablename)
        insert = "INSERT INTO TABLE {0} SELECT 1".format(self.tablename)
        select = "SELECT * FROM {0}".format(self.tablename)
        drop = "DROP TABLE {0}".format(self.tablename)
        reliable_cur = self.connection.cursor()
        reliable_cur.execute(create)
        reliable_cur.execute(refresh) # Load table metadata to make subsequent operations faster.
        successful_inserts = 0
        NUM_INSERTS = 3
        for i in range(NUM_INSERTS):
            # Connect with low timeout to trigger failed RPCs.
            LOW_TIMEOUT_S = 1
            low_timeout_connection = connect(ENV.host, ENV.port, timeout=LOW_TIMEOUT_S)
            low_timeout_cur = low_timeout_connection.cursor()
            try:
                # Use IMPALAD_LOAD_TABLES_DELAY>LOW_TIMEOUT_S to trigger timeout.
                # IMPALAD_LOAD_TABLES_DELAY was added in Impala 4.4.0 (IMPALA-12493), so with
                # older Impala servers the test is not expected to work.
                DELAY_S = LOW_TIMEOUT_S + 1
                configuration = {"debug_action": "IMPALAD_LOAD_TABLES_DELAY:SLEEP@{}".format(1000 * DELAY_S)}
                low_timeout_cur.execute(insert, configuration=configuration)
                successful_inserts += 1
            except TTransportException:
                # Sleep until the insert is expected to be finished and close the session.
                SLEEP_S = DELAY_S - LOW_TIMEOUT_S + 2
                time.sleep(SLEEP_S)
                # Reopen the transport to allow closing the session correctly.
                low_timeout_cur.session.client._iprot.trans.close()
                low_timeout_cur.session.client._iprot.trans.open()
                low_timeout_cur.close()
                low_timeout_connection.close()
        assert successful_inserts == 0
        # Use the reliable connection for result checking and cleanup.
        reliable_cur.execute(select)
        result = reliable_cur.fetchall()
        # All inserts must have actually finished after client timeout.
        assert len(result) == NUM_INSERTS
        reliable_cur.execute(drop)
        # If all inserts are successful then probably the Impala cluster is too fast.
        assert successful_inserts < NUM_INSERTS


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
