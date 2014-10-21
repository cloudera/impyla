# First check if the nightly cluster build succeeded
cd /tmp
curl -s -O -L http://stedolan.github.io/jq/download/linux64/jq
chmod 755 jq
NIGHTLY_STATUS=$(curl -s -L "http://golden.jenkins.sf.cloudera.com/view/CM/view/CM-Trunk/job/CM-Refresh-Nightly-Cluster/lastBuild/api/json" \ | /tmp/jq -r '.result')
if [ "$NIGHTLY_STATUS" != "SUCCESS" ]; then
    echo "CM-Refresh-Nightly-Cluster job failed; aborting impyla with FAIL"
    exit 1
fi

# Install all the necessary prerequisites
cd /tmp
virtualenv impyla-it-pyenv-$BUILD_NUMBER
source impyla-it-pyenv-$BUILD_NUMBER/bin/activate
pip install pytest
pip install thrift
pip install unittest2
pip install numpy
pip install pandas
pip install pywebhdfs
# pull latest llvmpy and numba to catch errors as early as possible
pip install git+https://github.com/llvmpy/llvmpy.git@master
pip install git+https://github.com/numba/numba.git@master

# Build impyla
cd $WORKSPACE ; make ; python setup.py install

# Run testing suite
cd /tmp; py.test --dbapi-compliance $WORKSPACE/impala/tests
deactivate
