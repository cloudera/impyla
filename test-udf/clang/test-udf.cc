#include "test-udf.h"

IntVal AddUdf(FunctionContext* context, const IntVal& arg1, const IntVal& arg2) {
  if (arg1.is_null || arg2.is_null) return IntVal::null();
  return IntVal(arg1.val + arg2.val);
}

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
