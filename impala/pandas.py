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
import string
import random
import datetime
from copy import copy
from cStringIO import StringIO

import pandas as pd

from .dbapi import connect, _py_to_sql_string
from .util import as_pandas

# some rando utilities

_null_slice = slice(None, None, None)

# Here we map the TTypeId types from TCLIService (which are returned for schema
# results by the RPC/DBAPI tools) back to the Impala-recognized types (i.e.,
# com.cloudera.impala.catalog.PrimitiveType); this is the inverse of the
_TTypeId_to_PrimitiveType = {
	'BOOLEAN_TYPE': 'BOOLEAN',
	'TINYINT_TYPE': 'TINYINT',
	'SMALLINT_TYPE': 'SMALLINT',
	'INT_TYPE': 'INT',
	'BIGINT_TYPE': 'BIGINT',
	'TIMESTAMP_TYPE': 'TIMESTAMP',
	'FLOAT_TYPE': 'FLOAT',
	'DOUBLE_TYPE': 'DOUBLE',
	'STRING_TYPE': 'STRING',
	'DECIMAL_TYPE': 'DECIMAL',
}

def _random_id(prefix='', length=8):
    return prefix + ''.join(random.sample(string.ascii_uppercase, length))

def _get_schema_hack(cursor, table_ref):
    # get the schema of the query result via a LIMIT 0 hack
    cursor.execute('SELECT * FROM %s LIMIT 0' % table_ref.to_sql())
    schema = [tup[:2] for tup in cursor.description]
    cursor.fetchall() # resets the state of the cursor and closes operation
    return schema

def _to_TableName(table):
    if not isinstance(table, basestring):
	raise ValueError("table must be a string")
    if table == '':
	raise ValueError("table must not be the empty string")
    fields = table.split('.')
    if len(fields) == 2:
	db = fields[0]
	name = fields[1]
    elif len(fields) == 1:
	db = None
	name = fields[0]
    else:
	raise ValueError("your value for table (%s) is weird" % table)
    return TableName(name, db)

def _numpy_dtype_to_impala_PrimitiveType(ty):
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

def _register_table(cursor, table_name, table_schema, path=None,
	file_format='TEXTFILE', partition_schema=None, field_terminator='\\t',
	line_terminator='\\n'):
    external = path is not None
    if external:
	query = "CREATE EXTERNAL TABLE %s" % table_name.to_sql()
    else:
	query = "CREATE TABLE %s" % table_name.to_sql()
    schema_string = ', '.join(['%s %s' % (col, ty) for (col, ty) in table_schema])
    query += " (%s)" % schema_string
    if partition_schema:
	schema_string = ', '.join(['%s %s' % (col, ty) for (col, ty) in partition_schema])
	query += " PARTITIONED BY (%s)" % schema_string
    if file_format == 'PARQUET':
	query += " STORED AS PARQUET"
    elif file_format == 'TEXTFILE':
	query += ((" ROW FORMAT DELIMITED FIELDS TERMINATED BY '%s' "
		   "LINES TERMINATED BY '%s' STORED AS TEXTFILE") %
		   (field_terminator, line_terminator))
    if external:
	query += " LOCATION '%s'" % path
    cursor.execute(query)


# PUBLIC API

class ImpalaContext(object):
    # TODO: need to clean up temporary stuff

    def __init__(self, temp_dir=None, temp_db=None, *args, **kwargs):
	# args and kwargs get passed directly into impala.dbapi.connect()
	suffix = _random_id(length=8)
	self._temp_dir = '/tmp/bdf-%s' % suffix if temp_dir is None else temp_dir
	self._temp_db = 'tmp_bdf_%s' % suffix if temp_db is None else temp_db
	self._conn = connect(*args, **kwargs)
	self._cursor = self._conn.cursor()
	if temp_db is None:
	    self._cursor.execute("CREATE DATABASE %s LOCATION '%s'" %
		    (self._temp_db, self._temp_dir))

    def read_sql_query(self, query, alias=None):
	"""Create a BDF from a SQL query executed by Impala"""
	query_alias = alias if alias else _random_id('inline_', 4)
	table_ref = InlineView(query, query_alias)
	schema = _get_schema_hack(self._cursor, table_ref)
	select_list = tuple([SelectItem(expr=Literal(col)) for (col, ty) in schema])
	return BigDataFrame(self, SelectStmt(select_list, table_ref))

    def read_sql_table(self, table):
	"""Create a BDF from a table name usable in Impala"""
	table_name = _to_TableName(table)
	table_ref = BaseTableRef(table_name)
	schema = _get_schema_hack(self._cursor, table_ref)
	select_list = tuple([SelectItem(expr=Literal(col)) for (col, ty) in schema])
	return BigDataFrame(self, SelectStmt(select_list, table_ref))

    def from_pandas(self, df, table=None, path=None, method='in_query',
	    file_format='TEXTFILE', field_terminator='\\t', line_terminator='\\n',
	    hdfs_host=None, webhdfs_port=50070, hdfs_user=None, overwrite=False):
	"""Create a BDF by shipping an in-memory pandas `DataFrame` into Impala"""
	# TODO: this is not atomic
	suffix = _random_id('tmp_table_', 8)
	if table is None:
	    table = "%s.%s" % (self._temp_db, suffix)
	if path is None:
	    path = os.path.join(self._temp_dir, suffix)
	table_name = _to_TableName(table)
	if overwrite:
	    self._cursor.execute("DROP TABLE IF EXISTS %s" % table_name.to_sql())
	columns = list(df.columns)
	types = [_numpy_dtype_to_impala_PrimitiveType(ty) for ty in df.dtypes]
	schema = zip(columns, types)
	_register_table(self._cursor, table_name, schema, path=path,
		file_format=file_format, field_terminator=field_terminator,
		line_terminator=line_terminator)
	if method == 'in_query':
	    query = "INSERT INTO %s VALUES " % table_name.to_sql()
	    query += ', '.join(['(%s)' % ', '.join(map(_py_to_sql_string, row)) for row in df.values])
	    self._cursor.execute(query)
	elif method == 'webhdfs':
	    if file_format != 'TEXTFILE':
		raise ValueError("only TEXTFILE format supported for webhdfs")
	    if path is None:
		raise ValueError("must supply a path for EXTERNAL table for webhdfs")
	    from pywebdfs.webhdfs import PyWebHdfsClient
	    hdfs_client = PyWebHdfsClient(host=hdfs_host, port=webhdfs_port,
		    user=hdfs_user)
	    raw_data = StringIO()
	    df.to_csv(raw_data, sep=field_terminator,
		    line_terminator=line_terminator, header=False, index=False)
	    hdfs_client.create_file(path.lstrip('/'), raw_data.getvalue(), overwrite=overwrite)
	    raw_data.close()
	else:
	    raise ValueError("method must be 'in_query' or 'webhdfs'; got %s" % method)
	return self.read_sql_table(table_name.to_sql())


class BigDataFrame(object):

    def __init__(self, ic, ast):
	self._ic = ic
	self._query_ast = ast

    def __iter__(self):
	"""Return an iterator object to iterate over rows locally"""
	self._ic._cursor.execute(self._query_ast.to_sql())
	return self._ic._cursor.__iter__()

    def store(self, path, name=None):
	"""Materialize the results and stores them in HFDS

	Implemented through a `CREATE TABLE AS SELECT`.
	"""
	raise NotImplementedError
	# TODO: finish this
	sql = 'CREATE TABLE %s AS %s STORED AS %s ...' % (name,
		self._query_ast.to_sql())
	cursor.execute(sql)
	return read_sql_table(cursor, name)

    def save_view(self, name, overwrite=False):
	"""Create a named view representing this BDF for later reference"""
	table_name = _to_TableName(name)
	if overwrite:
	    self._ic._cursor.execute('DROP VIEW IF EXISTS %s' % table_name.to_sql())
	sql = 'CREATE VIEW %s AS %s' % (table_name.to_sql(),
		self._query_ast.to_sql())
	self._ic._cursor.execute(sql)
	return self._ic.read_sql_table(table_name.to_sql())

    def take(self, n):
	"""Return `n` rows as a pandas `DataFrame`

	Distributed and no notion of order, so not guaranteed to be
	reproducible.
	"""
	ast = copy(self._query_ast)
	# compute the new LIMIT expression
	if ast._limit:
	    offset_expr = ast._limit._offset_expr
	    orig_limit_string = ast._limit._limit_expr.to_sql()
	    new_limit_string = ("CASE WHEN (%s) < %i THEN (%s) ELSE %i END" %
		    (orig, n, orig, n))
	    limit_elt = LimitElement(Literal(new_limit_string), offset_expr)
	else:
	    limit_elt = LimitElement(Literal(n), None)
	ast._limit = limit_elt
	bdf = BigDataFrame(self._ic, ast)
	return as_pandas(bdf.__iter__())

    def head(self, n):
	"""Return `n` rows as a pandas `DataFrame`

	Distributed and no notion of order, so not guaranteed to be
	reproducible.
	"""
	return self.take(n)

    def tail(self, n):
	"""Return `n` rows as a pandas `DataFrame`

	Distributed and no notion of order, so not guaranteed to be
	reproducible.
	"""
	return self.take(n)

    # for emulation of Pandas API
    @property
    def ix(self):
	return self

    def __getitem__(self, obj):
	"""'Indexing' functionality for the BigDataFrame

	Given a single object, the BDF will interpret it as a relational
	projection (i.e., a selection of columns).

	Given a tuple of length 2, the first element will be interpreted for row
	selection (i.e., predicate or WHERE clause), while the second element
	will be interpreted as a projection.
	"""
	if isinstance(obj, tuple) and len(obj) == 2:
	    alias = _random_id('inline_', 4)
	    table_ref = InlineView(self._query_ast.to_sql(), alias)
	    (limit_elt, where) = self._getitem_filter(obj[0])
	    select_list = self._getitem_projection(obj[1])
	    return BigDataFrame(self._ic, SelectStmt(select_list, table_ref, where=where, limit=limit_elt))
	elif isinstance(obj, list):
	    alias = _random_id('inline_', 4)
	    table_ref = InlineView(self._query_ast.to_sql(), alias)
	    select_list = self._getitem_projection(obj)
	    return BigDataFrame(self._ic, SelectStmt(select_list, table_ref))
	else:
	    # single object, possibly a slice; wrap in list and get projection
	    return self[[obj]]

    def _getitem_projection(self, obj):
	# obj is list; possible types would be:
	# int, string, expr, slice, SelectItem
	# need to convert to list of SelectItems
	select_list = []
	for elt in obj:
	    if isinstance(elt, SelectItem):
		select_list.append(elt)
	    elif isinstance(elt, basestring):
		select_list.append(SelectItem(expr=Literal(elt)))
	    elif isinstance(elt, Expr):
		select_list.append(SelectItem(expr=elt))
	    elif isinstance(elt, (int, long)):
		select_list.append(self._query_ast._select_list[elt])
	    elif isinstance(elt, slice):
		# slices are relative to the query_ast select_list
		# must be either integers or strings; if strings, must be
		# findable in the select list; slice finally converted to range
		if elt == _null_slice:
		    # take all columns
		    select_list.extend(self._query_ast._select_list)
		    continue
		col_strings = [s.name for s in self._query_ast._select_list]
		# get start index
		if isinstance(elt.start, basestring):
		    start = col_strings.index(elt.start)
		elif isinstance(elt.start, (int, long)):
		    start = elt.start
		elif elt.start is None:
		    start = 0
		else:
		    raise ValueError("slice.start must be string/int/long")
		# get stop index
		if isinstance(elt.stop, basestring):
		    stop = col_strings.index(elt.stop)
		elif isinstance(elt.stop, (int, long)):
		    stop = elt.stop
		elif elt.stop is None:
		    stop = len(self._query_ast._select_list)
		else:
		    raise ValueError("slice.stop must be string/int/long")
		# get step value
		if isinstance(elt.step, (int, long)):
		    step = elt.step
		elif step is None:
		    step = 1
		else:
		    raise ValueError("slice.step must be int/long")
		# finally pull out the corresponding SelectItem objects
		for i in range(start, stop, step):
		    select_list.append(self._query_ast._select_list[i])
	return select_list

    def _getitem_filter(self, obj):
	# obj is one of int, expr, slice
	# to be converted to a pair of LimitElement and Expr
	if isinstance(obj, (int, long)):
	    return (LimitElement(1, obj), None)
	if isinstance(obj, Expr):
	    return (None, obj)
	if isinstance(obj, slice):
	    if obj.step != 1 and obj.step is not None:
		raise ValueError("slices can only have a step size of 1")
	    if (not isinstance(obj.start, (int, long)) or
		    not isinstance(obj.stop, (int, long))):
		raise ValueError("slice stop and start must be int/long")
	    return (LimitElement(obj.stop - obj.start, obj.start), None)
	raise ValueError("row indexer must be int/long/slice/Expr")

    def join(self, other, on=None, how='inner', hint=None):
	left = InlineView(self._query_ast.to_sql(), 'left_tbl')
	right = InlineView(other._query_ast.to_sql(), 'right_tbl')
	# SELECT left.*, right.*
	select_list = [SelectItem(table_name=TableName(left.name)),
		       SelectItem(table_name=TableName(right.name))]
	table_ref = JoinTableRef(left, right, on=on, op=how, hint=hint)
	ast = SelectStmt(select_list, table_ref)
	return BigDataFrame(self._ic, ast)


# SQL AST

class SQLNodeMixin(object):
    def to_sql(self):
	raise NotImplementedError

    def __str__(self):
	return self.to_sql()


# Expr hierarchy

class Expr(SQLNodeMixin):
    def __init__(self):
	raise NotImplementedError


class Literal(Expr):
    def __init__(self, expr):
	self._expr = expr

    def to_sql(self):
	return "%s" % str(self._expr)


class BinaryExpr(Expr):
    _operators = ['=', '==', '!=', '>', '>=', '<', '<=', 'and', 'or']
    def __init__(self, op, expr1, expr2):
	if op not in BinaryExpr._operators:
	    raise ValueError("op %s not one of %s" % (op, str(BinaryExpr._operators)))
	self._op = op
	if not isinstance(expr1, Expr):
	    raise ValueError("expr1 %s is not of type Expr" % str(expr1))
	self._expr1 = expr1
	if not isinstance(expr2, Expr):
	    raise ValueError("expr2 %s is not of type Expr" % str(expr2))
	self._expr2 = expr2

    def to_sql(self):
	return "(%s) %s (%s)" % (self._expr1.to_sql(), self._op, self._expr2.to_sql())


# TableRef hierarchy

class TableRef(SQLNodeMixin):
    def __init__(self, alias):
	self._alias = alias # string

    @property
    def name(self):
	return self._alias

    def to_sql(self):
	return self._alias


class BaseTableRef(TableRef):
    def __init__(self, name, alias=None):
	super(BaseTableRef, self).__init__(alias)
	self._name = name # TableName

    @property
    def name(self):
	if self._alias:
	    return self._alias
	else:
	    return self._name.to_sql()

    def to_sql(self):
	if self._alias:
	    return "%s AS %s" (self._name.to_sql(), self._alias)
	else:
	    return self._name.to_sql()


class InlineView(TableRef):
    def __init__(self, query, alias):
	super(InlineView, self).__init__(alias)
	self._query = query

    @property
    def name(self):
	return self._alias

    def to_sql(self):
	return "(%s) AS %s" % (self._query, self._alias)


class JoinTableRef(TableRef):
    def __init__(self, left, right, on, op='inner', hint=None, alias=None):
	super(JoinTableRef, self).__init__(alias)
	self._left = left # TableRef
	self._right = right # TableRef
	self._op = op # string, inner, left outer, cross, etc.
	self._hint = hint # string, shuffle or broadcast
	# on is None, string, Expr, list[string]
	if on is None:
	    # for CROSS join
	    self._on = None
	elif isinstance(on, BinaryExpr):
	    self._on = on
	elif isinstance(on, Literal):
	    self._on = BinaryExpr('=', on, on)
	elif isinstance(on, basestring):
	    le = Literal('%s.%s' % (left.name, on))
	    re = Literal('%s.%s' % (right.name, on))
	    self._on = BinaryExpr('=', le, re)
	elif isinstance(on, (list, tuple)):
	    if not all([isinstance(x, basestring) for x in on]):
		raise ValueError("if on is a list/tuple, must only contain strings")
	    exprs = []
	    for s in on:
		le = Literal('%s.%s' % (left.name, s))
		re = Literal('%s.%s' % (right.name, s))
		exprs.append(BinaryExpr('=', le, re))
	    # reduce by conjunction
	    self._on = exprs[0]
	    for expr in exprs:
		self._on = BinaryExpr('and', self._on, expr)
	else:
	    raise ValueError("I don't know what to do with your on argument")

    def to_sql(self):
	hint = '' if not self._hint else '[%s]' % self._hint
	sql = '%s %s JOIN %s %s' % (self._left.to_sql(), self._op,
		hint, self._right.to_sql())
	if self._on is not None:
	    sql += ' ON %s' % self._on.to_sql()
	return sql


# other SQL elements

class OrderByElement(SQLNodeMixin):
    def __init__(self, expr, is_asc=None, nulls_first=None):
	self._expr = expr # Expr
	self._is_asc = is_asc # Bool
	self._nulls_first = nulls_first # Bool

    def to_sql(self):
	sql = self._expr.to_sql()
	if self._is_asc is not None:
	    sql += ' ASC' if self._is_asc else ' DESC'
	if self._nulls_first is not None:
	    if self._is_asc and self._nulls_first:
		sql += ' NULLS FIRST'
	    elif (not self._is_asc) and (not self._nulls_first):
		sql += ' NULLS LAST'
	return sql


class LimitElement(SQLNodeMixin):
    def __init__(self, limit_expr=None, offset_expr=None):
	self._limit_expr = limit_expr # Expr
	self._offset_expr = offset_expr # Expr

    def to_sql(self):
	sql = ''
	if self._limit_expr:
	    sql += ' LIMIT ' + self._limit_expr.to_sql()
	if self._offset_expr and self._offset_expr.to_sql() != '0':
	    sql += ' OFFSET ' + self._offset_expr.to_sql()
	return sql


class TableName(SQLNodeMixin):
    def __init__(self, table_name, db_name=None):
	self._table_name = table_name
	self._db_name = db_name

    def to_sql(self):
	sql = ''
	if self._db_name:
	    sql += self._db_name + '.'
	sql += self._table_name
	return sql


class SelectItem(SQLNodeMixin):
    def __init__(self, alias=None, expr=None, table_name=None):
	# TODO: check preconditions
	self._alias = alias # string
	self._expr = expr # Expr
	self._table_name = table_name # TableName
	self._is_star = True if self._expr is None else False

    @property
    def name(self):
	if not self._is_star:
	    if self._alias:
		return self._alias
	    else:
		return self._expr.to_sql()
	elif self._table_name:
	    return self._table_name.to_sql() + '.*'
	else:
	    return '*'

    def to_sql(self):
	if not self._is_star:
	    if self._alias:
		return '%s AS %s' % (self._expr.to_sql(), self._alias)
	    else:
		return self._expr.to_sql()
	elif self._table_name:
	    return self._table_name.to_sql() + '.*'
	else:
	    return '*'


# SQL object

class SelectStmt(SQLNodeMixin):
    def __init__(self, select_list, from_, where=None, order_by=None,
		 group_by=None, having=None, limit=None):
	self._select_list = tuple(select_list) # Iter[SelectItem]
	self._from = from_ # TableRef
	self._where = where # Expr
	self._order_by = order_by # Tuple[OrderByElement]
	self._group_by = group_by # Tuple[Expr]
	self._having = having # Expr
	self._limit = limit # LimitElement

	# do I need these?
	# self._has_groupby = False
	# self._has_agg = False

    def to_sql(self):
	sql = 'SELECT ' + ', '.join([s.to_sql() for s in self._select_list])
	sql += ' FROM ' + self._from.to_sql()
	if self._where:
	    sql += ' WHERE ' + self._where.to_sql()
	if self._group_by:
	    sql += ' GROUP BY ' + ', '.join([g.to_sql() for g in self._group_by])
	if self._having:
	    sql += ' HAVING ' + self._having.to_sql()
	if self._order_by:
	    sql += ' ORDER BY ' + ', '.join([o.to_sql() for o in self._order_by])
	if self._limit:
	    sql += self._limit.to_sql()
	return sql
