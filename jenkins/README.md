## Jenkins testing using the internal Cloudera sandbox environment

All the `impyla` jobs are prefixed with `impyla-`.

Testing occurs against either:

* the `nightly` build of CM/CDH or

* the stable `bottou` cluster

The tests run are either:

* DB API (PEP 249)-only (`run-dbapi.sh`)

* All tests, including UDF (`run-all.sh`)

The two main scripts specify the necessary environment variables that must be
set.  This also includes testing either HiveServer2 or Beeswax for
connectivity, and using released versus master versions of Numba.

Finally, the jobs that run against `nightly` will only start if the `nightly`
build succeeds.  This is accomplished by creating a dependence on a job called
`golden-nightly-success`, which runs a script like

```bash
NIGHTLY_URL="http://golden.jenkins.sf.cloudera.com/job/CM-Master-Refresh-Nightly-Cluster/lastBuild/api/json"
NIGHTLY_STATUS=$(curl -s -L "$NIGHTLY_URL" | $WORKSPACE/jenkins/parse-build-result.py)
if [ "$NIGHTLY_STATUS" != "SUCCESS" ]; then exit 1; fi
```
