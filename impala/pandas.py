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

def _schema_hack(cursor, sql_query):
    # get the schema of the query result via a LIMIT 0 hack
    cursor.execute('SELECT * FROM (%s) AS t LIMIT 0' % sql_query)
    schema = [tup[:2] for tup in cursor.description]
    cursor._reset_state()
    return schema

def read_sql_query(cursor, sql_query):
    """Create BigDataFrame from SQL query"""
    return SQLBigDataFrame(cursor, sql_query)

def read_sql_table(cursor, table):
    """Create BigDataFrame from SQL query"""
    return TableBigDataFrame(cursor, table)

def merge(first, second):
    return BigDataFrame()

def concat(objs):
    """Concatenate a list of BDFs"""
    return UnionStmt(objs)


class BigDataFrame(object):
    """Base class for Impala-backed data frame"""

    def __init__(self):
	self._column_names = ()
	self._column_types = ()

    def _compile(self):
	pass

    def store():
	pass

    def ix():
	pass

    def _projection():
	pass


class SQLBigDataFrame(BigDataFrame):
    """BDF initialized with a SQL query"""

    def __init__(self, cursor, sql_query):
	super(SQLBigDataFrame, self).__init__()
	self._sql_query = sql_query
	for tup in _schema_hack(cursor, sql_query):
	    self._column_names += (tup[0],)
	    self._column_types += (tup[1],)

    def _compile(self):
	return self._sql_query


class TableBigDataFrame(SelectStmt):
    def __init__(self, cursor, table):
	super(TableBigDataFrame, self).__init__()
	for tup in _schema_hack(cursor, 'SELECT * FROM %s' % table):
	    self._column_names += (tup[0],)
	    self._column_types += (tup[1],)
	    self._select += (SelectItem(tup[0], tup[0]),)
	self._from += (TableRef(table),)


class SelectStmt(BigDataFrame):
    def __init__(self):
	super(SelectStmt, self).__init__()
	self._select = () # Tuple[SelectItem]
	self._where = () # Tuple[Expr]
	self._groupby = () # Tuple[Expr]
	self._having = () # Tuple[Expr]
	self._from = () # Tuple[TableRef]
	self._orderby = () # Tuple[Expr]
	self._has_groupby = False
	self._has_agg = False

    def _compile(self):
	"""Compile BDF into a SQL string for exec on Impala"""
	pass


class UnionStmt(BigDataFrame):
    def __init__(self, bdfs):
	if len(bdfs) < 2:
	    raise ValueError("Must supply at least two BigDataFrames for concatenation")
	if not all([isinstance(bdf, BigDataFrame) for bdf in bdfs]):
	    raise ValueError("All supplied objects must be BigDataFrames")
	if not all([bdfs[0]._column_types == bdf._column_types for bdf in bdfs[1:]]):
	    raise ValueError("All BDFs must share the same schema")
	super(UnionStmt, self).__init__()
	self._union = () # Tuple[BDF]
	for bdf in bdfs:
	    self._union += (bdf,)


class SelectItem(object):
    def __init__(self, alias=None, expr=None):
	self._alias = alias
	self._expr = expr


class TableRef(object):
    def __init__(self, alias=None, bdf=None):
	self._alias = alias
	self._bdf = bdf





class ImpalaContext(object):
    """Helper object for managing connections to Impala etc"""

    def __init__(self):
	pass


class Expr(object):

    def __init__(self):
	pass

    def __str__(self):
	"""Emit the SQL string version of the expression"""


# See impala codebase for subclasses

class ArithmeticExpr

class BinaryPredicate