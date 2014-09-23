bench-impyla
============

Benchmarks for impyla

### 1 Convert BigML model to eliminate dictionaries

Convert the raw BigML model to something that can be compiled. This requires
eliminating the use of a dictionary to pass in the data points.

```bash
bin/process_bigml_model.py -i raw-models/model_100.py -o models/model_100.py -d raw-data/bigml_53168e4dd63708516d001938.csv
bin/process_bigml_model.py -i raw-models/model_1000.py -o models/model_1000.py -d raw-data/bigml_53168e4dd63708516d001938.csv
bin/process_bigml_model.py -i raw-models/model_1500.py -o models/model_1500.py -d raw-data/bigml_53168e4dd63708516d001938.csv
bin/process_bigml_model.py -i raw-models/model_2000.py -o models/model_2000.py -d raw-data/bigml_53168e4dd63708516d001938.csv
bin/process_bigml_model.py -i raw-models/model_500.py -o models/model_500.py -d raw-data/bigml_53168e4dd63708516d001938.csv
```
I also added a trivial `model_0.py` to analyze the overhead.


### 2 Generate models that eliminate use of strings

```bash
bin/destringify.py -i models/model_100.py -o categ-models/model_100.py
bin/destringify.py -i models/model_1000.py -o categ-models/model_1000.py
bin/destringify.py -i models/model_1500.py -o categ-models/model_1500.py
bin/destringify.py -i models/model_2000.py -o categ-models/model_2000.py
bin/destringify.py -i models/model_500.py -o categ-models/model_500.py
```

### 3 Replicate the input data set to make it more sizeable

The raw input data set contains 32561 rows. For meaningful benchmarking on a
cluster, we need more. We'll use PySpark to replicate the data set.

Using a PySpark shell on the cluster (after copying over the data):

```python
with open('/home/laserson/raw_data/bigml_53168e4dd63708516d001938.csv', 'r') as ip:
    ip.next() # burn header line
    raw = filter(lambda x: x != '', [line.strip() for line in ip])

single = sc.parallelize(raw, 5).map(lambda line: '\t'.join(line.split(',')))
replicated = single.flatMap(lambda x: [x]*15000)
replicated.saveAsTextFile('/user/laserson/bigml/census_text')
```

Also generate a data set that replaces the strings with numbers

```python
ident = lambda x: x # do nothing for strings
types = (ident, hash, ident, hash, ident, hash, hash, hash, hash, hash, ident,
	hash, hash)
categ_single = single.map(lambda line: '\t'.join([str(p[0](p[1])) for p in zip(types, line.split('\t'))]))
categ_replicated = categ_single.flatMap(lambda x: [x]*15000)
categ_replicated.saveAsTextFile('/user/laserson/bigml/census_categ_text')
```


### 3 Run model scoring in Impala

Advantages of model-scoring in Impala are that it's signficantly faster than
Spark and you can work on your local machine.  Below is some example code.  The
actual script run is `run_impala.py` or `run_impala_categ.py`.

```python
from impala.dbapi import connect
from impala.udf import ship_udf, udf, FunctionContext, StringVal, IntVal

create_table_query = """
    CREATE EXTERNAL TABLE IF NOT EXISTS census_text (age INT, workclass STRING,
	    final_weight INT, education STRING, education_num INT,
	    marital_status STRING, occupation STRING, relationship STRING,
	    race STRING, sex STRING, hours_per_week INT, native_country STRING,
	    income STRING)
    ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
    STORED AS TEXTFILE
    LOCATION '/user/laserson/bigml/census_text'
"""

score_obs_query = """
    SELECT DISTINCT predict_income(age, workclass, final_weight, education,
	    education_num, marital_status, occupation, relationship, race, sex,
	    hours_per_week, native_country, income) FROM census_text
"""

signature = StringVal(FunctionContext, IntVal, StringVal, IntVal, StringVal,
	IntVal, StringVal, StringVal, StringVal, StringVal, StringVal, IntVal,
	StringVal, StringVal)
predict_income = udf(signature)(predict_income)

ship_udf


```


### 4 Run model scoring in PySpark

```python
ident = lambda x: x # do nothing for strings
types = (int, ident, int, ident, int, ident, ident, ident, ident, ident, int,
	ident, ident)
num_fields = len(types)

def parse_obs(line):
    fields = line.split('\t')
    parsed = tuple([types[i](fields[i]) for i in xrange(num_fields)])
    return parsed

observations = sc.textFile('/user/laserson/bigml/census_text').map(parse_obs)
# the None is where the FunctionContext would go; for Impala compatibility
predictions = observations.map(lambda tup: predict_income(*((None,) + tup)))
predictions.distinct().collect()
```

### 5 Raw results

I run `bin/run_impala.py` and `bin/run_impala_categ.py` on my local machine.
For Spark, I log onto one of the nodes and run the code from a PySpark shell.

```
experiment,tree_size,code_size,execution_time,compile_time
impala,0,4,9.14,0.05
impala,100,2254,22.00,0.89
impala,500,9803,26.51,4.30
impala,1000,23495,32.00,15.95
impala,1500,28301,35.02,18.18
impala,2000,42442,36.88,30.54
impala_categ,0,4,11.27,0.03
impala_categ,100,2254,17.09,0.82
impala_categ,500,9803,18.76,3.38
impala_categ,1000,23495,19.86,8.82
impala_categ,1500,28301,21.36,13.10
impala_categ,2000,42442,22.72,22.69
spark,0,4,159.51,
spark,100,2542,174.91,
spark,500,11059,178.28,
spark,1000,26509,183.98,
spark,1500,35104,187.65,
spark,2000,47350,195.99,
spark_categ,0,4,196.37,
spark_categ,100,2542,198.81,
spark_categ,500,11059,198.79,
spark_categ,1000,26509,200.44,
spark_categ,1500,35104,200.78,
spark_categ,2000,47350,201.46,
```

Manually copied into `data/comparison.csv`.


### 6 Compute fraction memcmp nodes

```python
import re
from glob import glob
paths = glob('models/model_[1-9]*.py')
for path in paths:
    with open(path, 'r') as ip:
	lines = ip.readlines()

    num_nodes = len(filter(lambda l:  l.strip()[:2] == 'if', lines))
    num_memcmp = len(filter(lambda l: re.match(r".*if.*[!=]=.*'.*'", l) is not None, lines))
    print "%s\t%.0f" % (path, 100. * num_memcmp / num_nodes)
```

### 7 Visualize results

```python
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data/comparison.csv')
# take out the 'categ' rows
df = df.ix[df.experiment.map(lambda x: 'categ' not in x)]

x_i = df[df.experiment == 'impala'].tree_size.reset_index(drop=True)
y_i = df[df.experiment == 'impala'].execution_time.reset_index(drop=True)
x_s = df[df.experiment == 'spark'].tree_size.reset_index(drop=True)
y_s = df[df.experiment == 'spark'].execution_time.reset_index(drop=True)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x_i, y_i)
ax.plot(x_s, y_s)
fig.show()

x = df[df.experiment == 'impala'].code_size.reset_index(drop=True)
y = df[df.experiment == 'impala'].compile_time.reset_index(drop=True)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y)
fig.show()

```