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
OUTPUT_FILE=$(PREFIX)/impyla.bc

# if LLVM_CONFIG_PATH unset, try the default
if [ -z $(LLVM_CONFIG_PATH) ]; then LLVM_CONFIG_PATH=$(which llvm-config); fi;
ifndef LLVM_CONFIG_PATH
$(error llvm-config not in PATH -- please set LLVM_CONFIG_PATH=path/to/llvm-config)
endif
CLANG=$(shell $(LLVM_CONFIG_PATH) --bindir)/clang++
LINK=$(shell $(LLVM_CONFIG_PATH) --bindir)/llvm-link

all:
	$(CLANG) -c -emit-llvm -O0 -o $(PREFIX)/impala-types.bc $(PREFIX)/impala-types.cc
	$(CLANG) -c -emit-llvm -O0 -o $(PREFIX)/string-impl.bc $(PREFIX)/string-impl.cc
	$(LINK) -o $(OUTPUT_FILE) $(PREFIX)/*.bc

clean:
	rm -f $(PREFIX)/*.bc
