## Logistic regression with Impala

An example of performing logistic regression on Impala using the scikit-learn
API and the madlibport UDAs.

### 1 Install MADlib-style analytics functions

First, you must install the UDF/UDAs supplied in the [madlibport][madlibport]
repo.  These supply the actual implementations for logistic regression, etc.

### 2 Create some fake data for classification

We'll create some easily separable 2-dimensional data.

```python
import numpy as np
import sklearn.preprocessing
rows = 10000
cols = 2
class0 = np.random.multivariate_normal([2, 2], np.diag([1, 1]), rows / 2)
class1 = np.random.multivariate_normal([-2, -2], np.diag([1, 1]), rows - rows / 2)
data = np.vstack((np.hstack((class0, np.zeros((rows / 2, 1)))),
                  np.hstack((class1, np.ones((rows - rows / 2, 1))))))
data = data[np.random.permutation(rows)]
scaled_obs = sklearn.preprocessing.StandardScaler().fit_transform(data[:, :2])
data = np.hstack((scaled_obs, data[:, 2].reshape(rows, 1)))
```

We can perform an in-memory logistic regression with scikit-learn:

```python
import sklearn.linear_model
inmemory_estimator = sklearn.linear_model.LogisticRegression(fit_intercept=False)
inmemory_estimator.fit(data[:, :cols], data[:, cols])
```

### 3 Push the data into Impala

The method below is not efficient, but normally you data will already be in
Hadoop.

```python
import impala.dbapi
conn = impala.dbapi.connect(host='my.host', port=21050)
cursor = conn.cursor()
cursor.execute("USE logr_example")
# create the table to hold the data
cursor.execute("CREATE TABLE test_logr (%s, label BOOLEAN)" % ', '.join(['feat%i DOUBLE' % i for i in xrange(cols)]))
# push the data to Impala with INSERT statements in batches of 1000 rows
data_strings = []
for i in xrange(rows):
    row_string = '(' + ', '.join([str(val) for val in data[i, :-1]]) + ', %s' % ('true' if data[i, -1] > 0 else 'false') + ')'
    data_strings.append(row_string)
    if (i + 1) % 1000 == 0:
        data_query = 'INSERT INTO test_logr VALUES %s' % ', '.join(data_strings)
        cursor.execute(data_query)
        data_strings = []
```

### 4 Train logistic regression model in Impala using distributed implementation

```python
import impala.sklearn
training_data = "SELECT * FROM test_logr"
label_column = "label"
impala_logr = impala.sklearn.LogisticRegression()
impala_logr.fit(cursor, training_data, label_column)
```

### 5 Plot and compare the results of the distributed and in-memory models

```python
import matplotlib.pyplot as plt

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
ax.plot(x, y, 'g-', lw=3, label='in-memory sklearn')
(x, y) = get_points(impala_logr.coef_)
ax.plot(x, y, 'y-', lw=3, label='impala sklearn')
ax.legend()
fig.show()
```

The results of the two computations are very close:

![Plot of data and separation planes][plot]


[madlibport]: https://github.com/cloudera/madlibport
[plot]: logr_plot.png
