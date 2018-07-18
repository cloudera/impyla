# impyla

Python client for HiveServer2 implementations (e.g., Impala, Hive) for
distributed query engines.

For higher-level Impala functionality, including a Pandas-like interface over
distributed data sets, see the [Ibis project][ibis].

### Features

* HiveServer2 compliant; works with Impala and Hive, including nested data

* Fully [DB API 2.0 (PEP 249)][pep249]-compliant Python client (similar to
sqlite or MySQL clients) supporting Python 2.6+ and Python 3.3+.

* Works with Kerberos, LDAP, SSL

* [SQLAlchemy][sqlalchemy] connector

* Converter to [pandas][pandas] `DataFrame`, allowing easy integration into the
Python data stack (including [scikit-learn][sklearn] and
[matplotlib][matplotlib]); but see the [Ibis project][ibis] for a richer
experience

### Dependencies

Required:

* Python 2.6+ or 3.3+

* `six`, `bit_array`

* `thrift`

For Hive and/or Kerberos support:

```
pip install thrift_sasl==0.2.1
pip install sasl
```

Optional:

* `pandas` for conversion to `DataFrame` objects; but see the [Ibis project][ibis] instead

* `sqlalchemy` for the SQLAlchemy engine

* `pytest` for running tests; `unittest2` for testing on Python 2.6


### Installation

Install the latest release (`0.13.1`) with `pip`:

```bash
pip install impyla
```

For the latest (dev) version, install directly from the repo:

```bash
pip install git+https://github.com/cloudera/impyla.git
```

or clone the repo:

```bash
git clone https://github.com/cloudera/impyla.git
cd impyla
python setup.py install
```

#### Running the tests

impyla uses the [pytest][pytest] toolchain, and depends on the following
environment variables:

```bash
export IMPYLA_TEST_HOST=your.impalad.com
export IMPYLA_TEST_PORT=21050
export IMPYLA_TEST_AUTH_MECH=NOSASL
```

To run the maximal set of tests, run

```bash
cd path/to/impyla
py.test --connect impyla
```

Leave out the `--connect` option to skip tests for DB API compliance.


### Usage

Impyla implements the [Python DB API v2.0 (PEP 249)][pep249] database interface
(refer to it for API details):

```python
from impala.dbapi import connect
conn = connect(host='my.host.com', port=21050)
cursor = conn.cursor()
cursor.execute('SELECT * FROM mytable LIMIT 100')
print cursor.description  # prints the result set's schema
results = cursor.fetchall()
```

The `Cursor` object also exposes the iterator interface, which is buffered
(controlled by `cursor.arraysize`):

```python
cursor.execute('SELECT * FROM mytable LIMIT 100')
for row in cursor:
    process(row)
```

Furthermore the `Cursor` object returns you information about the columns
returned in the query. This is useful to export your data as a csv file.

```python
import csv

cursor.execute('SELECT * FROM mytable LIMIT 100')
columns = [datum[0] for datum in cursor.description]
targetfile = '/tmp/foo.csv'

with open(targetfile, 'w', newline='') as outcsv:
    writer = csv.writer(outcsv, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n')
    writer.writerow(columns)
    for row in cursor:
        writer.writerow(row)
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
[sqlalchemy]: http://www.sqlalchemy.org/
[ibis]: http://www.ibis-project.org/
[python-sasl-cython]: https://github.com/laserson/python-sasl/tree/cython/sasl
