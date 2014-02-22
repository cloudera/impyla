"""
A simple demonstration of Impala UDF generation.
"""

from llvm.core import Module
from numba.ext.impala import udf, BooleanVal, TinyIntVal, SmallIntVal, IntVal, BigIntVal, FloatVal, DoubleVal, StringVal, FunctionContext

# @udf(IntVal(FunctionContext, IntVal, IntVal))
# def AddUdf(context, arg1, arg2):
#     if arg1.is_null or arg2.is_null:
#         return IntVal.null
#     return IntVal(arg1.val + arg2.val)

@udf(IntVal(FunctionContext, IntVal, IntVal))
def AddUdf(context, arg1, arg2):
    if arg1.is_null or arg2.is_null:
	return IntVal.null
    x = "hello"
    return IntVal(arg1.val + len(x))

# @udf(FloatVal(FunctionContext, FloatVal, FloatVal))
# def AddUdf(context, arg1, arg2):
#     if arg1.is_null or arg2.is_null:
#         return FloatVal.null
#     return FloatVal(arg1.val + arg2.val)

# @udf(BigIntVal(FunctionContext, BigIntVal, BigIntVal))
# def AddUdf(context, arg1, arg2):
#     if arg1.is_null or arg2.is_null:
#         return BigIntVal.null
#     return BigIntVal(arg1.val + arg2.val)


# @udf(StringVal(FunctionContext, StringVal))
# def AddUdf(context, arg1, arg2):
#     if arg1.is_null or arg2.is_null:
#         return BigIntVal.null
#     return BigIntVal(arg1.val + arg2.val)


# Passthrough functions for investigating type lowering

# @udf(IntVal(FunctionContext, IntVal))
# def PassThroughIntVal(context, arg):
#     if arg.is_null:
#         return IntVal.null
#     return IntVal(arg.val)

# @udf(FloatVal(FunctionContext, FloatVal))
# def PassThroughFloatVal(context, arg):
#     if arg.is_null:
#         return FloatVal.null
#     return FloatVal(arg.val)

# @udf(StringVal(FunctionContext, StringVal))
# def PassThroughStringVal(context, arg):
#     if arg.is_null:
#         return StringVal.null
#     return StringVal(arg.ptr, arg.len)

# DEBUG
# def PassThroughStringVal(context, arg):
#     if arg.is_null:
#         return StringVal.null
#     return StringVal(arg.ptr, arg.len)
# import ipdb
# ipdb.run("PassThroughStringVal = udf(StringVal(FunctionContext, StringVal))(PassThroughStringVal)", globals(), locals())
# b /usr/local/lib/python2.7/site-packages/numba/lowering.py:143, "$16.4" in str(inst)
# b /usr/local/lib/python2.7/site-packages/numba/lowering.py:160, "$16.4" in str(inst)
# b /usr/local/lib/python2.7/site-packages/numba/lowering.py:311, "call $16.1($16.2, $16.3, )" in str(expr)
# b /usr/local/lib/python2.7/site-packages/numba/ext/impala.py:765


# Simply print the module IR
# print(add_udf.llvm_module)

# module_obj = Module.new('test-udf-numba')
# module_obj.add_function ... TODO: need to finish

with open('build/test-udf-numba.ll', 'wb') as op:
    op.write(AddUdf.llvm_module.to_bitcode())
    # op.write(PassThroughIntVal.llvm_module.to_bitcode())
    # op.write(PassThroughFloatVal.llvm_module.to_bitcode())
    # op.write(PassThroughStringVal.llvm_module.to_bitcode())
