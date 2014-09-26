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

import re

from sqlalchemy.dialects import registry
from sqlalchemy.dialects.postgresql.base import PGDialect
from sqlalchemy.engine.default import DefaultDialect
from sqlalchemy.types import (BOOLEAN, SMALLINT, BIGINT, TIMESTAMP, FLOAT,
        DECIMAL, Integer, Float, String)
from sqlalchemy.sql import compiler

registry.register('impala', 'impala.sqlalchemy', 'ImpalaDialect')


class TINYINT(Integer):
    __visit_name__ = 'TINYINT'


class INT(Integer):
    __visit_name__ = 'INT'


class DOUBLE(Float):
    __visit_name__ = 'DOUBLE'


class STRING(String):
    __visit_name__ = 'STRING'

_impala_type_to_sqlalchemy_type = {
        'BOOLEAN': BOOLEAN,
        'TINYINT': TINYINT,
        'SMALLINT': SMALLINT,
        'INT': INT,
        'BIGINT': BIGINT,
        'TIMESTAMP': TIMESTAMP,
        'FLOAT': FLOAT,
        'DOUBLE': DOUBLE,
        'STRING': STRING,
        'DECIMAL': DECIMAL}


class ImpalaIdentifierPreparer(compiler.IdentifierPreparer):
    """Impala uses backticks as quote characters."""

    def __init__(self, dialect, initial_quote='`',
                    final_quote=None, escape_quote='`', omit_schema=False):
        super(ImpalaIdentifierPreparer).__init__(dialect, initial_quote=initial_quote, final_quote=final_quote,
                                                escape_quote=escape_quote, omit_schema=omit_schema)


class ImpalaDialect(DefaultDialect):
    name = 'impala'
    driver = 'impala'
    paramstyle = 'pyformat'
    max_identifier_length = 128
    supports_sane_rowcount = False
    supports_sane_multi_rowcount = False
    supports_sequences = False
    supports_native_decimal = True
    supports_native_boolean = True
    supports_native_enum = False
    supports_default_values = False
    returns_unicode_strings = True
    preparer = ImpalaIdentifierPreparer

    @classmethod
    def dbapi(self):
        import impala.dbapi
        return impala.dbapi

    def initialize(self, connection):
        self.server_version_info = self._get_server_version_info(connection)
        self.default_schema_name = connection.connection.default_db

    def _get_server_version_info(self, connection):
        raw = connection.execute('select version()').scalar()
        v = raw.split()[2]
        m = re.match('(\d{1,3})\.(\d{1,3})\.(\d{1,3}).*', v)
        return tuple([int(x) for x in m.group(1, 2, 3) if x is not None])

    def has_table(self, connection, table_name, schema=None):
        tables = self.get_table_names(connection, schema)
        if table_name in tables:
            return True
        return False

    def get_table_names(self, connection, schema=None, **kw):
        query = 'SHOW TABLES'
        if schema is not None:
            query += ' IN %s' % schema
        return [tup[0] for tup in connection.execute(query).fetchall()]

    def get_columns(self, connection, table_name, schema=None, **kwargs):
        name = table_name
        if schema is not None:
            name = '%s.%s' % (schema, name)
        query = 'SELECT * FROM %s LIMIT 0' % name
        cursor = connection.execute(query)
        schema = cursor.cursor.description
        # We need to fetch the empty results otherwise these queries remain in flight
        cursor.fetchall()
        column_info = []
        for col in schema:
            column_info.append({
                'name': col[0],
                'type': _impala_type_to_sqlalchemy_type[col[1]],
                'nullable': True,
                'autoincrement': False})
        return column_info

    def get_pk_constraint(self, connection, table_name, schema=None, **kw):
        # no primary keys in impala
        return {'constrained_columns': [], 'name': None}

    def get_foreign_keys(self, connection, table_name, schema=None, **kw):
        # no foreign keys in impala
        return []

    def get_indexes(self, connection, table_name, schema=None, **kw):
        # no indexes in impala
        # TODO(laserson): handle partitions, like in PyHive
        return []

    def do_rollback(self, dbapi_connection):
        # no transactions in impala
        pass

    def create_connect_args(self, url):
        _, opts = super(ImpalaDialect, self).create_connect_args(url)
        if 'port' not in opts:
            opts['port'] = 21050
        return ([], opts)

