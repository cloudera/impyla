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

"""
Implements a blob store backed by an Impala table.

Schema is always (key BIGINT, value STRING), and should always have at least a
row (0, NULL).  Can be initialized to an already existing blob store table.

Supports getting binary data from the store.  Setting data is more fraught, as
the data must be encoded in the query itself.  This is allowed, but you better
know what you're doing.  It allows you to supply the name of a UDF that will
decode ASCII-encoded data (e.g., Base64). 

You do not have control over the keys.  They are increasing integers, and
putting data into the table should always use the next higher key.  This is not
rigorously checked when adding data (indeed, adding data from Impala (without
using BlobStore) makes it impossible).

This command also makes it easier to generate the necessary SQL to distribute
the side data around to other queries (e.g., cross-join).  A typical use case
would be to store model parameters as binary data for UDFs.
"""

import impala.util

class BlobStore(object):
    
    def __init__(self, cursor, name=None):
        self._cursor = cursor
        self._name = name
        self._max_key = None
        
        if self._name is None:
            self._name = impala.util.generate_random_table_name(prefix='blob',
                    safe=True, cursor=self._cursor)
            self._create_blob_table()
        self._validate_schema()
        self._refresh_max()
    
    @property
    def max_key(self):
        return self._max_key
    
    def _create_blob_table(self):
        self._cursor.execute("""
                CREATE TABLE %s (
                    key BIGINT,
                    value STRING)
                STORED AS parquetfile
                """ % self._name)
        self._cursor.execute("""
                INSERT INTO %s
                VALUES (0, NULL)
                """ % self._name)
    
    def _validate_schema(self):
        schema = self._cursor.get_schema(self._name)
        if len(schema) != 2:
            raise ValueError("schema of blob store must have two cols")
        if schema[0][0] != 'key' or schema[0][1] != 'BIGINT_TYPE':
            raise ValueError("first col of blob store must be key BIGINT")
        if schema[1][0] != 'value' or schema[1][1] != 'STRING_TYPE':
            raise ValueError("second col of blob store must be value STRING")
        self._cursor.execute("SELECT * WHERE key=0")
        results = self._cursor.fetchall()
        if len(results) != 1:
            raise ValueError("blob store must have a single row with key 0")
        if results[0][0] != 0:
            raise ValueError("query is f-ed up")
        if results[0][1] is not None:
            raise ValueError("key=0 should have value=NULL")
    
    def _refresh_max(self):
        self._cursor.execute("SELECT max(key) FROM %s" % self._name)
        self._max_key = self._cursor.fetchall()[0][0]
    
    def __getitem__(self, key):
        if not isinstance(key, int):
            raise ValueError("key must be integer")
        if key > self._max_key:
            raise KeyError("key=%i is greater than the max key value" % self._max_key)
        self._cursor.execute("SELECT value FROM %s WHERE key=%i" % (self._name, key))
        return self._cursor.fetchall()[0][0]
    
    def get(self, key):
        return self[key]
    
    def put(self, key, value, decode_fn=None):
        if not isinstance(key, int):
            raise ValueError("key must be int")
        if not isinstance(value, basestring):
            raise ValueError("value must be string-type (possibly binary)")
        if key != self._max_key + 1:
            raise ValueError("key must be one greater than current max_key")
        
        decoded_value = value if not decode_fn else '%s(%s)' % (decode_fn, value)
        self._cursor.execute("""
                INSERT INTO %s
                VALUES (%i, %s)
                """ % (self._name, key, decoded_value))
        self._max_key = key
    
    def put_sql(self, key, value):
        if not isinstance(key, int):
            raise ValueError("key must be int")
        if not isinstance(value, basestring):
            raise ValueError("value must be string-type (possibly binary)")
        if key != self._max_key + 1:
            raise ValueError("key must be one greater than current max_key")
        
        INSERT INTO %s SELECT %i, %s