import os

import pytest

from impala._thrift_api import ImpalaHttpClient


@pytest.fixture()
def proxy_env():
    reset_value = os.environ.get("HTTPS_PROXY")
    os.environ["HTTPS_PROXY"] = "https://foo:%3F%40%3D@localhost"
    yield "proxy_env"
    if reset_value is None:
        del os.environ["HTTPS_PROXY"]
    else:
        os.environ["HTTPS_PROXY"] = reset_value


class TestHttpTransport(object):
    def test_proxy_auth_header(self, proxy_env):
        client = ImpalaHttpClient(
            uri_or_host="https://localhost:443/cliservice",
        )
        assert client.proxy_auth == "Basic Zm9vOj9APQ=="
