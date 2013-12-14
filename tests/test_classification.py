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
import sklearn

import impala.dbapi

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

for i in xrange(rows):
    if i % 100 == 0:
        sys.stdout.write("%i\n" % i)
        sys.stdout.flush()
    cursor.execute("INSERT INTO test_logr")
    
        
    
    

cursor.execute("select pos from cosmic")
df = impala.to_dataframe(cursor)