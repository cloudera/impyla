#ifndef LASERSON_TEST_UDF_H
#define LASERSON_TEST_UDF_H

#include <impala_udf/udf.h>

using namespace impala_udf;

IntVal AddUdf(FunctionContext* context, const IntVal& arg1, const IntVal& arg2);
// IntVal Add1729(FunctionContext* context, const IntVal& arg1);
// StringVal GetFirst(FunctionContext* context, const StringVal& arg1);
// BigIntVal Subtract(FunctionContext* context, const IntVal& arg1, const TinyIntVal& arg2);

#endif
