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

import os
import datetime
from copy import copy
from cStringIO import StringIO
import csv

import pandas as pd
from impala.context import ImpalaContext

from impala.util import (as_pandas, _random_id, _py_to_sql_string,
                         _get_table_schema_hack)
from impala._sql_model import (_to_TableName, BaseTableRef, JoinTableRef,
                               SelectItem, SelectStmt, UnionStmt, Literal,
                               InlineView, TableName, Expr, _create_table,
                               _create_table_as_select, LimitElement)


# utilities

def _numpy_dtype_to_impala_PrimitiveType(ty):
    """Convert numpy dtype to Impala type string.

    Used in converting pandas DataFrame to SQL/Impala
    """
    # based on impl in pandas.io.sql.PandasSQLTable._sqlalchemy_type()
    if ty is datetime.date:
        # TODO: this might be wrong
        return 'TIMESTAMP'
    if pd.core.common.is_datetime64_dtype(ty):
        # TODO: this might be wrong
        return 'TIMESTAMP'
    if pd.core.common.is_timedelta64_dtype(ty):
        return 'BIGINT'
    if pd.core.common.is_float_dtype(ty):
        return 'DOUBLE'
    if pd.core.common.is_integer_dtype(ty):
        # TODO: BIGINT may be excessive?
        return 'BIGINT'
    if pd.core.common.is_bool(ty):
        return 'BOOLEAN'
    return 'STRING'


# BigDataFrame creation

def from_sql_query(ic, query, alias=None):
    """Create a BDF from a SQL query executed by Impala"""
    query_alias = alias if alias else _random_id('inline_', 4)
    table_ref = InlineView(query, query_alias)
    schema = _get_table_schema_hack(ic._cursor, table_ref.to_sql())
    select_list = tuple(
        [SelectItem(expr=Literal(col)) for (col, ty) in schema])
    return BigDataFrame(ic, SelectStmt(select_list, table_ref))


def from_sql_table(ic, table):
    """Create a BDF from a table name usable in Impala"""
    table_name = _to_TableName(table)
    table_ref = BaseTableRef(table_name)
    schema = _get_table_schema_hack(ic._cursor, table_ref.to_sql())
    select_list = tuple(
        [SelectItem(expr=Literal(col)) for (col, ty) in schema])
    return BigDataFrame(ic, SelectStmt(select_list, table_ref))


def from_hdfs(ic, path, schema, table=None, overwrite=False,
              file_format='TEXTFILE', partition_schema=None,
              field_terminator='\t', line_terminator='\n', escape_char='\\'):
    """Create a BDF backed by an external file in HDFS.

    File must be Impala-compatible
    """
    if partition_schema is not None:
        raise NotImplementedError(
            "Partitions not yet implemented in .from_hdfs()")
    if table is None:
        temp_table = _random_id('tmp_table_', 8)
        table = "%s.%s" % (ic._temp_db, temp_table)
    table_name = _to_TableName(table)
    if overwrite:
        ic._cursor.execute("DROP TABLE IF EXISTS %s" % table_name.to_sql())
    create_stmt = _create_table(table_name, schema, path=path,
                                file_format=file_format,
                                field_terminator=field_terminator,
                                line_terminator=line_terminator,
                                escape_char=escape_char)
    ic._cursor.execute(create_stmt)
    return from_sql_table(ic, table_name.to_sql())


def from_pandas(ic, df, table=None, path=None, method='in_query',
                file_format='TEXTFILE', field_terminator='\t',
                line_terminator='\n', escape_char='\\', overwrite=False):
    """Create a BDF by shipping an in-memory pandas `DataFrame` into Impala

    path is the dir, not the filename
    """
    # TODO: this is not atomic
    assert isinstance(ic, ImpalaContext)
    temp_table = _random_id('tmp_table_', 8)
    if table is None:
        table = "%s.%s" % (ic._temp_db, temp_table)
    if path is None:
        path = os.path.join(ic._temp_dir, temp_table)
    table_name = _to_TableName(table)
    if overwrite:
        ic._cursor.execute("DROP TABLE IF EXISTS %s" % table_name.to_sql())
    columns = list(df.columns)
    types = [_numpy_dtype_to_impala_PrimitiveType(ty) for ty in df.dtypes]
    schema = zip(columns, types)
    create_stmt = _create_table(table_name, schema, path=path,
                                file_format=file_format,
                                field_terminator=field_terminator,
                                line_terminator=line_terminator,
                                escape_char=escape_char)
    ic._cursor.execute(create_stmt)
    if method == 'in_query':
        query = "INSERT INTO %s VALUES " % table_name.to_sql()
        query += ', '.join(['(%s)' % ', '.join(map(_py_to_sql_string, row))
                            for row in df.values])
        ic._cursor.execute(query)
    elif method == 'webhdfs':
        if file_format != 'TEXTFILE':
            raise ValueError("only TEXTFILE format supported for webhdfs")
        if path is None:
            raise ValueError(
                "must supply a path for EXTERNAL table for webhdfs")
        hdfs_client = ic.hdfs_client()
        raw_data = StringIO()
        df.to_csv(raw_data, sep=field_terminator,
                  line_terminator=line_terminator, quoting=csv.QUOTE_NONE,
                  escapechar=escape_char, header=False, index=False)
        hdfs_client.create_file(
            os.path.join(path, 'data.txt').lstrip('/'), raw_data.getvalue(),
            overwrite=overwrite)
        raw_data.close()
    else:
        raise ValueError(
            "method must be 'in_query' or 'webhdfs'; got %s" % method)
    return from_sql_table(ic, table_name.to_sql())


class BigDataFrame(object):

    def __init__(self, ic, ast):
        self._ic = ic
        self._query_ast = ast
        self._schema = None

    @property
    def schema(self):
        if self._schema is None:
            table_ref = InlineView(
                self._query_ast.to_sql(), _random_id('inline_', 4))
            self._schema = _get_table_schema_hack(
                self._ic._cursor, table_ref.to_sql())
        return self._schema

    @property
    def is_sorted(self):
        if isinstance(self._query_ast, SelectStmt):
            return self._query_ast._order_by is not None
        # TODO: add warning that we're not sure if the BDF is already sorted
        # (e.g., bc this BDF is built directly from an inline view of a user-
        # supplied query string)
        return False

    def __getitem__(self, obj):
        """'Indexing' functionality for the BigDataFrame

        Given a single object or list, the BDF will interpret it as a
        relational projection (i.e., a selection of columns).

        Given a tuple of length 2, the first element will be interpreted for
        row selection (i.e., predicate/filter/WHERE clause), while the second
        element will be interpreted as a projection.
        """
        # other select/filter fns should be implemented with this one
        if isinstance(obj, tuple) and len(obj) == 2:
            alias = _random_id('inline_', 4)
            table_ref = InlineView(self._query_ast.to_sql(), alias)
            (limit_elt, where) = self._query_ast._filter(obj[0])
            select_list = self._query_ast._projection(obj[1])
            return BigDataFrame(
                self._ic, SelectStmt(
                    select_list, table_ref, where=where, limit=limit_elt))
        elif isinstance(obj, list):
            alias = _random_id('inline_', 4)
            table_ref = InlineView(self._query_ast.to_sql(), alias)
            select_list = self._query_ast._projection(obj)
            return BigDataFrame(self._ic, SelectStmt(select_list, table_ref))
        else:
            # single object, possibly a slice; wrap in list and get projection
            return self[[obj]]

    def join(self, other, on=None, how='inner', hint=None):
        """Join this BDF to another one.

        `on` is `None`, `string`, `Expr`, or `list[string]`
        """
        left = InlineView(self._query_ast.to_sql(), 'left_tbl')
        right = InlineView(other._query_ast.to_sql(), 'right_tbl')
        # SELECT left.*, right.*
        select_list = [SelectItem(table_name=TableName(left.name)),
                       SelectItem(table_name=TableName(right.name))]
        table_ref = JoinTableRef(left, right, on=on, op=how, hint=hint)
        ast = SelectStmt(select_list, table_ref)
        return BigDataFrame(self._ic, ast)

    def group_by(self, by):
        """Group the BDF

        `by` is `string`, `Expr`, or `list/tuple[string/Expr]`
        """
        if not isinstance(by, (tuple, list)):
            by = (by,)
        if not all([isinstance(e, (basestring, Expr)) for e in by]):
            raise ValueError("must supply only strings or Exprs")
        by = tuple([e if isinstance(e, Expr) else Literal(e) for e in by])
        table_ref = InlineView(self._query_ast.to_sql(), 'inner_tbl')
        # invalid AST; to be used by GroupBy
        incomplete_ast = SelectStmt([], table_ref, group_by=by)
        return GroupBy(self._ic, incomplete_ast)

    def concat(self, other):
        """Concatenate BDFs using a UNION statement.

        Schemas must be compatible.
        """
        if not isinstance(other, BigDataFrame):
            raise ValueError("other must be a BigDataFrame objects")
        if self.schema != other.schema:
            raise ValueError("schema mismatch")
        ast = UnionStmt([self._query_ast, other._query_ast])
        return BigDataFrame(self._ic, ast)

    def one_hot_categoricals(self, categoricals, prefix=None, dummy_na=False):
        """Convert categorical columns to one-hot encoding.

        categoricals is an iterable of column names that should be treated as
        categorical variables
        """
        # TODO
        raise NotImplementedError
        # unique_values = {}
        # for col in categoricals:
        #     distinct_query = "SELECT DISTINCT %s FROM %s" % (
        #         col, bdf.to_sql())
        #     self._cursor.execute(distinct_query)
        #     unique_values[col] = self._cursor.fetchall()

    def _store(self, path=None, table_name=None, file_format='TEXTFILE',
              field_terminator='\t', line_terminator='\n', escape_char='\\',
              overwrite=False):
        if overwrite:
            self._cursor.execute(
                "DROP TABLE IF EXISTS %s" % table_name.to_sql())
        create_stmt = _create_table_as_select(
            table_name, path=path, file_format=file_format,
            field_terminator=field_terminator, line_terminator=line_terminator,
            escape_char=escape_char)
        query = create_stmt + self.to_sql()
        self._cursor.execute(query)
        return from_sql_table(self._ic, table_name.to_sql())

    def store(self, path=None, table=None, file_format='TEXTFILE',
              field_terminator='\t', line_terminator='\n', escape_char='\\',
              overwrite=False):
        """Materialize the results and stores them in HFDS. Functions as an EXTERNAL table.

        Implemented through a `CREATE TABLE AS SELECT`.
        """
        temp_table = _random_id('tmp_table_', 8)
        if table is None:
            table = "%s.%s" % (self._temp_db, temp_table)
        if path is None:
            path = os.path.join(self._temp_dir, temp_table)
        table_name = _to_TableName(table)
        return self._store(path=path, table_name=table_name, file_format=file_format, field_terminator=field_terminator,
                    line_terminator=line_terminator, escape_char=escape_char, overwrite=overwrite)



    def store_managed(self, table, file_format='PARQUET', field_terminator='\t', line_terminator='\n', escape_char='\\',
              overwrite=False):
        """Materialize the results and stores them in HDFS as an impala managed table.

        Implemented through a `CREATE TABLE AS SELECT`.
        """
        table_name = _to_TableName(table)
        return self._store(path=None, table_name=table_name, file_format=file_format, field_terminator=field_terminator,
            line_terminator=line_terminator, escape_char=escape_char, overwrite=overwrite)


    def save_view(self, name, overwrite=False):
        """Create a named view representing this BDF for later reference"""
        # TODO: is this fn useful?
        table_name = _to_TableName(name)
        if overwrite:
            self._ic._cursor.execute(
                'DROP VIEW IF EXISTS %s' % table_name.to_sql())
        sql = 'CREATE VIEW %s AS %s' % (table_name.to_sql(),
                                        self._query_ast.to_sql())
        self._ic._cursor.execute(sql)
        return from_sql_table(self._ic, table_name.to_sql())

    def __iter__(self):
        """Return an iterator object to iterate over rows locally"""
        self._ic._cursor.execute(self._query_ast.to_sql())
        return self._ic._cursor.__iter__()

    def take(self, n):
        """Return `n` rows as a pandas `DataFrame`

        Distributed and no notion of order, so not guaranteed to be
        reproducible.
        """
        alias = _random_id('inline_', 4)
        table_ref = InlineView(self._query_ast.to_sql(), alias)
        # SELECT alias.*
        select_list = [SelectItem(table_name=TableName(table_ref.name))]
        limit_elt = LimitElement(Literal(n), None)
        ast = SelectStmt(select_list, table_ref, limit=limit_elt)
        bdf = BigDataFrame(self._ic, ast)
        return as_pandas(bdf.__iter__())

    def collect(self):
        """Return the BDF data to the client as a pandas DataFrame"""
        return as_pandas(self.__iter__())

    def count(self):
        count_query = ('SELECT COUNT(*) FROM (%s) AS count_tbl' %
                       self._query_ast.to_sql())
        self._ic._cursor.execute(count_query)
        return self._ic._cursor.fetchall()[0][0]


class GroupBy(object):

    def __init__(self, ic, grouped_ast):
        # NOTE: grouped_ast._select_list gets ignored
        if grouped_ast._group_by is None:
            raise ValueError("GroupBy requires an AST with a valid _group_by")
        self._ic = ic
        self._grouped_ast = grouped_ast

    @property
    def groups(self):
        ast = copy(self._grouped_ast)
        select_list = [SelectItem(expr=e) for e in self._grouped_ast._group_by]
        ast._select_list = tuple(select_list)
        return BigDataFrame(self._ic, ast)

    def __getitem__(self, obj):
        """Expression evaluation against groups.

        Given a single object or list, the GroupBy will interpret it as a set
        of SELECT expressions to evaluate in the context of the GROUP BY.

        Given a tuple of length 2, the first element will be interpreted for
        group selection (i.e., a HAVING clause), while the second element will
        be interpreted as a set of expressions to evaluate against the groups.
        """
        ast = copy(self._grouped_ast)
        if isinstance(obj, tuple) and len(obj) == 2:
            if not isinstance(obj[0], Expr):
                raise ValueError("The group filter (obj[0]) must be Expr type")
            ast._having = obj[0]
            obj = obj[1]
        # obj is now the SELECT portion
        if not isinstance(obj, (list, tuple)):
            obj = [obj]
        select_list = []
        for elt in obj:
            if isinstance(elt, SelectItem):
                select_list.append(elt)
            elif isinstance(elt, basestring):
                select_list.append(SelectItem(expr=Literal(elt)))
            elif isinstance(elt, Expr):
                select_list.append(SelectItem(expr=elt))
        ast._select_list = select_list
        return BigDataFrame(self._ic, ast)
