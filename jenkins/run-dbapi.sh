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

set -e
set -x

# Check for necessary environment variables
: ${IMPALA_HOST:?"IMPALA_HOST is unset"}
: ${IMPALA_PROTOCOL:?"IMPALA_PROTOCOL is unset"}
: ${IMPALA_PORT:?"IMPALA_PORT is unset"}
: ${PYTHON_VERSION:?"PYTHON_VERSION is unset"}
: ${USE_KERBEROS:?"USE_KERBEROS is unset"}
# the following are set by jenkins and are only needed if WORKSPACE not set
#   GIT_URL
#   GIT_BRANCH

printenv

mkdir -p /tmp/impyla-dbapi
TMP_DIR=$(mktemp -d -p /tmp/impyla-dbapi tmpXXXX)

function cleanup {
    rm -rf $TMP_DIR
}
trap cleanup EXIT

cd $TMP_DIR

# checkout impyla if necessary
# this is necessary when run via SSH on a kerberized node
if [ -z "$WORKSPACE" ]; then
    : ${GIT_URL:?"GIT_URL is unset"}
    : ${GIT_BRANCH:?"GIT_BRANCH is unset"}
    git clone $GIT_URL
    pushd impyla && git checkout origin/$GIT_BRANCH && popd
    IMPYLA_HOME=$TMP_DIR/impyla
else
    # WORKSPACE is set, so I must be on a Jenkins slave
    IMPYLA_HOME=$WORKSPACE
fi

# pull in PR if necessary
if [ -n "$GITHUB_PR" ]; then
    pushd $IMPYLA_HOME
    git clean -d -f
    git fetch origin pull/$GITHUB_PR/head:pr_$GITHUB_PR
    git checkout pr_$GITHUB_PR
    popd
fi

# Setup Python
curl https://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh > miniconda.sh
bash miniconda.sh -b -p $TMP_DIR/miniconda
export PATH="$TMP_DIR/miniconda/bin:$PATH"
conda update -y -q conda
conda info -a

# Install impyla and deps into new environment
CONDA_ENV_NAME=pyenv-impyla-dbapi-test
conda create -y -q -n $CONDA_ENV_NAME python=$PYTHON_VERSION
source activate $CONDA_ENV_NAME
pip install unittest2 pytest
# build impyla
pip install $IMPYLA_HOME

python --version
which python

if [ $USE_KERBEROS = "True" ]; then
    pip install git+https://github.com/laserson/python-sasl.git@cython
    kinit -l 4h -kt /cdep/keytabs/systest.keytab systest
fi

# Run PEP 249 testing suite
py.test --pyargs impala.tests.test_dbapi_compliance
