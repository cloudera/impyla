# Copyright 2013 Cloudera Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
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

from __future__ import absolute_import

from impala.util import (_random_id, _py_to_sql_string, _get_table_schema_hack,
                         _gen_safe_random_table_name)


class BlobStore(object):

    def __init__(self, ic, name=None):
        self._ic = ic
        self._name = name

        if self._name is None:
            # TODO: this should take the db name into account when generating
            table_name = _gen_safe_random_table_name(ic._cursor, prefix='blob')
            self._name = "%s.%s" % (self._ic._temp_db, table_name)
            self._create_blob_table()
        self._validate_schema()

    @property
    def name(self):
        return self._name

    def _create_blob_table(self):
        self._ic._cursor.execute("""
                CREATE TABLE %s (
                    key STRING,
                    value STRING)
                STORED AS parquetfile
                """ % self._name)

    def _validate_schema(self):
        schema = _get_table_schema_hack(self._ic._cursor, self.name)
        if len(schema) != 2:
            raise ValueError("schema of blob store must have two cols")
        if schema[0][0] != 'key' or schema[0][1] != 'STRING':
            raise ValueError("first col of blob store must be 'key STRING'")
        if schema[1][0] != 'value' or schema[1][1] != 'STRING':
            raise ValueError("second col of blob store must be 'value STRING'")

    def __getitem__(self, key):
        if not isinstance(key, basestring):
            raise ValueError("key must be a string")
        # TODO: I should make sure to escape single quotes here
        self._ic._cursor.execute("SELECT value FROM %s WHERE key=%s" % (
            self._name, _py_to_sql_string(key)))
        results = self._ic._cursor.fetchall()
        if len(results) == 0:
            raise KeyError("%s not found." % key)
        if len(results) > 1:
            raise KeyError(
                "%s is not unique. Blob store in illegal state." % key)
        return results[0][0]

    def get(self, key):
        return self[key]

    def has_key(self, key):
        # TODO: I should make sure to escape single quotes here
        self._ic._cursor.execute("SELECT COUNT(*) FROM %s WHERE key=%s" % (
            self._name, _py_to_sql_string(key)))
        count = self._ic._cursor.fetchall()[0][0]
        if count == 0:
            return False
        elif count == 1:
            return True
        else:
            raise KeyError(
                "%s is not unique. Blob store in illegal state." % key)

    def send(self, key, value, decode_fn=lambda x: x, safe=False):
        if not isinstance(key, basestring):
            raise ValueError("key must be a string")
        if not isinstance(value, basestring) and value is not None:
            raise ValueError(
                "value must be string-type (possibly binary) or None")

        if safe and key in self:
            raise ValueError("Already have key %s" % key)

        # TODO: I should make sure to escape single quotes here
        decoded_value = decode_fn(value)
        self._ic._cursor.execute("""
                INSERT INTO %s
                VALUES (%s, %s)
                """ % (
            self._name, _py_to_sql_string(key),
            _py_to_sql_string(decoded_value)))

    def put(self, key, expr, from_, safe=False):
        if not isinstance(key, basestring):
            raise ValueError("key must be string")

        if safe and key in self:
            raise ValueError("Already have key %s" % key)

        # TODO: I should make sure to escape single quotes here
        self._ic._cursor.execute("""
                INSERT INTO %s
                SELECT %s, %s
                FROM %s
                """ % (self._name, _py_to_sql_string(key), expr, from_))

    def distribute_value_to_table(self, key, table_name):
        """Distributed value assoc with key to all rows in table_name.

        table_name is the name of a table or view.
        """

        if not isinstance(key, basestring):
            raise ValueError("key must be string")

        from_with_side_data = """
                %(table_name)s CROSS JOIN %(blob_store)s
                WHERE %(blob_store)s.key = %(key)s
                """ % {'table_name': table_name,
                       'blob_store': self.name,
                       'key': _py_to_sql_string(key)}

        return from_with_side_data
