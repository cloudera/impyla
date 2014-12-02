## Testing against a nightly on Cloudera internal Jenkins

To configure a Jenkins job to test impyla, you must inject the following
environment variables.  These variables make some assumption related to
Cloudera's internal CM/CDH testing.

```bash
# example config
HOST_SHORT_NAME=nightly
NIGHTLY_JOB_NAME=CM-Master-Refresh-Nightly-Cluster
PYMODULE_VERSIONS=master
IMPALA_PROTOCOL=hiveserver2
```

Here are possible values for the variables:

`HOST_SHORT_NAME` and `NIGHTLY_JOB_NAME`:

* `nightly` and `CM-Master-Refresh-Nightly-Cluster`

* `nightly52` and `CM-Refresh-5.2-Cluster`

* `nightly-kerberized` and `CM-Refresh-Nightly-Kerberos-Cluster`


`PYMODULE_VERSIONS`

* `master`

* `release`


`IMPALA_PROTOCOL`

* `hiveserver2`

* `beeswax`


## Testing against bottou using Cloudera internal Jenkins

Set the following vars

```bash
# example config
PYMODULE_VERSIONS=master
IMPALA_PROTOCOL=hiveserver2
```

Possible values are as above.
