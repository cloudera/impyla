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

# Check for necessary environment variables
: ${IMPALA_HOST:?"IMPALA_HOST is unset"}
: ${IMPALA_PROTOCOL:?"IMPALA_PROTOCOL is unset"}
: ${IMPALA_PORT:?"IMPALA_PORT is unset"}
: ${NAMENODE_HOST:?"NAMENODE_HOST is unset"}
: ${WEBHDFS_PORT:?"WEBHDFS_PORT is unset"}
: ${LLVM_CONFIG_PATH:?"LLVM_CONFIG_PATH is unset"}
: ${NUMBA_VERSION:?"NUMBA_VERSION is unset"}

# Set up virtualenv and install prereqs
VENV_NAME=$JOB_NAME-pyvenv-$BUILD_NUMBER
cd /tmp && virtualenv $VENV_NAME && source $VENV_NAME/bin/activate
pip install pytest
pip install thrift
pip install sasl
pip install unittest2
pip install sqlalchemy
pip install numpy
pip install pandas
pip install hdfs[kerberos]
if [ "$NUMBA_VERSION" == "master" ]; then
    pip install git+https://github.com/llvmpy/llvmpy.git@master
    pip install git+https://github.com/numba/numba.git@master
elif [ "$NUMBA_VERSION" == "release" ]; then
    pip install llvmpy
    pip install numba==0.13.4
else
    echo "NUMBA_VERSION must be 'master' or 'release'; got $NUMBA_VERSION"
    exit 1
fi

# Build impyla
cd $WORKSPACE && make clean && make && python setup.py install

# Run testing suite
cd /tmp && py.test --dbapi-compliance $WORKSPACE/impala/tests

# cleanup
deactivate && rm -rf /tmp/$VENV_NAME
