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

import struct

from sklearn.base import BaseEstimator

import impala.util

class ImpalaLogisticRegression(BaseEstimator):
    
    def __init__(self, step_size=0.1, mu=0.1, n_iter=5):
        self.step_size = step_size
        self.mu = mu
        self.n_iter = n_iter
        self.coef_ = None
    
    def partial_fit(self, cursor, model_store, data_query, label_column, epoch):
        """Fit logistic regression model.
        
        Parameters
        ----------
        
        model_store is BlobStore that contains model data.  The key
        `str(epoch - 1)` must exist.
        
        data_query is a SQL query string that produces rows that go into the
        regression.  It will be converted into a VIEW, just for this fn call.
        All columns go into the regression except for the `label_column`.
        
        label_column is the string name of the column that contains the labels.
        """
        # A preferable alternative is to create a more repeatable pattern.  To
        # do so, the UDAs should all take the same args:
        # 1. a bit-string for the previous model,
        # 2. a bit-string for the model hyper-parameters,
        # 3. a bit-string representing the observation,
        # 4. the label.
        #
        # Something like this:
        # model_value = """
        #         %(udf_name)s(%(model)s, %(param)s, %(observation)s, %(label)s)
        #         """ % ('logr',
        #                '%s.value' % model_store.name,
        #                'param_table.value',
        #                'toarray(data_table.*)')
        #
        # Here is the logistic regression query as currently impl. in the
        # madlibport repo:
        #
        # INSERT INTO model_table
        # SELECT 5, encodearray(logr(decodearray(model_table.model), toarray(data_table.feat1, data_table.feat2), label, step, mu))
        # FROM model_table, data_table
        # WHERE (data_table.label is null || true)=(model_table.model is null || true) AND model_table.iter=4;
        
        prev_epoch = epoch - 1
        data_view = impala.util.create_view_from_query(cursor, data_query, safe=True)
        data_schema = impala.util.compute_result_schema(cursor, "SELECT * FROM %s" % data_view)
        columns = [tup[0] for tup in data_schema]
        if label_column not in columns:
            raise ValueError("%s is not a column in the provided data_query" % label_column)
        data_columns = [c for c in columns if c != label_column]
        model_value = """
                %(udf_name)s(%(model)s, %(observation)s, %(label_column)s, %(step_size)f, %(mu)f)
                """ % {'udf_name': 'logr',
                       'model': '%s.value' % model_store.name,
                       'observation': 'toarray(%s)' % ', '.join(['%s.%s' % (data_view, col) for col in data_columns]),
                       'label_column': label_column,
                       'step_size': self.step_size,
                       'mu': self.mu}
        derived_from_clause = model_store.distribute_value_to_table(str(prev_epoch), data_view)
        model_store.put(str(epoch), model_value, derived_from_clause)   # actual execution here
        impala.util.drop_view(cursor, data_view)
        self.coef_ = self._decode_coef(model_store[str(epoch)])
    
    def fit(self, cursor, data_query, label_column):
        import pdb
        pdb.set_trace()
        model_store = impala.blob.BlobStore(cursor)
        model_store.send_null('0')
        for i in xrange(self.n_iter):
            epoch = i + 1
            self.partial_fit(cursor, model_store, data_query, label_column, epoch)
            
    
    def _decode_coef(self, coef_string):
        num_values = len(coef_string) / struct.calcsize("d")
        values = struct.unpack("%id" % num_values, coef_string)
        return list(values)
