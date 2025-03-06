# Copyright 2020 Cloudera Inc.
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
import logging

import six

from thrift.protocol.TBinaryProtocol import TBinaryProtocolAccelerated
# noinspection PyProtectedMember
from impala._thrift_gen.ImpalaService import ImpalaHiveServer2Service

ThriftClient = ImpalaHiveServer2Service.Client

from impala import hiveserver2 as hs2
from impala._thrift_api import ImpalaHttpClient
from impala.error import HttpError
from impala.hiveserver2 import HS2Service
from impala.tests.util import ImpylaTestEnv

ENV = ImpylaTestEnv()


# This code is based on https://github.com/apache/impala/blob/master/tests/custom_cluster/test_hs2_fault_injection.py


class FaultInjectingHttpClient(ImpalaHttpClient, object):
    """Class for injecting faults into ImpalaHttpClient. Faults are injected by using the
    'enable_fault' method. The 'flush' method is overridden to check for injected faults
    and raise exceptions, if needed."""

    def __init__(self, *args, **kwargs):
        super(FaultInjectingHttpClient, self).__init__(*args, **kwargs)
        self.fault_code = None
        self.fault_message = None
        self.fault_enabled = False
        self.num_requests = 0
        self.fault_frequency = 0

    # noinspection PyAttributeOutsideInit
    def enable_fault(self, http_code, http_message, fault_frequency, fault_body=None,
                     fault_headers=None, set_num_requests=None):
        """Inject fault with given code and message at the given frequency.
        As an example, if frequency is 20% then inject fault for 1 out of every 5
        requests."""
        if fault_headers is None:
            fault_headers = {}
        self.fault_enabled = True
        self.fault_code = http_code
        self.fault_message = http_message
        self.fault_frequency = fault_frequency
        assert 0 < fault_frequency <= 1
        if set_num_requests is not None:
            self.num_requests = set_num_requests
        else:
            self.num_requests = 0
        self.fault_body = fault_body
        self.fault_headers = fault_headers

    def disable_fault(self):
        self.fault_enabled = False

    def _check_code(self):
        if self.code >= 300:
            # Report any http response code that is not 1XX (informational response) or
            # 2XX (successful).
            raise HttpError(self.code, self.message, self.body, self.headers)

    def _inject_fault(self):
        if not self.fault_enabled:
            return False
        if self.fault_frequency == 1:
            return True
        if round(self.num_requests % (1 / self.fault_frequency)) == 1:
            return True
        return False

    # noinspection PyAttributeOutsideInit
    def flush(self):
        ImpalaHttpClient.flush(self)
        self.num_requests += 1
        # Override code and message with the injected fault
        if self.fault_code is not None and self._inject_fault():
            self.code = self.fault_code
            self.message = self.fault_message
            self.body = self.fault_body
            self.headers = self.fault_headers
            self._check_code()

    def _read(self, sz):
        """Keep pep8 quiet"""
        pass


# noinspection PyMethodMayBeStatic
class TestHS2FaultInjection(object):
    """Class for testing the http fault injection in various rpcs used by Impyla"""

    def setup_method(self):
        host = "[%s]" % ENV.host if ":" in ENV.host else ENV.host
        url = 'http://%s:%s/%s' % (host, ENV.http_port, "cliservice")
        self.transport = FaultInjectingHttpClient(url)
        self.configuration = {'idle_session_timeout': '30'}

    def teardown_method(self):
        self.transport.disable_fault()

    def connect(self, retries=3):
        self.transport.open()
        protocol = TBinaryProtocolAccelerated(self.transport)
        service = ThriftClient(protocol)
        service = HS2Service(service, retries=retries)
        return hs2.HiveServer2Connection(service, default_db=None)

    def __expect_msg_retry(self, impala_rpc_name, retries):
        """Returns expected log message for rpcs which can be retried"""
        return ("Caught HttpError HTTP code 502: Injected Fault  in {0} (tries_left={1})".
                format(impala_rpc_name, retries))

    def __expect_msg_retry_with_extra(self, impala_rpc_name, retries):
        """Returns expected log message for rpcs which can be retried and where the http
        message has a message body"""
        return ("Caught HttpError HTTP code 503: Injected Fault EXTRA in {0} (tries_left={1})".
                format(impala_rpc_name, retries))

    def __expect_msg_retry_with_retry_after(self, impala_rpc_name, retries):
        """Returns expected log message for rpcs which can be retried and where the http
        message has a body and a Retry-After header that can be correctly decoded"""
        return ("Caught HttpError HTTP code 503: Injected Fault EXTRA in {0} (tries_left={1}), retry after 1 secs".
                format(impala_rpc_name, retries))

    def __expect_msg_retry_with_retry_after_sleep(self):
        """Returns expected log message for the sleep which uses a value
        from the Retry-After header"""
        return ("sleeping after seeing Retry-After value of 1")

    def __expect_msg_retry_after_default_sleep(self):
        """Returns expected log message for the default sleep time of 1 second"""
        return ("sleeping for 1 second before retrying")

    def __expect_msg_retry_with_retry_after_no_extra(self, impala_rpc_name, retries):
        """Returns expected log message for rpcs which can be retried and the http
        message has a Retry-After header that can be correctly decoded"""
        return ("Caught HttpError HTTP code 503: Injected Fault  in {0} (tries_left={1}), retry after 1 secs".
                format(impala_rpc_name, retries))
  
    def __expect_msg_no_retry(self, impala_rpc_name):
        """Returns expected log message for rpcs which can not be retried"""
        return ("Caught HttpError HTTP code 502: Injected Fault  in {0} which is not retryable".
                format(impala_rpc_name))

    def test_connect(self, caplog):
        """Tests fault injection in cursor() call.
        OpenSession rpc fails.
        Retries results in a successful connection."""
        caplog.set_level(logging.DEBUG)
        self.transport.enable_fault(502, "Injected Fault", 0.2)
        con = self.connect(retries=4)
        cur = con.cursor(configuration=self.configuration)
        cur.close()
        con.close()
        assert self.__expect_msg_retry("OpenSession", 4) in caplog.text

    def test_connect_proxy(self, caplog):
        """Tests fault injection in cursor() call.
        The injected error has a message body.
        OpenSession rpc fails.
        Retries results in a successful connection."""
        caplog.set_level(logging.DEBUG)
        self.transport.enable_fault(503, "Injected Fault", 0.20, 'EXTRA')
        con = self.connect(retries=4)
        cur = con.cursor(configuration=self.configuration)
        cur.close()
        con.close()
        assert self.__expect_msg_retry_with_extra("OpenSession", 4) in caplog.text
        assert self.__expect_msg_retry_after_default_sleep() in caplog.text

    def test_connect_proxy_no_retry(self, caplog):
        """Tests fault injection in cursor() call.
        The injected error contains headers but no Retry-After header.
        OpenSession rpc fails.
        Retries results in a successful connection."""
        caplog.set_level(logging.DEBUG)
        self.transport.enable_fault(503, "Injected Fault", 0.20, 'EXTRA',
                                    {"header1": "value1"})
        con = self.connect(retries=4)
        cur = con.cursor(configuration=self.configuration)
        cur.close()
        con.close()
        assert self.__expect_msg_retry_with_extra("OpenSession", 4) in caplog.text
        assert self.__expect_msg_retry_after_default_sleep() in caplog.text

    def test_connect_proxy_bad_retry(self, caplog):
        """Tests fault injection in cursor() call.
        The injected error contains a body and a junk Retry-After header.
        OpenSession rpc fails.
        Retries results in a successful connection."""
        caplog.set_level(logging.DEBUG)
        self.transport.enable_fault(503, "Injected Fault", 0.20, 'EXTRA',
                                    {"header1": "value1",
                                     "Retry-After": "junk"})
        con = self.connect(retries=4)
        cur = con.cursor(configuration=self.configuration)
        cur.close()
        con.close()
        assert self.__expect_msg_retry_with_extra("OpenSession", 4) in caplog.text
        assert self.__expect_msg_retry_after_default_sleep() in caplog.text

    def test_connect_proxy_retry(self, caplog):
        """Tests fault injection in cursor() call.
        The injected error contains a body and a Retry-After header that can be decoded.
        Retries results in a successful connection."""
        caplog.set_level(logging.DEBUG)
        self.transport.enable_fault(503, "Injected Fault", 0.20, 'EXTRA',
                                    {"header1": "value1",
                                     "Retry-After": "1"})
        con = self.connect(retries=4)
        cur = con.cursor(configuration=self.configuration)
        cur.close()
        con.close()
        assert self.__expect_msg_retry_with_retry_after("OpenSession", 4) in caplog.text
        assert self.__expect_msg_retry_with_retry_after_sleep() in caplog.text

    def test_connect_proxy_retry_no_body(self, caplog):
        """Tests fault injection in cursor() call.
        The injected error has no body but does have a Retry-After header that can be decoded.
        Retries results in a successful connection."""
        caplog.set_level(logging.DEBUG)
        self.transport.enable_fault(503, "Injected Fault", 0.20, None,
                                    {"header1": "value1",
                                     "Retry-After": "1"})
        con = self.connect(retries=4)
        cur = con.cursor(configuration=self.configuration)
        cur.close()
        con.close()
        assert self.__expect_msg_retry_with_retry_after_no_extra("OpenSession", 4) in caplog.text

    def test_execute_query(self, caplog):
        """Tests fault injection in execute().
        ExecuteStatement rpc fails and results in error since retries are not supported."""
        con = self.connect()
        cur = con.cursor(configuration=self.configuration)
        caplog.set_level(logging.DEBUG)
        self.transport.enable_fault(502, "Injected Fault", 0.50)

        query_handle = None
        try:
            query_handle = cur.execute('select 1')
            assert False, 'execute should have failed'
        except HttpError as e:
            assert str(e) == 'HTTP code 502: Injected Fault'
        assert query_handle is None
        cur.close()
        con.close()
        assert self.__expect_msg_no_retry("ExecuteStatement") in caplog.text

    def test_get_query_state(self, caplog):
        """Tests fault injection in fetchall().
        GetOperationStatus rpc fails but is retried successfully."""
        con = self.connect(retries=4)
        cur = con.cursor(configuration=self.configuration)
        caplog.set_level(logging.DEBUG)
        cur.execute_async('select 1', {})
        self.transport.enable_fault(502, "Injected Fault", 0.1)
        cur.fetchall()
        cur.close()
        con.close()
        assert self.__expect_msg_retry("GetOperationStatus", 4) in caplog.text

    def test_get_result_set_metadata(self, caplog):
        """Tests fault injection in fetchcbatch().
        GetResultSetMetadata rpc fails and is retried succesfully."""
        con = self.connect(retries=4)
        cur = con.cursor(configuration=self.configuration)
        caplog.set_level(logging.DEBUG)
        cur.execute('select 1', {})
        self.transport.enable_fault(502, "Injected Fault", 0.1)
        cur.fetchcbatch()
        cur.close()
        con.close()
        assert self.__expect_msg_retry("GetResultSetMetadata", 4) in caplog.text

    def test_fetch_results(self, caplog):
        """Tests fault injection in fetchcbatch().
        FetchResults rpc fails and cannot be retried."""
        con = self.connect()
        cur = con.cursor(configuration=self.configuration)
        caplog.set_level(logging.DEBUG)
        cur.execute('select 1', {})
        try:
            self.transport.enable_fault(502, "Injected Fault", 0.5, set_num_requests=1)
            cur.fetchcbatch()
            assert False, 'should see exception'
        except HttpError as e:
            assert str(e) == 'HTTP code 502: Injected Fault'
        self.transport.disable_fault()
        cur.close()
        con.close()
        assert self.__expect_msg_no_retry("FetchResults") in caplog.text

    def test_close_operation(self, caplog):
        """Tests fault injection in fetchcbatch().
        CloseOperation rpc fails and cannot be retried.."""
        con = self.connect()
        cur = con.cursor(configuration=self.configuration)
        caplog.set_level(logging.DEBUG)
        cur.execute('select 1', {})
        cur.fetchcbatch()
        try:
            self.transport.enable_fault(502, "Injected Fault", 0.5)
            cur.close()
        except HttpError as e:
            assert str(e) == 'HTTP code 502: Injected Fault'
        self.transport.disable_fault()
        cur.close()
        con.close()
        assert self.__expect_msg_no_retry("CloseImpalaOperation") in caplog.text

    def test_get_runtime_profile_summary(self, caplog):
        """Tests fault injection in get_profile(), get_summary(), and get_log().
        GetRuntimeProfile, GetExecSummary and GetLog rpcs fail due to fault, but succeed
        after retries"""
        con = self.connect(retries=4)
        cur = con.cursor(configuration=self.configuration)
        caplog.set_level(logging.DEBUG)
        cur.execute('select 1', {})
        cur.fetchcbatch()
        self.transport.enable_fault(502, "Injected Fault", 0.50)
        profile = cur.get_profile()
        assert profile is not None
        summary = cur.get_summary()
        assert summary is not None
        ret_log = cur.get_log()
        assert ret_log is not None
        self.transport.disable_fault()
        cur.close()
        con.close()
        assert self.__expect_msg_retry("GetRuntimeProfile", 4) in caplog.text
        assert self.__expect_msg_retry("GetExecSummary", 4) in caplog.text
        assert self.__expect_msg_retry("GetLog", 4) in caplog.text
