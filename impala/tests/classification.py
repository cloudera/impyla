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

from __future__ import absolute_import

import sys
from six.moves import range

import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model
import sklearn.preprocessing

import impala.dbapi
import impala.sklearn


rows = 10000
cols = 2

# class0 = np.random.multivariate_normal(np.random.normal(0, 1, cols),
#                                        np.diag(np.exp(np.random.normal(0, 1, cols))),
#                                        rows / 2)
# class1 = np.random.multivariate_normal(np.random.normal(0, 1, cols),
#                                        np.diag(np.exp(np.random.normal(0, 1, cols))),
#                                        rows - rows / 2)

class0 = np.random.multivariate_normal([2, 2],
                                       np.diag([1, 1]),
                                       rows / 2)
class1 = np.random.multivariate_normal([-2, -2],
                                       np.diag([1, 1]),
                                       rows - rows / 2)

data = np.vstack((np.hstack((class0, np.zeros((rows / 2, 1)))),
                  np.hstack((class1, np.ones((rows - rows / 2, 1))))))
data = data[np.random.permutation(rows)]
scaled_obs = sklearn.preprocessing.StandardScaler().fit_transform(data[:, :2])
data = np.hstack((scaled_obs, data[:, 2].reshape(rows, 1)))

# in memory
inmemory_estimator = sklearn.linear_model.LogisticRegression(
    fit_intercept=False)
inmemory_estimator.fit(data[:, :cols], data[:, cols])

# impala
conn = impala.dbapi.connect(host='ulaz-1.ent.cloudera.com', port=21050)
cursor = conn.cursor(user='root')

cursor.execute("CREATE DATABASE IF NOT EXISTS test_class")
cursor.execute("USE test_class")
cursor.execute("CREATE TABLE test_logr (%s, label BOOLEAN)" %
               ', '.join(['feat%i DOUBLE' % i for i in range(cols)]))
data_strings = []
for i in range(rows):
    row_string = '(' + ', '.join([str(val) for val in data[i, :-1]]) + ', %s' % ('true' if data[i, -1] > 0 else 'false') + ')'
    data_strings.append(row_string)
    if (i + 1) % 1000 == 0:
        sys.stdout.write("%i\n" % (i + 1))
        sys.stdout.flush()
        data_query = 'INSERT INTO test_logr VALUES %s' % ', '.join(
            data_strings)
        cursor.execute(data_query)
        data_strings = []

impala_logr = impala.sklearn.LogisticRegression()
impala_logr.fit(cursor, "SELECT * FROM test_logr", "label")

impala_svm = impala.sklearn.SVM()
impala_svm.fit(cursor, "SELECT * FROM test_logr", "label")

# plot data


def get_orthogonal(x):
    x = np.asarray(x).ravel()
    x_norm = x / np.linalg.norm(x)
    y = np.random.normal(size=len(x))
    y_norm = y / np.linalg.norm(y)
    q = y_norm - np.dot(y_norm, x_norm) * x_norm
    q_norm = q / np.linalg.norm(q)
    return q_norm


def get_points(coef):
    orth = get_orthogonal(coef)
    orth_x = [-3 * orth[0], 3 * orth[0]]
    orth_y = [-3 * orth[1], 3 * orth[1]]
    return (orth_x, orth_y)


fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(data[:, 0], data[:, 1], s=30, c=data[:, 2])
(x, y) = get_points(inmemory_estimator.coef_)
ax.plot(x, y, 'k-')
(x, y) = get_points(impala_logr.coef_)
ax.plot(x, y, 'k:')
(x, y) = get_points(impala_svm.coef_)
ax.plot(x, y, 'k--')
fig.show()


# import impala.sklearn
# import impala.blob
# import impala.rpc
# import impala.dbapi

# reload(impala.sklearn)
# reload(impala.dbapi)
# reload(impala.blob)
# reload(impala.rpc)
# reload(impala.error)
# conn = impala.dbapi.connect(host='ulaz-1.ent.cloudera.com', port=21050)
# cursor = conn.cursor(user='root')
# cursor.execute("USE test_class")


# model_store = impala.blob.BlobStore(cursor)
# model_store = impala.blob.BlobStore(cursor, 'blob20131215144247onmerczp')

# data_query = "SELECT * FROM test_logr"
# label_column = 'label'


# model_value = """
#                 %(udf_name)s(%(model)s, %(observation)s, %(label_column)s, %(step_size)f, %(mu)f)
#                 """ % {'udf_name': 'logr',
#                        'model': '%s.value' % model_store.name,
#                        'observation': 'toarray(%s)' % ', '.join(['%s.%s' % (data_view, col) for col in data_columns]),
#                        'label_column': label_column,
#                        'step_size': step_size,
#                        'mu': mu}


# database_name = '.*'
# database_name = 'test_class'
# table_name = '.*'
# table_name = 'blob20131214211350ixuvnmkz'
# req = TGetColumnsReq(sessionHandle=session_handle,
#                      schemaName=database_name,
#                      tableName=table_name,
#                      columnName='.*')
# resp = service.GetColumns(req)
# impala.rpc.err_if_rpc_not_ok(resp)
# operation_handle = resp.operationHandle
# results = impala.rpc.fetch_results(service=service, operation_handle=operation_handle)


# def delete_all_tables(cursor):
#     cursor.execute("USE test_class")
#     cursor.execute("SHOW TABLES")
#     tables = cursor.fetchall()
#     for table in tables:
#         cursor.execute("DROP TABLE %s" % table[0])

# def delete_all_views(cursor):
#     cursor.execute("USE test_class")
#     cursor.execute("SHOW TABLES")
#     tables = cursor.fetchall()
#     for table in tables:
#         cursor.execute("DROP VIEW %s" % table[0])


# def norm(x):
#     return x / np.sqrt(np.dot(x, x))
