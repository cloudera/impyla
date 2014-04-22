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

PREFIX=impala/udf/precompiled
INCLUDE_DIR=$(PREFIX)
SRC_FILE=$(PREFIX)/impala-precompiled.cc
OUTPUT_FILE=$(PREFIX)/impala-precompiled.bc

# if LLVM_CONFIG unset, try the default
if [ -z $(LLVM_CONFIG) ]; then LLVM_CONFIG=`which llvm-config`; fi;
ifndef LLVM_CONFIG
$(error llvm-config not in PATH -- please set LLVM_CONFIG=path/to/llvm-config)
endif
CLANG=$(shell $(LLVM_CONFIG) --bindir)/clang++

all:
	$(CLANG) -emit-llvm -O0 -I $(INCLUDE_DIR) -c $(SRC_FILE) -o $(OUTPUT_FILE)

clean:
	rm -f $(OUTPUT_FILE)
