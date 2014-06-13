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

import time
import string
import random

try:
    import pandas as pd    
    def as_pandas(cursor):
        names = [metadata[0] for metadata in cursor.description]
        return pd.DataFrame([dict(zip(names, row)) for row in cursor], columns=names)
except ImportError:
    print "Failed to import pandas"

def generate_random_table_name(prefix='tmp', safe=False, cursor=None):
    # unlikely but can be problematic if generated table name is taken in the interim
    tries_left = 3
    while tries_left > 0:
        date = time.localtime(time.time())
        date_string = "%04i%02i%02i%02i%02i%02i" % (date.tm_year, date.tm_mon,
                date.tm_mday, date.tm_hour, date.tm_min, date.tm_sec)
        random_string = ''.join(random.sample(string.ascii_lowercase, 8))
        name = "%s%s%s" % (prefix, date_string, random_string)
        if safe == False:
            return name
        # safe is True; check cursor
        if cursor is None:
            raise ValueError("Must supply a cursor for safe table name gen")
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