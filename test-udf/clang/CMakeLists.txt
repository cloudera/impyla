cmake_minimum_required(VERSION 2.6)

# where to put generated libraries
set(LIBRARY_OUTPUT_PATH "build")
# where to put generated binaries
set(EXECUTABLE_OUTPUT_PATH "build")

find_program(CLANG_EXECUTABLE clang++)

# Function to generate rule to cross compile a source file to an IR module.
# This should be called with the .cc src file and it will generate a
# src-file-ir target that can be built.
# e.g. COMPILE_TO_IR(test.cc) generates the "test-ir" make target.
set(IR_COMPILE_FLAGS "-emit-llvm" "-O3" "-c")
# set(IR_COMPILE_FLAGS "-S" "-emit-llvm" "-O0" "-c")
function(COMPILE_TO_IR SRC_FILE)
  get_filename_component(BASE_NAME ${SRC_FILE} NAME_WE)
  set(OUTPUT_FILE "build/${BASE_NAME}-clang.ll")
  add_custom_command(
    OUTPUT ${OUTPUT_FILE}
    # COMMAND ${CLANG_EXECUTABLE} ${IR_COMPILE_FLAGS} ${SRC_FILE} -o ${OUTPUT_FILE}
    COMMAND /usr/local/Cellar/llvm/3.3/bin/clang++ ${IR_COMPILE_FLAGS} ${SRC_FILE} -o ${OUTPUT_FILE}
    DEPENDS ${SRC_FILE})
  add_custom_target(${BASE_NAME}-ir ALL DEPENDS ${OUTPUT_FILE})
endfunction(COMPILE_TO_IR)

# Build the UDA/UDFs into a shared library.
add_library(garbage SHARED test-udf.cc)

# Custom targest to cross compile UDA/UDF to ir
if (CLANG_EXECUTABLE)
  COMPILE_TO_IR(test-udf.cc )
endif(CLANG_EXECUTABLE)
