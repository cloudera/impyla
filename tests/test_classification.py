# Copyright 2013 Cloudera Inc.
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

import sys

import numpy as np
import sklearn.linear_model

import impala.dbapi
import impala.sklearn

rows = 10000
cols = 100

class0 = np.random.multivariate_normal(np.random.normal(0, 1, cols),
                                       np.diag(np.exp(np.random.normal(0, 1, cols))),
                                       rows / 2)
class1 = np.random.multivariate_normal(np.random.normal(0, 1, cols),
                                       np.diag(np.exp(np.random.normal(0, 1, cols))),
                                       rows - rows / 2)

data = np.vstack((np.hstack((class0, np.zeros((rows / 2, 1)))),
                  np.hstack((class1, np.ones((rows - rows / 2, 1))))))
data = data[np.random.permutation(rows)]

# in memory
inmemory_estimator = sklearn.linear_model.LogisticRegression(fit_intercept=False)
inmemory_estimator.fit(data[:, :cols], data[:, cols])

# impala
conn = impala.dbapi.connect(host='ulaz-1.ent.cloudera.com', port=21050)
cursor = conn.cursor(user='root')

cursor.execute("CREATE DATABASE IF NOT EXISTS test_class")
cursor.execute("USE test_class")
cursor.execute("CREATE TABLE test_logr (%s, label BOOLEAN)" % ', '.join(['feat%i DOUBLE' % i for i in xrange(cols)]))
data_strings = []
for i in xrange(rows):
    row_string = '(' + ', '.join([str(val) for val in data[i, :-1]]) + ', %s' % ('true' if data[i, -1] > 0 else 'false') + ')'
    data_strings.append(row_string)
    if (i + 1) % 200 == 0:
        sys.stdout.write("%i\n" % (i+1))
        sys.stdout.flush()
        data_query = 'INSERT INTO test_logr VALUES %s' % ', '.join(data_strings)
        cursor.execute(data_query)
        data_strings = []

impala_estimator = impala.sklearn.ImpalaLogisticRegression()
impala_estimator.fit(cursor, "SELECT * FROM test_logr", "label")



import impala.sklearn
import impala.blob
import impala.rpc
import impala.dbapi

reload(impala.sklearn)
reload(impala.dbapi)
reload(impala.blob)
reload(impala.rpc)
conn = impala.dbapi.connect(host='ulaz-1.ent.cloudera.com', port=21050)
cursor = conn.cursor(user='root')
cursor.execute("USE test_class")




model_store = impala.blob.BlobStore(cursor)
model_store = impala.blob.BlobStore(cursor, 'blob20131215144247onmerczp')

data_query = "SELECT * FROM test_logr"
label_column = 'label'


model_value = """
                %(udf_name)s(%(model)s, %(observation)s, %(label_column)s, %(step_size)f, %(mu)f)
                """ % {'udf_name': 'logr',
                       'model': '%s.value' % model_store.name,
                       'observation': 'toarray(%s)' % ', '.join(['%s.%s' % (data_view, col) for col in data_columns]),
                       'label_column': label_column,
                       'step_size': step_size,
                       'mu': mu}




database_name = '.*'
database_name = 'test_class'
table_name = '.*'
table_name = 'blob20131214211350ixuvnmkz'
req = TGetColumnsReq(sessionHandle=session_handle,
                     schemaName=database_name,
                     tableName=table_name,
                     columnName='.*')
resp = service.GetColumns(req)
impala.rpc.err_if_rpc_not_ok(resp)
operation_handle = resp.operationHandle
results = impala.rpc.fetch_results(service=service, operation_handle=operation_handle)


