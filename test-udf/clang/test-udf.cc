#include "test-udf.h"
#include <cstring>

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

// BooleanVal PassThroughBooleanVal(FunctionContext* context, const BooleanVal& arg) {
//     if (arg.is_null) return BooleanVal::null();
//     return BooleanVal(arg.val);
// }

// TinyIntVal PassThroughTinyIntVal(FunctionContext* context, const TinyIntVal& arg) {
//     if (arg.is_null) return TinyIntVal::null();
//     return TinyIntVal(arg.val);
// }

// SmallIntVal PassThroughSmallIntVal(FunctionContext* context, const SmallIntVal& arg) {
//     if (arg.is_null) return SmallIntVal::null();
//     return SmallIntVal(arg.val);
// }

// IntVal PassThroughIntVal(FunctionContext* context, const IntVal& arg) {
//     if (arg.is_null) return IntVal::null();
//     return IntVal(arg.val);
// }

// BigIntVal PassThroughBigIntVal(FunctionContext* context, const BigIntVal& arg) {
//     if (arg.is_null) return BigIntVal::null();
//     return BigIntVal(arg.val);
// }

// FloatVal PassThroughFloatVal(FunctionContext* context, const FloatVal& arg) {
//     if (arg.is_null) return FloatVal::null();
//     return FloatVal(arg.val);
// }

// DoubleVal PassThroughDoubleVal(FunctionContext* context, const DoubleVal& arg) {
//     if (arg.is_null) return DoubleVal::null();
//     return DoubleVal(arg.val);
// }

// TimestampVal PassThroughTimestampVal(FunctionContext* context, const TimestampVal& arg) {
//     if (arg.is_null) return TimestampVal::null();
//     return TimestampVal(arg.date, arg.time_of_day);
// }

// StringVal PassThroughStringVal(FunctionContext* context, const StringVal& arg) {
//     if (arg.is_null) return StringVal::null();
//     return StringVal(arg.ptr, arg.len);
// }


// BooleanVal StringEq1(FunctionContext* context, const StringVal& arg1, const StringVal& arg2) {
//     if (arg1.is_null || arg2.is_null) return BooleanVal::null();
//     if (arg1.len != arg2.len) return BooleanVal(false);
//     for (int i = 0; i < arg1.len; i++) {
//         if (arg1.ptr[i] != arg2.ptr[i]) return BooleanVal(false);
//     }
//     return BooleanVal(true);
// }

// BooleanVal StringEq2(FunctionContext* context, const StringVal& arg1, const StringVal& arg2) {
//     if (arg1 == arg2) {
//         return true;
//     } else {
//         return false;
//     }
// }

bool StringEq(FunctionContext* context,
	      const StringVal& arg1,
	      const StringVal& arg2) {
    if (arg1.is_null != arg2.is_null)
	return false;
    if (arg1.is_null)
	return true;
    if (arg1.len != arg2.len)
	return false;
    return (arg1.ptr == arg2.ptr) ||
	    memcmp(arg1.ptr, arg2.ptr, arg1.len) == 0;
}


// bool StringEq3(FunctionContext* context,
//               const StringVal& arg1,
//               const StringVal& arg2) {
//     return memcmp(arg1.ptr, arg2.ptr, arg1.len) == 0;
// }


// uint8_t GetThird(FunctionContext* context, const StringVal& arg1, const IntVal& arg2) {
//     return arg1.ptr[arg2.val];
// }


// bool StringTest(FunctionContext* context, const StringVal& arg1) {
//     // const char* foo = "bar";
//     StringVal foo("bar");
//     // if (arg1.len != strlen(foo)) return false;
//     if (arg1.len != foo.len) return false;
//     // return memcmp(arg1.ptr, foo, arg1.len);
//     return memcmp(arg1.ptr, foo.ptr, arg1.len);
// }

// int test_size_t(const char* arg) {
    // int a = strlen(arg);
    // return a;
// }