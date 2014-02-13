#! /usr/bin/env bash
cd $IMPYLA_HOME/test-udf/numba && python impala_udf.py
cat $IMPYLA_HOME/test-udf/numba/build/*.ll | $(brew --prefix llvm)/bin/llvm-dis > $IMPYLA_HOME/test-udf/numba/build/test-udf-numba.ll.txt