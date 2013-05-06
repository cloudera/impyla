impyla
======

Python client to Cloudera Impala

(Built for Impala 0.7; uses beeswax)


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
