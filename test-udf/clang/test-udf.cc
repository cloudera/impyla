#include "test-udf.h"

// IntVal AddUdf(FunctionContext* context, const IntVal& arg1, const IntVal& arg2) {
//   if (arg1.is_null || arg2.is_null) return IntVal::null();
//   return IntVal(arg1.val + arg2.val);
// }

// FloatVal AddUdf(FunctionContext* context, const FloatVal& arg1, const FloatVal& arg2) {
//   if (arg1.is_null || arg2.is_null) return FloatVal::null();
//   return FloatVal(arg1.val + arg2.val);
// }

// DoubleVal AddUdf(FunctionContext* context, const DoubleVal& arg1, const DoubleVal& arg2) {
//   if (arg1.is_null || arg2.is_null) return DoubleVal::null();
//   return DoubleVal(arg1.val + arg2.val);
// }

// IntVal Add1729(FunctionContext* context, const IntVal& arg) {
//   if (arg.is_null) return IntVal::null();
//   return IntVal(arg.val + 1729);
// }

// StringVal GetFirst(FunctionContext* context, const StringVal& arg1) {
//     if (arg1.is_null) return StringVal::null();
//     if (arg1.len == 0) return StringVal("");
//     return StringVal(arg1.ptr, 1);
// }

// BigIntVal Subtract(FunctionContext* context, const IntVal& arg1, const TinyIntVal& arg2) {
//     if (arg1.is_null || arg2.is_null) return BigIntVal::null();
//     return BigIntVal(arg1.val - arg2.val);
// }


// Pass through functions for investigating the type lowering

BooleanVal PassThroughBooleanVal(FunctionContext* context, const BooleanVal& arg) {
    if (arg.is_null) return BooleanVal::null();
    return BooleanVal(arg.val);
}

TinyIntVal PassThroughTinyIntVal(FunctionContext* context, const TinyIntVal& arg) {
    if (arg.is_null) return TinyIntVal::null();
    return TinyIntVal(arg.val);
}

SmallIntVal PassThroughSmallIntVal(FunctionContext* context, const SmallIntVal& arg) {
    if (arg.is_null) return SmallIntVal::null();
    return SmallIntVal(arg.val);
}

IntVal PassThroughIntVal(FunctionContext* context, const IntVal& arg) {
    if (arg.is_null) return IntVal::null();
    return IntVal(arg.val);
}

BigIntVal PassThroughBigIntVal(FunctionContext* context, const BigIntVal& arg) {
    if (arg.is_null) return BigIntVal::null();
    return BigIntVal(arg.val);
}

FloatVal PassThroughFloatVal(FunctionContext* context, const FloatVal& arg) {
    if (arg.is_null) return FloatVal::null();
    return FloatVal(arg.val);
}

DoubleVal PassThroughDoubleVal(FunctionContext* context, const DoubleVal& arg) {
    if (arg.is_null) return DoubleVal::null();
    return DoubleVal(arg.val);
}

TimestampVal PassThroughTimestampVal(FunctionContext* context, const TimestampVal& arg) {
    if (arg.is_null) return TimestampVal::null();
    return TimestampVal(arg.date, arg.time_of_day);
}

StringVal PassThroughStringVal(FunctionContext* context, const StringVal& arg) {
    if (arg.is_null) return StringVal::null();
    return StringVal(arg.ptr, arg.len);
}
