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

if [ -z "$IMPALA_REPO" ]; then
    echo "Need to set IMPALA_REPO"
    exit 1
fi

if [ -z "$IMPYLA_REPO" ]; then
    echo "Need to set IMPYLA_REPO"
    exit 1
fi

echo "copying thrift files from the main Impala repo"
cp $IMPALA_REPO/common/thrift/TCLIService.thrift $IMPYLA_REPO/impala/thrift
cp $IMPALA_REPO/common/thrift/ImpalaService.thrift $IMPYLA_REPO/impala/thrift
cp $IMPALA_REPO/common/thrift/ExecStats.thrift $IMPYLA_REPO/impala/thrift
cp $IMPALA_REPO/common/thrift/Status.thrift $IMPYLA_REPO/impala/thrift
cp $IMPALA_REPO/common/thrift/Types.thrift $IMPYLA_REPO/impala/thrift
cp $IMPALA_REPO/thirdparty/thrift-*/contrib/fb303/if/fb303.thrift $IMPYLA_REPO/impala/thrift

# beeswax.thrift already includes a namespace py declaration, which breaks my
# directory structure, so here I delete it (in preparation for adding the proper
# namespace declaration below)
grep -v 'namespace py beeswaxd' $IMPALA_REPO/common/thrift/beeswax.thrift \
        > $IMPYLA_REPO/impala/thrift/beeswax.thrift

# hive_metastore.thrift assumes a directory structure for fb303.thrift, so we
# change the include statement here
cat $IMPALA_REPO/thirdparty/hive-*/src/metastore/if/hive_metastore.thrift \
        | sed 's/share\/fb303\/if\///g' \
        > $IMPYLA_REPO/impala/thrift/hive_metastore.thrift

# we add "namespace py" statements to all the thrift files so we can get the
# appropriate directory structure
echo "adding namespace py lines to thrift files"
for THRIFT_FILE in $IMPYLA_REPO/impala/thrift/*.thrift; do
    FILE_NAME=$(basename $THRIFT_FILE)
    BASE_NAME=${FILE_NAME%.*}
    ADD_NAMESPACE_PY="
        BEGIN {
            n = 0
        }
        {
            if (\$0 ~ /^namespace/ && n == 0) {
                print \"namespace py impala._thrift_gen.$BASE_NAME\";
                n += 1;
            }
            print \$0;
        }"
    echo "    $BASE_NAME"
    cat $THRIFT_FILE | awk "$ADD_NAMESPACE_PY" > $IMPYLA_REPO/impala/thrift/temp.thrift
    mv $IMPYLA_REPO/impala/thrift/temp.thrift $THRIFT_FILE
done

echo "generating thrift python modules"
thrift -r --gen py:new_style -out $IMPYLA_REPO $IMPYLA_REPO/impala/thrift/ImpalaService.thrift

echo "removing extraneous $IMPYLA_REPO/__init__.py"
rm -f $IMPYLA_REPO/__init__.py
