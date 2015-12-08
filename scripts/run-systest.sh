#! /usr/bin/env bash
# Copyright 2015 Cloudera Inc.
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

# Check for necessary externally-set environment variables
: ${IMPYLA_TEST_HOST:?"IMPYLA_TEST_HOST is unset"}
: ${IMPYLA_TEST_PORT:?"IMPYLA_TEST_PORT is unset"}
: ${IMPYLA_TEST_AUTH_MECH:?"IMPYLA_TEST_AUTH_MECH is unset"}
: ${IMPYLA_TEST_USE_SSL:?"IMPYLA_TEST_USE_SSL is unset"}
: ${IMPYLA_TEST_PYTHON_VERSION:?"IMPYLA_TEST_PYTHON_VERSION is unset"}
: ${IMPYLA_TEST_CODECOV_TOKEN:?"IMPYLA_TEST_CODECOV_TOKEN is unset"}

GIT_URL="https://github.com/cloudera/impyla.git"
GIT_BRANCH="master"

printenv

# create the local temporary working space
mkdir -p /tmp
TMP_DIR=$(mktemp -d -p /tmp tmp_impyla_XXXX)
function cleanup_tmp_dir {
    cd ~
    rm -rf $TMP_DIR
}
trap cleanup_tmp_dir EXIT

cd $TMP_DIR

# checkout impyla
git clone $GIT_URL
pushd impyla && git checkout origin/$GIT_BRANCH && popd
IMPYLA_HOME=$TMP_DIR/impyla

# setup Python
curl https://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh > miniconda.sh
bash miniconda.sh -b -p $TMP_DIR/miniconda
export PATH="$TMP_DIR/miniconda/bin:$PATH"
conda update -y -q conda
conda info -a

# install impyla and deps into new environment
CONDA_ENV_NAME=pyenv-impyla-test
conda create -y -q -n $CONDA_ENV_NAME python=$IMPYLA_TEST_PYTHON_VERSION pip
source activate $CONDA_ENV_NAME
pip install thriftpy sqlalchemy
pip install unittest2 pytest-cov
# Hive and Kerberos need sasl: sudo yum install -y cyrus-sasl-devel
pip install git+https://github.com/cloudera/python-sasl.git@cython
python --version
which python

# build impyla
pip install $IMPYLA_HOME

# print test environment
python -c "from impala.tests.util import ImpylaTestEnv; print(ImpylaTestEnv())"

cd $IMPYLA_HOME

# Run PEP 249 testing suite
py.test --connect \
    --cov impala \
    --cov-report xml --cov-report term \
    --cov-config .coveragerc \
    impala

# Report code coverage to codecov.io
if [ -n $IMPYLA_TEST_CODECOV_TOKEN ]; then
    bash <(curl -s https://codecov.io/bash) -t $IMPYLA_TEST_CODECOV_TOKEN
fi
