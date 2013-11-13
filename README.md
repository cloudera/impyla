# impyla

Python client to Cloudera Impala.


## Rationale and vision

Impala allows you to rapidly analyze large, distributed data sets.  But it
doesn't integrate easily with your ad hoc (Python) analytical tools (pandas,
scikit-learn).  impyla aims to remedy this.

This package offers:

* Lightweight, `pip`-installable package for Impala-driven analytics anywhere

* Integration with [pandas][1] (and therefore the rest of the Python data stack,
including [scikit-learn][2] and [matplotlib][3])

* Integration with [MADlib][4], enabling scalable, in-database, distributed
machine learning (see [the Impala port of MADlib][5])

Eventually, we'll also support:

* Integration with [Spark][6]

* Running Python UDFs by compiling them to LLVM IR


## Installation

Requires `thrift>=0.9`.

    pip install impyla

or from the repo

    git clone git://github.com/laserson/impyla.git
    cd impyla
    python setup.py install


## Quickstart

Impyla implements the Python DB API 2 (PEP 249)

    import impala.dbapi
    conn = impala.dbapi.connect(host='my.host.com', port=21050)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM table LIMIT 100')
    for row in cursor:
        process(row)

You can also get back a pandas DataFrame object
    
    import impala.pandas
    df = impala.pandas.Cursor2DataFrame(cur)
    # carry df through scikit-learn, for example


[1]: http://pandas.pydata.org/
[2]: http://scikit-learn.org/
[3]: http://matplotlib.org/
[4]: http://madlib.net/
[5]: https://github.com/bitfort/madlibport
[6]: http://spark.incubator.apache.org/
