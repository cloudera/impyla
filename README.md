#impyla

Python client to Cloudera Impala.

####Rationale/vision

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



Installation
------------

Uses setuptools/distribute.

Requires `thrift>=0.9`.

Currently:

    git clone git://github.com/laserson/impyla.git
    cd impyla
    python setup.py install

Eventually:

    pip install impyla


Usage
-----

    import impala
    client = impala.ImpalaBeeswaxClient('host:port')
    client.connect()
    results = client.execute(query)

Note that `query` gets parsed by `impalad`, not the `impala-shell`, so do not do
things like add semicolons to the end of the query.

[1]: http://pandas.pydata.org/
[2]: http://scikit-learn.org/
[3]: http://matplotlib.org/
[4]: http://madlib.net/
[5]: https://github.com/bitfort/madlibport
[6]: http://spark.incubator.apache.org/
[7]: 