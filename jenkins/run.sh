#! /usr/bin/env bash
# Copyright 2014 Cloudera Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# See README.md for necessary environment variables for this script

# First check if the nightly cluster build succeeded
NIGHTLY_STATUS=$(curl -s -L "http://golden.jenkins.sf.cloudera.com/job/$NIGHTLY_JOB_NAME/lastBuild/api/json" \
    | $WORKSPACE/jenkins/parse_build_result.py)
if [ "$NIGHTLY_STATUS" != "SUCCESS" ]; then
    echo "$NIGHTLY_JOB_NAME Jenkins job failed"
    echo "aborting impyla Jenkins job with FAIL"
    exit 1
fi

# Set up necessary vars
export IMPALA_HOST=$HOST_SHORT_NAME-2.ent.cloudera.com
if [ "$IMPALA_PROTOCOL" == "hiveserver2" ]; then
    export IMPALA_PORT=21050
elif [ "$IMPALA_PROTOCOL" == "beeswax" ]; then
    export IMPALA_PORT=21000
else
    echo "IMPALA_PROTOCOL must be set to 'hiveserver2' or 'beeswax'; got $IMPALA_PROTOCOL"
    echo "aborting impyla Jenkins job with FAIL"
    exit 1
fi
export NAMENODE_HOST=$HOST_SHORT_NAME-1.ent.cloudera.com
export WEBHDFS_PORT=20101
export LLVM_CONFIG_PATH=/opt/toolchain/llvm-3.3/bin/llvm-config
VENV_NAME=impyla-it-pyenv-$HOST_SHORT_NAME-$PYMODULE_VERSIONS-$IMPALA_PROTOCOL-$BUILD_NUMBER

# Install all the necessary prerequisites
cd /tmp
virtualenv $VENV_NAME
source $VENV_NAME/bin/activate
pip install pytest
pip install thrift
pip install unittest2
pip install numpy
pip install pandas
pip install pywebhdfs
if [ "$PYMODULE_VERSIONS" == "master" ]; then
    pip install git+https://github.com/llvmpy/llvmpy.git@master
    pip install git+https://github.com/numba/numba.git@master
elif [ "$PYMODULE_VERSIONS" == "release" ]; then
    pip install llvmpy
    pip install numba
else
    echo "PYMODULE_VERSIONS must be 'master' or 'release'; got $PYMODULE_VERSIONS"
    echo "aborting impyla Jenkins job with FAIL"
    exit 1
fi

# Build impyla
cd $WORKSPACE && make clean && make && python setup.py install

# Run testing suite
cd /tmp && py.test --dbapi-compliance $WORKSPACE/impala/tests

# cleanup
deactivate && rm -rf /tmp/$VENV_NAME
