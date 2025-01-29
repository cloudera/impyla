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

* Python 2.7+ or 3.5+

* `six`, `bitarray`

* `thrift==0.16.0`

* `thrift_sasl==0.4.3`

Optional:

* `kerberos>=1.3.0` for Kerberos over HTTP support. This also requires Kerberos libraries
   to be installed on your system - see [System Kerberos](#system-kerberos)

* `pandas` for conversion to `DataFrame` objects; but see the [Ibis project][ibis] instead

* `sqlalchemy` for the SQLAlchemy engine

* `pytest` and `requests` for running tests; `unittest2` for testing on Python 2.6


#### System Kerberos

Different systems require different packages to be installed to enable Kerberos support in
Impyla. Some examples of how to install the packages on different distributions follow.

Ubuntu:
```bash
apt-get install libkrb5-dev krb5-user
```

RHEL/CentOS:
```bash
yum install krb5-libs krb5-devel krb5-server krb5-workstation
```

### Installation

Install the latest release with `pip`:

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
py.test --connect impala
```

Leave out the `--connect` option to skip tests for DB API compliance.

To test impyla with different Python versions [tox] can be used.
The commands below will run all impyla tests with all supported and
installed Python versions:
```bash
cd path/to/impyla
tox
```
To filter environments / tests use `-e` and [pytest] arguments after `--`:
```bash
tox -e py310 -- -ktest_utf8_strings
```

### Usage

Impyla implements the [Python DB API v2.0 (PEP 249)][pep249] database interface
(refer to it for API details):

```python
from impala.dbapi import connect
conn = connect(host='my.host.com', port=21050) # auth_mechanism='PLAIN' for unsecured Hive connection, see function doc
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
    print(row)
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
[pytest]: http://pytest.org/latest/
[sqlalchemy]: http://www.sqlalchemy.org/
[ibis]: http://www.ibis-project.org/
[tox]: http://tox.wiki/

# How do I contribute code?
You need to first sign and return an
[ICLA](https://github.com/cloudera/native-toolchain/blob/icla/Cloudera%20ICLA_25APR2018.pdf)
and
[CCLA](https://github.com/cloudera/native-toolchain/blob/icla/Cloudera%20CCLA_25APR2018.pdf)
before we can accept and redistribute your contribution. Once these are submitted you are
free to start contributing to impyla. Submit these to CLA@cloudera.com.

## Find
We use Github issues to track bugs for this project. Find an issue that you would like to
work on (or file one if you have discovered a new issue!). If no-one is working on it,
assign it to yourself only if you intend to work on it shortly.

It's a good idea to discuss your intended approach on the issue. You are much more
likely to have your patch reviewed and committed if you've already got buy-in from the
impyla community before you start.

## Fix
Now start coding! As you are writing your patch, please keep the following things in mind:

First, please include tests with your patch. If your patch adds a feature or fixes a bug
and does not include tests, it will generally not be accepted. If you are unsure how to
write tests for a particular component, please ask on the issue for guidance.

Second, please keep your patch narrowly targeted to the problem described by the issue.
It's better for everyone if we maintain discipline about the scope of each patch. In
general, if you find a bug while working on a specific feature, file a issue for the bug,
check if you can assign it to yourself and fix it independently of the feature. This helps
us to differentiate between bug fixes and features and allows us to build stable
maintenance releases.

Finally, please write a good, clear commit message, with a short, descriptive title and
a message that is exactly long enough to explain what the problem was, and how it was
fixed.

Please create a pull request on github with your patch.
