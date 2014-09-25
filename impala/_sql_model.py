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

# utilities

def _to_TableName(table):
    """Convert string table name ([foo.]bar) into a TableName object."""
    if not isinstance(table, basestring):
        raise ValueError("`table` must be a string")
    if table == '':
        raise ValueError("`table` must not be the empty string")
    fields = table.split('.')
    if len(fields) == 2:
        db = fields[0]
        name = fields[1]
    elif len(fields) == 1:
        db = None
        name = fields[0]
    else:
        raise ValueError("your value for `table` (%s) is weird" % table)
    return TableName(name, db)


# Mixin for SQL objects

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
        return "((%s) %s (%s))" % (self._expr1.to_sql(), self._op, self._expr2.to_sql())


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


# Query objects (DQL statements)

class QueryStmt(SQLNodeMixin):

    def to_sql(self):
        raise NotImplementedError

    def select_list(self):
        raise NotImplementedError

    # below are internally used helper functions
    # they only make use of the QueryStmt API above

    def _projection(self, obj):
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
                select_list.append(self.select_list[elt])
            elif isinstance(elt, slice):
                # slices are relative to the query_ast select_list
                # must be either integers or strings; if strings, must be
                # findable in the select list; slice finally converted to range
                if elt == slice(None, None, None):
                    # null slice; take all columns
                    select_list.extend(self.select_list)
                    continue
                col_strings = [s.name for s in self.select_list]
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
                    stop = len(self.select_list)
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
                    select_list.append(self.select_list[i])
        return select_list

    def _where(self, obj):
        # obj is one of int, expr, slice
        # to be converted to a pair of LimitElement and Expr
        # this fn does not currently make use of self, but his here for
        # organizational convenience
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


class SelectStmt(QueryStmt):
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

    def select_list(self):
        return self._select_list

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


class UnionStmt(QueryStmt):
    def __init__(self, queries):
        self._union_list = tuple(queries) # Tuple[QueryStmt]

    def select_list(self):
        # somewhere down the tree, there must be a SelectStmt
        return self._union_list[0].select_list()

    def to_sql(self):
        return ' UNION ALL '.join([u.to_sql() for u in self._union_list])


# DDL statement helpers (they are not currently modeled)

def _create_table(table_name, table_schema, path=None,
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
    else:
        raise ValueError("Invalid file format")
    if external:
        query += " LOCATION '%s'" % path
    return query

def _create_table_as_select(table_name, path=None, file_format='TEXTFILE',
        field_terminator='\\t', line_terminator='\\n'):
    external = path is not None
    if external:
        query = "CREATE EXTERNAL TABLE %s" % table_name.to_sql()
    else:
        query = "CREATE TABLE %s" % table_name.to_sql()
    if file_format == 'PARQUET':
        query += " STORED AS PARQUET"
    elif file_format == 'TEXTFILE':
        query += ((" ROW FORMAT DELIMITED FIELDS TERMINATED BY '%s' "
                   "LINES TERMINATED BY '%s' STORED AS TEXTFILE") %
                   (field_terminator, line_terminator))
    if external:
        query += " LOCATION '%s'" % path
    query += " AS "
    return query
