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

# some inspiration from Dropbox's PyHive

from __future__ import absolute_import

import re

from sqlalchemy.dialects import registry

from sqlalchemy.engine.default import DefaultDialect, DefaultExecutionContext
from sqlalchemy.sql.compiler import (DDLCompiler, GenericTypeCompiler,
                                     IdentifierPreparer)
from sqlalchemy.types import (BOOLEAN, SMALLINT, BIGINT, TIMESTAMP, FLOAT,
                              DECIMAL, Integer, Float, String, CHAR, VARCHAR,
                              DATE)
from sqlalchemy import text


registry.register('impala', 'impala.sqlalchemy', 'ImpalaDialect')
registry.register('impala4', 'impala.sqlalchemy', 'Impala4Dialect')


class TINYINT(Integer):
    __visit_name__ = 'TINYINT'


class INT(Integer):
    __visit_name__ = 'INT'


class DOUBLE(Float):
    __visit_name__ = 'DOUBLE'


class STRING(String):
    __visit_name__ = 'STRING'


class ImpalaDDLCompiler(DDLCompiler):
    # Omit support for foreign keys due to Impala's limited support - https://issues.apache.org/jira/browse/IMPALA-2112
    def visit_foreign_key_constraint(self, constraint):
        return None

    # Omit support for primary keys due to Impala's limited support - https://issues.apache.org/jira/browse/IMPALA-2112
    def visit_primary_key_constraint(self, constraint):
        return None

    def get_column_specification(self, column, **kwargs):
        column.nullable = True  # Prevent adding NOT NULL constraints; since all columns in Impala are nullable
        colspec = super(ImpalaDDLCompiler, self).get_column_specification(
            column, **kwargs
        )
        return colspec

    def post_create_table(self, table):
        """Build table-level CREATE options."""

        table_opts = []

        if 'impala_partitioned_by' in table.kwargs:
            table_opts.append('PARTITIONED BY %s' % table.kwargs.get('impala_partitioned_by'))

        if 'impala_partition_by' in table.kwargs:
            table_opts.append('PARTITION BY %s' % table.kwargs.get('impala_partition_by'))

        if 'impala_stored_as' in table.kwargs:
            table_opts.append('STORED AS %s' % table.kwargs.get('impala_stored_as'))

        if 'impala_table_properties' in table.kwargs:
            table_properties = ["'{0}' = '{1}'".format(property_, value)
                                for property_, value
                                in sorted(table.kwargs.get('impala_table_properties', {}).items())]
            table_opts.append('TBLPROPERTIES (%s)' % ', '.join(table_properties))
        return '\n%s' % '\n'.join(table_opts)


# Impala type compiler for Impala <= 3.4.0
class ImpalaTypeCompiler(GenericTypeCompiler):
    # pylint: disable=unused-argument

    # https://docs.cloudera.com/documentation/enterprise/6/6.3/topics/impala_porting.html
    def visit_TEXT(self, type_):
        return 'STRING'

    visit_NCHAR = visit_TEXT
    visit_NVARCHAR = visit_TEXT

    def visit_DATETIME(self, type_):
        return 'TIMESTAMP'

    # Impala <= 3.4.0 only supports the TIMESTAMP type
    visit_TIME = visit_DATETIME
    visit_DATE = visit_DATETIME

    def visit_TINYINT(self, type_):
        return 'TINYINT'

    def visit_INT(self, type_):
        return 'INT'

    def visit_DOUBLE(self, type_):
        return 'DOUBLE'

    def visit_STRING(self, type_):
        return 'STRING'


# Impala type compiler for Impala >= 4.0
class Impala4TypeCompiler(ImpalaTypeCompiler):
    # Impala >= 4.0 supports the DATE type - https://issues.apache.org/jira/browse/IMPALA-6169
    def visit_DATE(self, type_):
        return 'DATE'

class ImpalaIdentifierPreparer(IdentifierPreparer):
    # https://github.com/cloudera/Impala/blob/master/fe/src/main/jflex/sql-scanner.flex
    reserved_words = frozenset([
        'add', 'aggregate', 'all', 'alter', 'analytic', 'and', 'anti',
        'api_version', 'array', 'as', 'asc', 'avro', 'between', 'bigint',
        'binary', 'boolean', 'by', 'cached', 'case', 'cast', 'change', 'char',
        'class', 'close_fn', 'column', 'columns', 'comment', 'compute',
        'create', 'cross', 'current', 'data', 'database', 'databases', 'date',
        'datetime', 'decimal', 'delimited', 'desc', 'describe', 'distinct',
        'div', 'double', 'drop', 'else', 'end', 'escaped', 'exists', 'explain',
        'external', 'false', 'fields', 'fileformat', 'finalize_fn', 'first',
        'float', 'following', 'for', 'format', 'formatted', 'from', 'full',
        'function', 'functions', 'grant', 'group', 'having', 'if', 'in',
        'init_fn', 'inner', 'inpath', 'insert', 'int', 'integer',
        'intermediate', 'interval', 'into', 'invalidate', 'is', 'join', 'last',
        'left', 'like', 'limit', 'lines', 'load', 'location', 'map',
        'merge_fn', 'metadata', 'not', 'null', 'nulls', 'offset', 'on', 'or',
        'order', 'outer', 'over', 'overwrite', 'parquet', 'parquetfile',
        'partition', 'partitioned', 'partitions', 'preceding', 'prepare_fn',
        'produced', 'range', 'rcfile', 'real', 'refresh', 'regexp', 'rename',
        'replace', 'returns', 'revoke', 'right', 'rlike', 'role', 'roles',
        'row', 'rows', 'schema', 'schemas', 'select', 'semi', 'sequencefile',
        'serdeproperties', 'serialize_fn', 'set', 'show', 'smallint', 'stats',
        'stored', 'straight_join', 'string', 'struct', 'symbol', 'table',
        'tables', 'tblproperties', 'terminated', 'textfile', 'then',
        'timestamp', 'tinyint', 'to', 'true', 'unbounded', 'uncached', 'union',
        'update_fn', 'use', 'using', 'values', 'varchar', 'view', 'when',
        'where', 'with'])

    legal_characters = re.compile(r'^[A-Z0-9_]+$', re.I)

    def __init__(self, dialect):
        super(ImpalaIdentifierPreparer, self).__init__(dialect,
                                                       initial_quote='`')


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
    'DECIMAL': DECIMAL,
    'CHAR': CHAR,
    'VARCHAR': VARCHAR,
    'DATE': DATE
    }

class ImpalaExecutionContext(DefaultExecutionContext):
       def create_cursor(self):
           self._is_server_side = False
           cursor_configuration = self.execution_options.get('cursor_configuration', {})
           return self._dbapi_connection.cursor(configuration=cursor_configuration)


# Dialect to be used with Impala <= 3.4.0
class ImpalaDialect(DefaultDialect):
    name = 'impala'
    driver = 'impala'
    paramstyle = 'pyformat'
    preparer = ImpalaIdentifierPreparer
    max_identifier_length = 128
    supports_sane_rowcount = False
    supports_sane_multi_rowcount = False
    supports_multivalues_insert = True
    supports_sequences = False
    supports_native_decimal = True
    supports_native_boolean = True
    supports_native_enum = False
    supports_default_values = False
    returns_unicode_strings = True
    ddl_compiler = ImpalaDDLCompiler
    type_compiler = ImpalaTypeCompiler
    execution_ctx_cls = ImpalaExecutionContext
    # disable supports_statement_cache explicitly to avoid warning in sqlalchemy.
    # TODO: it is not clear whether it would be safe to enable, needs more research
    supports_statement_cache = False

    # sqlalchemy dbapi() is deprecated in favor of import_dbapi().
    # Keeping both to remain as compatible as possible.
    @classmethod
    def dbapi(cls):
        # pylint: disable=method-hidden
        import impala.dbapi
        return impala.dbapi

    @classmethod
    def import_dbapi(cls):
        # pylint: disable=method-hidden
        import impala.dbapi
        return impala.dbapi

    def create_connect_args(self, url):
        kwargs = {
            'host': url.host,
            'port': url.port,
            'user': url.username,
            'password': url.password,
            'database': url.database,
        }
        kwargs.update(url.query)
        return ([], kwargs)

    def initialize(self, connection):
        self.default_schema_name = connection.connection.default_db

    def _get_server_version_info(self, connection):
        raw = connection.execute(text('select version()')).scalar()
        v = raw.split()[2]
        m = re.match(r'.*?(\d{1,3})\.(\d{1,3})\.(\d{1,3}).*', v)
        return tuple([int(x) for x in m.group(1, 2, 3) if x is not None])

    def has_table(self, connection, table_name, schema=None, **kw):
        tables = self.get_table_names(connection, schema)
        if table_name in tables:
            return True
        return False

    def get_table_names(self, connection, schema=None, **kw):
        query = 'SHOW TABLES'
        if schema is not None:
            escaped_schema = re.sub(r"^[\`]{1,}|[\`]{1,}$", '', schema)
            escaped_schema = re.sub(r"^|$", '`', escaped_schema)
            query += ' IN %s' % escaped_schema
        tables = [
            tup[1] if len(tup) > 1 else tup[0]
            for tup in connection.execute(text(query)).fetchall()
        ]
        return tables

    def get_view_names(self, connection, schema=None, **kw):
        # Impala doesn't distinguish between tables and view when calling
        # SHOW TABLES. So return a blank list.
        return []

    def get_schema_names(self, connection, **kw):
        rp = connection.execute(text("SHOW SCHEMAS"))
        return [r[0] for r in rp]

    def get_columns(self, connection, table_name, schema=None, **kwargs):
        # pylint: disable=unused-argument
        name = table_name
        if schema is not None:
            name = '%s.%s' % (schema, name)
        query = 'SELECT * FROM %s LIMIT 0' % name
        cursor = connection.execute(text(query))
        schema = cursor.cursor.description
        # We need to fetch the empty results otherwise these queries remain in
        # flight
        cursor.fetchall()
        column_info = []
        # `select * from table` results in 'tablename.columnname', so strip off 'tablename.'
        for col in schema:
            column_info.append({
                'name': col[0].split('.')[-1].strip() if '.' in col[0] else col[0],
                'type': _impala_type_to_sqlalchemy_type[col[1]],
                'nullable': True,
                'autoincrement': False})
        return column_info

    def get_pk_constraint(self, connection, table_name, schema=None, **kw):
        # pylint: disable=unused-argument
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


# Dialect to be used with Impala >= 4.0
class Impala4Dialect(ImpalaDialect):
    name = 'impala4'
    driver = 'impala4'
    type_compiler = Impala4TypeCompiler
