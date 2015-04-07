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
import pkgutil

import pytest
import pandas as pd

from impala.context import ImpalaContext
from impala.bdf import from_pandas


def test_context_cleanup(host, port, protocol, use_kerberos, ic, hdfs_client):
    # create a *new* ImpalaContext
    ctx = ImpalaContext(temp_dir=None, temp_db=None, nn_host=ic._nn_host,
                        webhdfs_port=ic._webhdfs_port, hdfs_user=ic._hdfs_user,
                        host=host, port=port, protocol=protocol,
                        use_kerberos=use_kerberos)

    # check that the database was created
    ctx._cursor.execute('SHOW DATABASES')
    databases = [tup[0].lower() for tup in ctx._cursor]
    assert ctx._temp_db.lower() in databases

    # check that a bdf table created with the ic is represented in the database
    df = pd.DataFrame({'a': (1, 2, 5), 'b': ('foo', 'bar', 'pasta')})
    bdf = from_pandas(ctx, df, method='in_query')
    # hack to get the table name: I know that this table was generated
    # ultimately with a `from_sql_table`, so I just reach into the AST to
    # figure it out.
    table_name = bdf._query_ast._from.name.split('.')[-1]
    ctx._cursor.execute('USE %s' % ctx._temp_db)
    ctx._cursor.execute('SHOW TABLES')
    tables = [tup[0].lower() for tup in ctx._cursor]
    assert table_name.lower() in tables

    # check that the temporary directory was created
    # (raises FileNotFound on failure)
    assert hdfs_client.status(ctx._temp_dir)

    # check that the corresponding data file has the correct size
    table_path = os.path.join(ctx._temp_dir, table_name)
    sizes = [s['length'] for (_, s) in hdfs_client.list(table_path)
             if s['type'] == 'FILE']
    assert len(sizes) == 1
    assert sizes[0] == 20

    ctx.close()

    # check that the temp database was dropped
    ctx._cursor.execute('SHOW DATABASES')
    databases = [tup[0].lower() for tup in ctx._cursor]
    assert ctx._temp_db.lower() not in databases

    # check that the temp dir was deleted
    # I know this is importable because this test depends on hdfs_client, which
    # skips if hdfs is not available
    from hdfs.util import HdfsError
    with pytest.raises(HdfsError):
        assert hdfs_client.status(ctx._temp_dir)
