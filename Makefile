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
