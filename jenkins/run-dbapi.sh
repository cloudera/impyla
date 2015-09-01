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
: ${IMPYLA_TEST_HOST:?"IMPYLA_TEST_HOST is unset"}
: ${IMPYLA_TEST_PORT:?"IMPYLA_TEST_PORT is unset"}
: ${IMPYLA_TEST_AUTH_MECH:?"IMPYLA_TEST_AUTH_MECH is unset"}
: ${PYTHON_VERSION:?"PYTHON_VERSION is unset"}
# the following are set by jenkins and are only needed if WORKSPACE not set
#   GIT_URL
#   GIT_BRANCH
# and for pulling in a pull request
#   GITHUB_PR
# For reporting to codecov.io, set
#   CODECOV_TOKEN

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
if [ -z "$WORKSPACE" -a -n "$GITHUB_PR" ]; then
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
pip install thriftpy sqlalchemy
pip install unittest2 pytest-cov codecov prospector[with_pyroma]

# build impyla
pip install $IMPYLA_HOME

python --version
which python

python -c "from impala.tests.util import ImpylaTestEnv; print(ImpylaTestEnv())"

if [ $IMPYLA_TEST_AUTH_MECH != "NOSASL" ]; then
    pip install git+https://github.com/laserson/python-sasl.git@cython
    kinit -l 4h -kt /cdep/keytabs/systest.keytab systest
fi

cd $IMPYLA_HOME

# Run PEP 249 testing suite
py.test --connect \
    --cov impala \
    --cov-report xml --cov-report term \
    --cov-config .coveragerc \
    impala

# Enforce PEP 8 etc
if [ $PYTHON_VERSION != "2.6" ]; then
    prospector
fi

# Report code coverage to codecov.io
if [ -n $CODECOV_TOKEN ]; then
    bash <(curl -s https://codecov.io/bash) -t $CODECOV_TOKEN
fi
