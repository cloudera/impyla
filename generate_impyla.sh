#! /usr/bin/env bash

export IMPALA_REPO="/Users/laserson/cloudera/repos/Impala"
export IMPYLA_REPO="/Users/laserson/repos/impyla"

mkdir -p $IMPYLA_REPO/thrift

# copy over thrift dependencies
cp $IMPALA_REPO/common/thrift/cli_service.thrift $IMPYLA_REPO/thrift

# generate the python code
thrift -gen py:new_style -out $IMPYLA_REPO/lib $IMPYLA_REPO/thrift/cli_service.thrift
