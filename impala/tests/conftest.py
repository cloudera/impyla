# Copyright 2014 Cloudera Inc.
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

from __future__ import absolute_import

import logging

from pytest import fixture, skip

from impala.dbapi import connect
from impala.util import (
    _random_id, force_drop_impala_database, force_drop_hive_database)
from impala.tests.util import ImpylaTestEnv


# set up some special cmd line options for test running


def pytest_addoption(parser):
    parser.addoption('--connect', action='store_true', default=False,
                     help='Also run DB API 2.0 compliance tests')
    parser.addoption('--log-info', action='store_true', default=False,
                     help='Enable INFO logging')
    parser.addoption('--log-debug', action='store_true', default=False,
                     help='Enable DEBUG logging')


def pytest_configure(config):
    # if both --log-debug and --log-info are set, the DEBUG takes precedence
    if config.getoption('log_debug'):
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.DEBUG)
        root_logger.addHandler(logging.StreamHandler())
    elif config.getoption('log_info'):
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.INFO)
        root_logger.addHandler(logging.StreamHandler())
    config.addinivalue_line("markers", "connect")
    config.addinivalue_line("markers", "params_neg: marks tests that verify invalid parameters are not allowed")

def pytest_runtest_setup(item):
    if (getattr(item.obj, 'connect', None) and
            not item.config.getvalue('connect')):
        skip('--connect not requested (for integration tests)')


# testing fixtures


ENV = ImpylaTestEnv()
hive = ENV.auth_mech == 'PLAIN'


@fixture(scope='session')
def host():
    return ENV.host


@fixture(scope='session')
def port():
    return ENV.port


@fixture(scope='session')
def auth_mech():
    return ENV.auth_mech


@fixture(scope='session')
def tmp_db():
    return _random_id('tmp_impyla_')


@fixture(scope='session')
def con(host, port, auth_mech, tmp_db):
    # create the temporary database
    con = connect(host=host, port=port, auth_mechanism=auth_mech)
    cur = con.cursor()
    cur.execute('CREATE DATABASE {0}'.format(tmp_db))
    cur.close()
    con.close()

    # create the actual fixture
    con = connect(host=host, port=port, auth_mechanism=auth_mech,
                  database=tmp_db)
    yield con
    con.close()

    # cleanup the temporary database
    con = connect(host=host, port=port, auth_mechanism=auth_mech)
    cur = con.cursor()
    if hive:
        force_drop_hive_database(cur, tmp_db)
    else:
        force_drop_impala_database(cur, tmp_db)
    cur.close()
    con.close()


@fixture(scope='session')
def cur(con):
    cur = con.cursor()
    yield cur
    cur.close()

@fixture(scope='session')
def cur_no_string_conv(con):
    cur = con.cursor(convert_types=True, convert_strings_to_unicode=False)
    yield cur
    cur.close()
