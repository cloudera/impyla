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
from cStringIO import StringIO

import pandas as pd

from impala.bdf import BigDataFrame
from impala.util import _random_id, _get_schema_hack, _py_to_sql_string
from impala.dbapi import connect
from impala._sql_model import (_to_TableName, BaseTableRef, SelectItem,
        SelectStmt, Literal, InlineView, _create_table)

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


class ImpalaContext(object):

    def __init__(self, temp_dir=None, temp_db=None, nn_host=None,
            webhdfs_port=50070, hdfs_user=None, *args, **kwargs):
        # args and kwargs get passed directly into impala.dbapi.connect()
        suffix = _random_id(length=8)
        self._temp_dir = '/tmp/bdf-%s' % suffix if temp_dir is None else temp_dir
        self._temp_db = 'tmp_bdf_%s' % suffix if temp_db is None else temp_db
        self._conn = connect(*args, **kwargs)
        self._cursor = self._conn.cursor()
        # used for pywebhdfs cleanup of temp dir; not required
        self._nn_host = nn_host
        self._webhdfs_port = webhdfs_port
        self._hdfs_user = hdfs_user
        if temp_db is None:
            self._cursor.execute("CREATE DATABASE %s LOCATION '%s'" %
                    (self._temp_db, self._temp_dir))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        # drop the temp database
        self._cursor.execute('USE %s' % self._temp_db)
        self._cursor.execute('SHOW TABLES')
        temp_tables = [x[0] for x in self._cursor.fetchall()]
        for table in temp_tables:
            self._cursor.execute('DROP TABLE IF EXISTS %s.%s' % (self._temp_db, table))
        self._cursor.execute('USE default')
        self._cursor.execute('DROP DATABASE IF EXISTS %s' % self._temp_db)
        # drop the temp dir in HDFS
        try:
            from requests.exceptions import ConnectionError
            from pywebhdfs.webhdfs import PyWebHdfsClient
            hdfs_client = PyWebHdfsClient(host=self._nn_host,
                port=self._webhdfs_port, user_name=self._hdfs_user)
            hdfs_client.delete_file_dir(self._temp_dir.lstrip('/'), recursive=True)
        except ImportError:
            import sys
            sys.stderr.write("Could not import requests or pywebhdfs. "
                "You must delete the temporary directory manually: %s" % self._temp_dir)
        except ConnectionError:
            import sys
            sys.stderr.write("Could not connect via pywebhdfs. "
                "You must delete the temporary directory manually: %s" % self._temp_dir)

    def from_sql_query(self, query, alias=None):
        """Create a BDF from a SQL query executed by Impala"""
        query_alias = alias if alias else _random_id('inline_', 4)
        table_ref = InlineView(query, query_alias)
        schema = _get_schema_hack(self._cursor, table_ref)
        select_list = tuple([SelectItem(expr=Literal(col)) for (col, ty) in schema])
        return BigDataFrame(self, SelectStmt(select_list, table_ref))

    def from_sql_table(self, table):
        """Create a BDF from a table name usable in Impala"""
        table_name = _to_TableName(table)
        table_ref = BaseTableRef(table_name)
        schema = _get_schema_hack(self._cursor, table_ref)
        select_list = tuple([SelectItem(expr=Literal(col)) for (col, ty) in schema])
        return BigDataFrame(self, SelectStmt(select_list, table_ref))

    def from_hdfs(self, path, schema, table=None, overwrite=False,
            file_format='TEXTFILE', partition_schema=None,
            field_terminator='\\t', line_terminator='\\n'):
        """Create a BDF backed by an external file in HDFS.

        File must be Impala-compatible
        """
        if partition_schema is not None:
            raise NotImplementedError("Partitions not yet implemented in .from_hdfs()")
        if table is None:
            temp_table = _random_id('tmp_table_', 8)
            table = "%s.%s" % (self._temp_db, temp_table)
        table_name = _to_TableName(table)
        if overwrite:
            self._cursor.execute("DROP TABLE IF EXISTS %s" % table_name.to_sql())
        create_stmt = _create_table(table_name, schema, path=path,
                file_format=file_format, field_terminator=field_terminator,
                line_terminator=line_terminator)
        self._cursor.execute(create_stmt)
        return self.from_sql_table(table_name.to_sql())

    def from_pandas(self, df, table=None, path=None, method='in_query',
            file_format='TEXTFILE', field_terminator='\t', line_terminator='\n',
            hdfs_host=None, webhdfs_port=50070, hdfs_user=None, overwrite=False):
        """Create a BDF by shipping an in-memory pandas `DataFrame` into Impala
        
        path is the dir, not the filename
        """
        # TODO: this is not atomic
        temp_table = _random_id('tmp_table_', 8)
        if table is None:
            table = "%s.%s" % (self._temp_db, temp_table)
        if path is None:
            path = os.path.join(self._temp_dir, temp_table)
        table_name = _to_TableName(table)
        if overwrite:
            self._cursor.execute("DROP TABLE IF EXISTS %s" % table_name.to_sql())
        columns = list(df.columns)
        types = [_numpy_dtype_to_impala_PrimitiveType(ty) for ty in df.dtypes]
        schema = zip(columns, types)
        create_stmt = _create_table(table_name, schema, path=path,
                file_format=file_format, field_terminator=field_terminator,
                line_terminator=line_terminator)
        self._cursor.execute(create_stmt)
        if method == 'in_query':
            query = "INSERT INTO %s VALUES " % table_name.to_sql()
            query += ', '.join(['(%s)' % ', '.join(map(_py_to_sql_string, row)) for row in df.values])
            self._cursor.execute(query)
        elif method == 'webhdfs':
            if file_format != 'TEXTFILE':
                raise ValueError("only TEXTFILE format supported for webhdfs")
            if path is None:
                raise ValueError("must supply a path for EXTERNAL table for webhdfs")
            from pywebhdfs.webhdfs import PyWebHdfsClient
            hdfs_client = PyWebHdfsClient(host=hdfs_host, port=webhdfs_port,
                    user_name=hdfs_user)
            raw_data = StringIO()
            df.to_csv(raw_data, sep=field_terminator,
                    line_terminator=line_terminator, header=False, index=False)
            hdfs_client.create_file(os.path.join(path, 'data.txt').lstrip('/'), raw_data.getvalue(), overwrite=overwrite)
            raw_data.close()
        else:
            raise ValueError("method must be 'in_query' or 'webhdfs'; got %s" % method)
        return self.from_sql_table(table_name.to_sql())
