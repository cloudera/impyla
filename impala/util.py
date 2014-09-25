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

import time
import string
import random

try:
    import pandas as pd
    def as_pandas(cursor):
        names = [metadata[0] for metadata in cursor.description]
        return pd.DataFrame.from_records(cursor.fetchall(), columns=names)
except ImportError:
    print "Failed to import pandas"

def _random_id(prefix='', length=8):
    return prefix + ''.join(random.sample(string.ascii_uppercase, length))

def _get_schema_hack(cursor, table_ref):
    """Get the schema of TableRef by talking to Impala"""
    # get the schema of the query result via a LIMIT 0 hack
    # table_ref is a TableRef object
    cursor.execute('SELECT * FROM %s LIMIT 0' % table_ref.to_sql())
    schema = [tup[:2] for tup in cursor.description]
    cursor.fetchall() # resets the state of the cursor and closes operation
    return schema

def _gen_safe_random_table_name(cursor, prefix='tmp'):
    # unlikely but can be problematic if generated table name is taken in the interim
    tries_left = 3
    while tries_left > 0:
        name = _random_id(prefix, 8)
        if not cursor.table_exists(name):
            return name
        tries_left -= 1
    raise ValueError("Failed to generate a safe table name")

def compute_result_schema(cursor, query_string):
    temp_name = generate_random_table_name(safe=True, cursor=cursor)
    try:
        cursor.execute("CREATE VIEW %s AS %s" % (temp_name, query_string))
        cursor.execute("SELECT * FROM %s LIMIT 0" % temp_name)
        schema = cursor.description
    finally:
        cursor.execute("DROP VIEW %s" % temp_name)
    return schema

def create_view_from_query(cursor, query_string, view_name=None, safe=False):
    if view_name is None:
        view_name = generate_random_table_name(safe=safe, cursor=cursor)
    cursor.execute("CREATE VIEW %s AS %s" % (view_name, query_string))
    return view_name

def drop_view(cursor, view_name):
    cursor.execute("DROP VIEW %s" % view_name)

def _escape(s):
    e = s
    e = e.replace('\\', '\\\\')
    e = e.replace('\n', '\\n')
    e = e.replace('\r', '\\r')
    e = e.replace("'", "\\'")
    e = e.replace('"', '\\"')
    return e

def _py_to_sql_string(value):
    if value is None:
        return 'NULL'
    elif isinstance(value, basestring):
        return "'" + _escape(value) + "'"
    else:
        return str(value)
