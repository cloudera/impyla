# impyla

Python client for the Impala distributed query engine.


### Features

Fully supported:

* Lightweight, `pip`-installable package for connecting to Impala databases

* Fully [DB API 2.0 (PEP 249)][pep249]-compliant Python client (similar to
sqlite or MySQL clients)

* Support for HiveServer2 and Beeswax; support for Kerberos

* Converter to [pandas][pandas] `DataFrame`, allowing easy integration into the
Python data stack (including [scikit-learn][sklearn] and
[matplotlib][matplotlib])

In various phases of maturity:

* SQLAlchemy connector; integration with Blaze

* `BigDataFrame` abstraction for performing `pandas`-style analytics on large
datasets (similar to Spark's RDD abstraction); computation is pushed into the
Impala engine.

* `scikit-learn`-flavored wrapper for [MADlib][madlib]-style prediction,
allowing for large-scale, distributed machine learning (see
[the Impala port of MADlib][madlibport])

* Compiling UDFs written in Python into low-level machine code for execution by
Impala (powered by [Numba][numba]/[LLVM][llvm])


### Dependencies

Required for DB API connectivity:

* `python2.6` or `python2.7`

* `six`

* `thrift>=0.8` (Python package only; no need for code-gen)

Required for UDFs:

* `numba<=0.13.4` (which has a few requirements, like LLVM)

* `boost` (because `udf.h` depends on `boost/cstdint.hpp`)

Required for SQLAlchemy integration (and Blaze):

* `sqlalchemy`

Required for `BigDataFrame`:

* `pandas`

Required for utilizing automated shipping/registering of code/UDFs/BDFs/etc:

* `pywebhdfs`

For manipulating results as pandas `DataFrame`s, we recommend installing pandas
regardless.

Generally, we recommend installing all the libraries above; the UDF libraries
will be the most difficult, and are not required if you will not use any Python
UDFs.  Interacting with Impala using the `ImpalaContext` will simplify shipping
data and will perform cleanup on temporary data/tables.

This project is installed with `setuptools`.

### Installation

Install the latest release (`0.9.0`) with `pip`:

```bash
pip install impyla
```

For the latest (dev) version, clone the repo:

```bash
git clone https://github.com/cloudera/impyla.git
cd impyla
make # optional: only for Numba-compiled UDFs; requires LLVM/clang
python setup.py install
```

#### Running the tests

impyla uses the [pytest][pytest] toolchain, and depends on the following environment
variables:

```bash
export IMPALA_HOST=your.impalad.com
# beeswax might work here too
export IMPALA_PORT=21050
export IMPALA_PROTOCOL=hiveserver2
# needed to push data to the cluster
export NAMENODE_HOST=bottou01-10g.pa.cloudera.com
export WEBHDFS_PORT=50070
```

To run the maximal set of tests, run

```bash
py.test --dbapi-compliance path/to/impyla/impala/tests
```

Leave out the `--dbapi-compliance` option to skip tests for DB API compliance.
Add a `--udf` option to only run local UDF compilation tests.


### Quickstart

Impyla implements the [Python DB API v2.0 (PEP 249)][pep249] database interface
(refer to it for API details):

```python
from impala.dbapi import connect
conn = connect(host='my.host.com', port=21050)
cursor = conn.cursor()
cursor.execute('SELECT * FROM mytable LIMIT 100')
print cursor.description # prints the result set's schema
results = cursor.fetchall()
```

**Note**: if connecting to Impala through the *HiveServer2* service, make sure
to set the port to the HiveServer2 port (defaults to 21050 in CM), not Beeswax
(defaults to 21000) which is what the Impala shell uses.

The `Cursor` object also supports the iterator interface, which is buffered
(controlled by `cursor.arraysize`):

```python
cursor.execute('SELECT * FROM mytable LIMIT 100')
for row in cursor:
    process(row)
```

You can also get back a pandas DataFrame object
    
```python
from impala.util import as_pandas
df = as_pandas(cur)
# carry df through scikit-learn, for example
```


[pep249]: http://legacy.python.org/dev/peps/pep-0249/
[pandas]: http://pandas.pydata.org/
[sklearn]: http://scikit-learn.org/
[matplotlib]: http://matplotlib.org/
[madlib]: http://madlib.net/
[madlibport]: https://github.com/bitfort/madlibport
[numba]: http://numba.pydata.org/
[llvm]: http://llvm.org/
[pytest]: http://pytest.org/latest/
