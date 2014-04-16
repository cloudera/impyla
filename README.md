# impyla

Python client for the Impala distributed query engine.


### Features

Fully supported:

* Lightweight, `pip`-installable package for connecting to Impala databases

* Fully [DB API 2.0 (PEP 249)][pep249]-compliant Python client (similar to
sqlite or MySQL clients)

* Converter to [pandas][pandas] `DataFrame`, allowing easy integration into the
Python data stack (including [scikit-learn][sklearn] and
[matplotlib][matplotlib])

Alpha-quality:

* Wrapper for [MADlib][madlib]-style prediction, allowing for large-scale,
distributed machine learning (see [the Impala port of MADlib][madlibport])

* Compiling UDFs written in Python into low-level machine code for execution by
Impala (see the [`udf`](https://github.com/cloudera/impyla/tree/udf) branch;
powered by [Numba][numba]/[LLVM][llvm])


### Dependencies

Required:

* `python2.6` or `python2.7`

* `thrift>=0.8` (Python package only; no need for code-gen)

Optional:

* `pandas` for the `.as_pandas()` function to work

This project is installed with `setuptools>=2`.

### Installation

Install the latest release (`0.8.1`) with `pip`:

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

**Note**: the specified port number should be for the *HiveServer2* service
(defaults to 21050 in CM), not Beeswax (defaults to 21000) which is what the
Impala shell uses.

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
