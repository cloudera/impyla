Rapid, batch model-scoring with Impyla
======================================

BigML's machine-learning-as-a-service allows you to export a usable model as a
Python function.  If you have lots of data to score, you're probably going to do
it on Hadoop.  Here we will compare the performance of doing this using a
compiled Python UDF in Impala versus processing the data with PySpark, which is
ostensibly at least as fast as Hadoop Streaming.


## Problem and data

We will be using a model trained by our friends at BigML on Fisher's classical
Iris data set.  It is a classification problem that has 3 classes, using 4
numerical features.  The raw data can be found in `raw_data/`.

This data is quite puny from Hadoop's perspective, so we will simply replicate
it 1 million times using PySpark:

```python
with open('raw_data/iris.data', 'r') as ip:
    raw = filter(lambda x: x != '', [line.strip() for line in ip])

single = sc.parallelize(raw, 5).map(lambda line: '\t'.join(line.split(',')[:-1]))
replicated = single.flatMap(lambda x: [x]*1000000)
replicated.saveAsTextFile('bigml/iris_text')
```

To improve the performance more, we will rewrite the data in Parquet format
using Impala:

```sql
CREATE EXTERNAL TABLE iris_text (
    sepal_length DOUBLE,
    sepal_width DOUBLE,
    petal_length DOUBLE,
    petal_width DOUBLE
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE
LOCATION '/user/laserson/bigml/iris_text';

CREATE TABLE iris_parquet LIKE iris_text STORED AS PARQUET;

INSERT INTO iris_parquet SELECT * FROM iris_text;
```

Finally, the classifier function itself was provided by BigML:

```python
def predict_species(sepal_width=None, petal_length=None, petal_width=None):
    """ Predictor for species from model/52952081035d07727e01d836
        Predictive model by BigML - Machine Learning Made Easy
    """
    # 0 == Iris-virginica
    # 1 == Iris-versicolor
    # 2 == Iris-setosa
#    if (petal_width is None):
#        return 0
    if (petal_width > 0.8):
        if (petal_width <= 1.75):
#            if (petal_length is None):
#                return 1
            if (petal_length > 4.95):
                if (petal_width <= 1.55):
                    return 0
                if (petal_width > 1.55):
                    if (petal_length > 5.45):
                        return 0
                    if (petal_length <= 5.45):
                        return 1
            if (petal_length <= 4.95):
                if (petal_width <= 1.65):
                    return 1
                if (petal_width > 1.65):
                    return 0
        if (petal_width > 1.75):
#            if (petal_length is None):
#                return 0
            if (petal_length > 4.85):
                return 0
            if (petal_length <= 4.85):
#                if (sepal_width is None):
#                    return 0
                if (sepal_width <= 3.1):
                    return 0
                if (sepal_width > 3.1):
                    return 1
    if (petal_width <= 0.8):
        return 2
```

## Spark solution

Spark lets you easily write distributed computations using Python.

```python
observations = sc.textFile('/user/laserson/bigml/iris_text') \
        .map(lambda line: tuple([float(val) for val in line.split('\t')[1:]]))
predictions = observations.map(lambda tup: predict_species(*tup))
predictions.distinct().collect()
```

## Impala solution

The solution is similar, but the Python function has to be compiled.

```python
from impala.dbapi import connect
from impala.udf import ship_udf
from numba.ext.impala import udf, FunctionContext, DoubleVal, IntVal

def predict_species(context, sepal_width, petal_length, petal_width):
    """ Predictor for species from model/52952081035d07727e01d836
        Predictive model by BigML - Machine Learning Made Easy
    """
    # 0 == Iris-virginica
    # 1 == Iris-versicolor
    # 2 == Iris-setosa
    if sepal_width.is_null or petal_length.is_null or petal_width.is_null:
        return IntVal.null
    sepal_width = sepal_width.val
    petal_length = petal_length.val
    petal_width = petal_width.val
#    if (petal_width is None):
#        return IntVal(0)
    if (petal_width > 0.8):
        if (petal_width <= 1.75):
#            if (petal_length is None):
#                return IntVal(1)
            if (petal_length > 4.95):
                if (petal_width <= 1.55):
                    return IntVal(0)
                if (petal_width > 1.55):
                    if (petal_length > 5.45):
                        return IntVal(0)
                    if (petal_length <= 5.45):
                        return IntVal(1)
            if (petal_length <= 4.95):
                if (petal_width <= 1.65):
                    return IntVal(1)
                if (petal_width > 1.65):
                    return IntVal(0)
        if (petal_width > 1.75):
#            if (petal_length is None):
#                return IntVal(0)
            if (petal_length > 4.85):
                return IntVal(0)
            if (petal_length <= 4.85):
#                if (sepal_width is None):
#                    return IntVal(0)
                if (sepal_width <= 3.1):
                    return IntVal(0)
                if (sepal_width > 3.1):
                    return IntVal(1)
    if (petal_width <= 0.8):
        return IntVal(2)

# connect to impala
host = 'bottou01-10g.pa.cloudera.com'
user = 'laserson'
conn = connect(host=host, port=21050)
cursor = conn.cursor(user='laserson')
cursor.execute('USE laserson')

# compile and ship
predict_species = udf(IntVal(FunctionContext, DoubleVal, DoubleVal, DoubleVal))(predict_species)
ship_udf(cursor, predict_species, '/user/laserson/bigml/udfs/bigml.ll', host, user=user)
```

Then run the computation:

```python
sepal_width, petal_length, petal_width):
cursor.execute("SELECT DISTINCT predict_species(sepal_width, petal_length, petal_width) FROM iris_text")
```