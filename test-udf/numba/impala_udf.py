"""
A simple demonstration of Impala UDF generation.
"""

from numba.ext.impala import udf, IntVal, FunctionContext

@udf(IntVal(FunctionContext, IntVal, IntVal))
def AddUdf(context, arg1, arg2):
    if arg1.is_null or arg2.is_null:
	return IntVal.null
    return IntVal(arg1.val + arg2.val)

# Simply print the module IR
# print(add_udf.llvm_module)

with open('build/test-udf-numba.ll', 'wb') as op:
    op.write(AddUdf.llvm_module.to_bitcode())
