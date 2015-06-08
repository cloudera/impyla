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
: ${PYTHON_VERSION:?"PYTHON_VERSION is unset"}

mkdir -p /tmp/impyla-dbapi/$BUILD_NUMBER
TMP_DIR=$(mktemp -d -p /tmp/impyla-dbapi/$BUILD_NUMBER tmpXXXX)

function cleanup {
    rm -rf $TMP_DIR
}
trap cleanup EXIT

# Build requested Python version
cd $TMP_DIR
wget https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tgz
tar -xzf Python-$PYTHON_VERSION.tgz
cd Python-$PYTHON_VERSION
./configure --prefix=$TMP_DIR
make && make altinstall

PY_MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
PY_MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)
PY_BIN_DIR=$TMP_DIR/bin
PY_EXEC=$PY_BIN_DIR/python$PY_MAJOR.$PY_MINOR

$PY_EXEC --version
which $PY_EXEC

# Install pip and virtualenv
curl https://bootstrap.pypa.io/get-pip.py | $PY_EXEC
$PY_BIN_DIR/pip install virtualenv

# Set up virtualenv and install prereqs
cd $TMP_DIR
VENV_NAME=impyla-dbapi-pyvenv-$BUILD_NUMBER
$PY_BIN_DIR/virtualenv -p $PY_EXEC $VENV_NAME
source $VENV_NAME/bin/activate
pip install pytest
if [ "$PY_MAJOR" -eq "2" -a "$PY_MINOR" -le "6" ]; then
    pip install unittest2  # for Python <= 2.6
fi

# Build impyla
cd $WORKSPACE && pip install .

# Run PEP 249 testing suite
cd $TMP_DIR && py.test --pyargs impala.tests.test_dbapi_compliance

deactivate
