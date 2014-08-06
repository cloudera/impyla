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

import string
import random
from copy import copy

from .util import as_pandas

# some rando utilities

_null_slice = slice(None, None, None)

def _random_id(prefix='', length=8):
    return prefix + ''.join(random.sample(string.ascii_uppercase, length))

def _get_schema_hack(cursor, table_ref):
    # get the schema of the query result via a LIMIT 0 hack
    cursor.execute('SELECT * FROM %s LIMIT 0' % table_ref.to_sql())
    schema = [tup[:2] for tup in cursor.description]
    cursor.fetchall() # resets the state of the cursor and closes operation
    return schema


# PUBLIC API

def read_sql_query(cursor, query, alias=None):
    """Create a BDF from a SQL query executed by Impala"""
    query_alias = alias if alias else _random_id('inline_', 4)
    table_ref = InlineView(query, query_alias)
    schema = _get_schema_hack(cursor, table_ref)
    select_list = tuple([SelectItem(expr=Literal(col)) for (col, ty) in schema])
    return BigDataFrame(SelectStmt(select_list, table_ref))

def read_sql_table(cursor, table):
    """Create a BDF from a table name usable in Impala"""
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
	raise ValueError("your value for table is weird")
    table_name = TableName(name, db)
    table_ref = BaseTableRef(table_name)
    schema = _get_schema_hack(cursor, table_ref)
    select_list = tuple([SelectItem(expr=Literal(col)) for (col, ty) in schema])
    return BigDataFrame(SelectStmt(select_list, table_ref))

def read_hdfs(cursor, path, schema):
    """Create a BDF from an Impala-compatible file in HDFS

    Uses `CREATE EXTERNAL TABLE`. Should be CSV or Avro/Parquet
    """
    raise NotImplementedError

def from_pandas(cursor, df):
    """Create a BDF by shipping an in-memory pandas `DataFrame` into Impala

    TBD: could possible translate into a `VALUES()` statement instead of writing
    the data to HDFS first.
    """
    raise NotImplementedError


class BigDataFrame(object):

    def __init__(self, ast=None):
	self._query_ast = ast

    def fetch(self, cursor):
	"""Return the cursor object ready for iterating over rows"""
	cursor.execute(self._query_ast.to_sql())
	return cursor

    def store(self, cursor, name, path):
	"""Materialize the results and stores them in HFDS

	Implemented through a `CREATE TABLE AS SELECT`.
	"""
	raise NotImplementedError
	# TODO: finish this
	sql = 'CREATE TABLE %s AS %s STORED AS %s ...' % (name, self._query_ast.to_sql())
	cursor.execute(sql)
	return read_sql_table(cursor, name)

    def save_view(self, cursor, view_name, db_name=None):
	"""Create a named view representing this BDF for later reference"""
	table_name = TableName(view_name, db_name)
	sql = 'CREATE VIEW %s AS %s' % (table_name.to_sql(), self._query_ast.to_sql())
	cursor.execute(sql)
	return read_sql_table(cursor, table_name.to_sql())

    def take(self, cursor, n):
	"""Return `n` rows as a pandas `DataFrame`

	Distributed and no notion of order, so not guaranteed to be
	reproducible.
	"""
	bdf = BigDataFrame(self._query_ast.limit(Literal(n)))
	return as_pandas(bdf.fetch(cursor))

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
	    return self._getitem_tuple(obj)
	elif isinstance(obj, list):
	    return self._getitem_projection(obj)
	else:
	    # single object, possibly a slice; wrap in list and get projection
	    return self._getitem_projection([obj])

    def _getitem_tuple(self, obj):
	raise NotImplementedError

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
	    if not isinstance(obj.start, (int, long)) or
		    not isinstance(obj.stop, (int, long)):
		raise ValueError("slice stop and start must be int/long")
	    return (LimitElement(obj.stop - obj.start, obj.start), None)
	raise ValueError("row indexer must be int/long/slice/Expr")



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
	if op not in _operators:
	    raise ValueError("op %s not one of %s" % (op, str(_operators)))
	self._op = op
	if not isinstance(expr1, Expr):
	    raise ValueError("expr1 %s is not of type Expr" % str(expr1))
	self._expr1 = expr1
	if not isinstance(expr2, Expr):
	    raise ValueError("expr2 %s is not of type Expr" % str(expr2))
	self._expr2 = expr2

    def to_sql(self):
	return "%s %s %s" % (self._expr1.to_sql(), self._op, self._expr2.to_sql())



class TableRef(SQLNodeMixin):
    def __init__(self, alias):
	self._alias = alias

    def to_sql(self):
	return " %s " % self._alias


class BaseTableRef(TableRef):
    def __init__(self, name, alias=None):
	self._name = name # TableName
	self._alias = alias # string

    def to_sql(self):
	if self._alias:
	    return "%s AS %s" (self._name.to_sql(), self._alias)
	else:
	    return self._name.to_sql()


class InlineView(TableRef):
    def __init__(self, query, alias):
	super(InlineView, self).__init__(alias)
	self._query = query

    def to_sql(self):
	return "(%s) AS %s" % (self._query, self._alias)


class JoinTableRef(TableRef):
    def __init__(self):
	raise NotImplementedError




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
	self._is_star = True if not self._expr else False

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





class RelationalMixin(object):
    def projection(self):
	raise NotImplementedError

    def select(self):
	raise NotImplementedError

    def rename(self):
	raise NotImplementedError

    def join(self):
	raise NotImplementedError

    def limit(self, n, offset=None):
	raise NotImplementedError



class SelectStmt(SQLNodeMixin, RelationalMixin):
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

    def projection(self, select_list):
	table_ref = InlineView(self.to_sql(), _random_id())
	return SelectStmt(select_list, table_ref)

    def limit(self, n, offset=None):
	select_list = [SelectItem()] # SELECT *
	table_ref = InlineView(self.to_sql(), _random_id())
	return SelectStmt(select_list, table_ref, limit=LimitElement(n, offset))

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
