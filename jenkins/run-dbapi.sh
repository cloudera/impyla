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

# Set up virtualenv and install prereqs
VENV_NAME=$JOB_NAME-pyvenv-$BUILD_NUMBER
cd /tmp && virtualenv $VENV_NAME && source $VENV_NAME/bin/activate
pip install pytest
pip install thrift
pip install unittest2

# Build impyla
cd $WORKSPACE && python setup.py install

# Run PEP 249 testing suite
cd /tmp && py.test --dbapi-compliance $WORKSPACE/impala/tests/test_dbapi_compliance.py

# Cleanup virtualenv
deactivate && rm -rf /tmp/$VENV_NAME
