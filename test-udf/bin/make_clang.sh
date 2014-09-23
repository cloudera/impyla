#! /usr/bin/env bash
cd $IMPYLA_HOME/test-udf/clang && cmake . && make
cat $IMPYLA_HOME/test-udf/clang/build/*.ll | $(brew --prefix llvm)/bin/llvm-dis > $IMPYLA_HOME/test-udf/clang/build/test-udf-clang.ll.txt
