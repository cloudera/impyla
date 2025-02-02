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

from __future__ import absolute_import

import base64
import sys
import warnings
import logging
import string
import random
import six
import datetime
import os.path
from six.moves import http_cookies


try:
    from logging import NullHandler
except ImportError:
    # py 2.6 compat
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass


def get_logger_and_init_null(logger_name):
    logger = logging.getLogger(logger_name)
    logger.addHandler(NullHandler())
    return logger


log = get_logger_and_init_null(__name__)


def as_pandas(cursor, coerce_float=False):
    """Return a pandas `DataFrame` out of an impyla cursor.

    This will pull the entire result set into memory.  For richer pandas-like
    functionality on distributed data sets, see the Ibis project.

    Parameters
    ----------
    cursor : `HiveServer2Cursor`
        The cursor object that has a result set waiting to be fetched.
        
    coerce_float : bool, optional
        Attempt to convert values of non-string, non-numeric objects to floating 
        point.

    Returns
    -------
    DataFrame
    """
    from pandas import DataFrame  # pylint: disable=import-error
    names = [metadata[0] for metadata in cursor.description]
    return DataFrame.from_records(cursor.fetchall(), columns=names, 
                                  coerce_float=coerce_float)


def _random_id(prefix='', length=8):
    return prefix + ''.join(random.sample(string.ascii_uppercase, length))


def _get_table_schema_hack(cursor, table):
    """Get the schema of table by talking to Impala

    table must be a string (incl possible db name)
    """
    # get the schema of the query result via a LIMIT 0 hack
    cursor.execute('SELECT * FROM %s LIMIT 0' % table)
    schema = [tup[:2] for tup in cursor.description]
    cursor.fetchall()  # resets the state of the cursor and closes operation
    return schema


def _gen_safe_random_table_name(cursor, prefix='tmp'):
    # unlikely but can be problematic if generated table name is taken in the
    # interim
    tries_left = 3
    while tries_left > 0:
        name = _random_id(prefix, 8)
        if not cursor.table_exists(name):
            return name
        tries_left -= 1
    raise ValueError("Failed to generate a safe table name")


def compute_result_schema(cursor, query_string):
    temp_name = _random_id(prefix="tmp_crs_")
    try:
        cursor.execute("CREATE VIEW %s AS %s" % (temp_name, query_string))
        cursor.execute("SELECT * FROM %s LIMIT 0" % temp_name)
        schema = cursor.description
    finally:
        cursor.execute("DROP VIEW %s" % temp_name)
    return schema


def force_drop_impala_database(cursor, database):
    cursor.execute('USE %s' % database)
    cursor.execute('SHOW TABLES')
    tables = [x[0] for x in cursor.fetchall()]
    for table in tables:
        cursor.execute('DROP TABLE IF EXISTS %s.%s' % (database, table))
    cursor.execute('SHOW FUNCTIONS')
    udfs = [x[1] for x in cursor.fetchall()]
    for udf in udfs:
        cursor.execute('DROP FUNCTION IF EXISTS %s.%s' % (database, udf))
    cursor.execute('SHOW AGGREGATE FUNCTIONS')
    udas = [x[1] for x in cursor.fetchall()]
    for uda in udas:
        cursor.execute('DROP AGGREGATE FUNCTION IF EXISTS %s.%s' % (
                       database, uda))
    cursor.execute('USE default')
    cursor.execute('DROP DATABASE IF EXISTS %s' % database)


def force_drop_hive_database(cursor, database):
    cursor.execute('USE default')
    cursor.execute('DROP DATABASE IF EXISTS {0} CASCADE'.format(database))


def _escape(s):
    e = s
    e = e.replace('\\', '\\\\')
    e = e.replace('\n', '\\n')
    e = e.replace('\r', '\\r')
    e = e.replace("'", "\\'")
    e = e.replace('"', '\\"')
    log.debug('%s => %s', s, e)
    return e


def _py_to_sql_string(value):
    if value is None:
        return 'NULL'
    elif isinstance(value, six.string_types):
        return "'" + _escape(value) + "'"
    else:
        return str(value)


# Logging-related utils


def warn_protocol_param():
    msg = ("Specifying the protocol argument is no longer necessary because "
           "impyla only supports HiveServer2.")
    warnings.warn(msg, Warning)


def warn_deprecate(functionality='This', alternative=None):
    msg = ("{0} functionality in impyla is now deprecated and will be removed "
           "in a future release".format(functionality))
    if alternative:
        msg += "; Please use {0} instead.".format(alternative)
    warnings.warn(msg, Warning)


def warn_nontls_jwt():
    msg = ("JWT authentication is running without SSL/TLS. This is not a secure "
           "configuration unless other layers are providing transport security.")
    warnings.warn(msg, Warning)

# Cookie-related utils


def cookie_matches_path(c, path):
    if 'path' not in c or not c['path']:
        return True
    cookie_path = c['path'].strip()
    if not cookie_path.startswith('/'):
        cookie_path = '/' + cookie_path
    cookie_path = os.path.normpath(cookie_path)
    if cookie_path == '/':
        return True
    if not path.startswith('/'):
        path = '/' + path
    path = os.path.normpath(path)
    return path == cookie_path or path.startswith(cookie_path + '/')


def get_cookie_expiry(c):
    if 'max-age' in c and c['max-age']:
        try:
            max_age_sec = int(c['max-age'])
            return datetime.datetime.now() + datetime.timedelta(seconds=max_age_sec)
        except:
            pass
    # TODO: implement support for 'expires' cookie attribute as well.
    return None


def get_cookies(resp_headers):
    """Returns a SimpleCookie containing all Set-Cookie entries in resp_headers."""
    if 'Set-Cookie' not in resp_headers:
        return None

    cookies = http_cookies.SimpleCookie()
    try:
        if sys.version_info.major == 2:
            cookies.load(resp_headers['Set-Cookie'])
        else:
            cookie_headers = resp_headers.get_all('Set-Cookie')
            for header in cookie_headers:
                cookies.load(header)
        return cookies
    except Exception:
        return None


def get_all_cookies(path, resp_headers):
    """Return cookies that match path.

    Returns a list of Morsel objects representing cookie key/value pairs for all cookies
    in resp_headers matching path."""
    cookies = get_cookies(resp_headers)
    if not cookies:
        return None

    matching_cookies = []
    for c in cookies.values():
        if c and cookie_matches_path(c, path):
            matching_cookies.append(c)
    return matching_cookies


def get_all_matching_cookies(cookie_names, path, resp_headers):
    """Return cookies in cookie_names that match path.

    Returns a list of Morsel objects representing cookie key/value pairs for cookies
    in resp_headers matching path where the cookie is also listed in cookie_names."""
    cookies = get_cookies(resp_headers)
    if not cookies:
        return None

    matching_cookies = []
    for cn in cookie_names:
        if cn in cookies:
            c = cookies[cn]
            if c and cookie_matches_path(c, path):
                matching_cookies.append(c)
    return matching_cookies


def get_basic_credentials_for_request_headers(user, password):
    """Returns base64 encoded credentials for HTTP request headers

    This function produces RFC 2617-compliant basic credentials:
    - RFC 2045 encoding of username:password without limitations to 76 chars
      per line (and without trailing newline)
    - No translation of characters (+,/) for URL-safety
    """
    user_password = '%s:%s' % (user, password)
    return base64.b64encode(user_password.encode()).decode()
