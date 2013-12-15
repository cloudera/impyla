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

Schema is always (key STRING, value STRING).  Can be initialized to an already
existing blob store table.

Supports getting binary data from the store.  Also support putting data in from
Impala (via a SQL query).  Sending data is more fraught, as the data must be
encoded in the query itself.  This is allowed, but you better know what you're
doing.  It also allows you to supply the name of a UDF that will decode ASCII-
encoded data (e.g., Base64).

This command also makes it easier to generate the necessary SQL to distribute
the side data around to other queries (e.g., cross-join).  A typical use case
would be to store model parameters as binary data for UDFs.
"""

import impala.util

def wrap_single_quotes(x):
    return "'%s'" % x

class BlobStore(object):
    
    def __init__(self, cursor, name=None):
        self._cursor = cursor
        self._name = name
        
        if self._name is None:
            self._name = impala.util.generate_random_table_name(prefix='blob',
                    safe=True, cursor=self._cursor)
            self._create_blob_table()
        self._validate_schema()
    
    @property
    def name(self):
        return self._name
    
    def _create_blob_table(self):
        self._cursor.execute("""
                CREATE TABLE %s (
                    key STRING,
                    value STRING)
                STORED AS parquetfile
                """ % self._name)
    
    def _validate_schema(self):
        schema = self._cursor.get_table_schema(self._name)
        if len(schema) != 2:
            raise ValueError("schema of blob store must have two cols")
        if schema[0][0] != 'key' or schema[0][1] != 'STRING_TYPE':
            raise ValueError("first col of blob store must be 'key STRING'")
        if schema[1][0] != 'value' or schema[1][1] != 'STRING_TYPE':
            raise ValueError("second col of blob store must be 'value STRING'")
    
    def __getitem__(self, key):
        if not isinstance(key, basestring):
            raise ValueError("key must be a string")
        # TODO: I should make sure to escape single quotes here
        self._cursor.execute("SELECT value FROM %s WHERE key='%s'" % (self._name, key))
        results = self._cursor.fetchall()
        if len(results) == 0:
            raise KeyError("%s not found." % key)
        if len(results) > 1:
            raise KeyError("%s is not unique. Blob store in illegal state." % key)
        return results[0][0]
    
    def get(self, key):
        return self[key]
    
    def has_key(self, key):
        # TODO: I should make sure to escape single quotes here
        self._cursor.execute("SELECT COUNT(*) FROM %s WHERE key='%s'" % (self._name, key))
        count = self._cursor.fetchall()[0][0]
        if count == 0:
            return False
        elif count == 1:
            return True
        else:
            raise KeyError("%s is not unique. Blob store in illegal state." % key)
    
    def send(self, key, value, decode_fn=wrap_single_quotes, safe=False):
        if not isinstance(key, basestring):
            raise ValueError("key must be a string")
        if not isinstance(value, basestring):
            raise ValueError("value must be string-type (possibly binary)")
        
        if safe and self.has_key(key):
            raise ValueError("Already have key %s" % key)
        
        # TODO: I should make sure to escape single quotes here
        decoded_value = decode_fn(value)
        self._cursor.execute("""
                INSERT INTO %s
                VALUES ('%s', %s)
                """ % (self._name, key, decoded_value))
    
    def send_null(self, key, safe=False):
        self.send(key, 'NULL', decode_fn=lambda x: x, safe=safe)
    
    def put(self, key, expr, from_, safe=False):
        if not isinstance(key, basestring):
            raise ValueError("key must be string")
        
        if safe and self.has_key(key):
            raise ValueError("Already have key %s" % key)
        
        # TODO: I should make sure to escape single quotes here
        self._cursor.execute("""
                INSERT INTO %s
                SELECT '%s', %s
                FROM %s
                """ % (self._name, key, expr, from_))
    
    def distribute_value_to_table(self, key, table_name):
        """Distributed value assoc with key to all rows in table_name.
        
        table_name is the name of a table or view.
        """
        
        if not isinstance(key, basestring):
            raise ValueError("key must be string")
        
        # hack: Impala doesn't let you do a cross join for fear of breaking
        # something.  In order to get a cross join, perform an INNER JOIN using
        # a condition that always evaluates to true.  However, the condition
        # must evaluate a predicate on a column, and cannot simply use literals
        # (e.g., 1 = 1 is not valid).  So we must reference a column in the
        # table_name table.  To do so, we will get the list of columns from the given
        # FROM clause and just choose one of the columns arbitrarily.
        table_schema = self._cursor.get_table_schema(table_name)
        hack_column = table_schema[0][0]
        
        # TODO: I should make sure to escape single quotes here
        from_with_side_data = """
                %(table_name)s INNER JOIN %(blob_store)s
                ON (%(blob_store)s.value is null || true) = (%(table_name)s.%(hack_column)s is null || true)
                WHERE %(blob_store)s.key = '%(key)s'
                """ % {'table_name': table_name,
                       'blob_store': self.name,
                       'key': key,
                       'hack_column': hack_column}
        
        return from_with_side_data
