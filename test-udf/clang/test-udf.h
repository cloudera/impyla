#ifndef LASERSON_TEST_UDF_H
#define LASERSON_TEST_UDF_H

#include <impala_udf/udf.h>

using namespace impala_udf;

// IntVal AddUdf(FunctionContext* context, const IntVal& arg1, const IntVal& arg2);
// IntVal Add1729(FunctionContext* context, const IntVal& arg1);
// StringVal GetFirst(FunctionContext* context, const StringVal& arg1);
// BigIntVal Subtract(FunctionContext* context, const IntVal& arg1, const TinyIntVal& arg2);

// FloatVal AddUdf(FunctionContext* context, const FloatVal& arg1, const FloatVal& arg2);
// DoubleVal AddUdf(FunctionContext* context, const DoubleVal& arg1, const DoubleVal& arg2);

// Generate pass through functions to investigate the type lowering
// BooleanVal PassThroughBooleanVal(FunctionContext* context, const BooleanVal& arg);
// TinyIntVal PassThroughTinyIntVal(FunctionContext* context, const TinyIntVal& arg);
// SmallIntVal PassThroughSmallIntVal(FunctionContext* context, const SmallIntVal& arg);
// IntVal PassThroughIntVal(FunctionContext* context, const IntVal& arg);
// BigIntVal PassThroughBigIntVal(FunctionContext* context, const BigIntVal& arg);
// FloatVal PassThroughFloatVal(FunctionContext* context, const FloatVal& arg);
// DoubleVal PassThroughDoubleVal(FunctionContext* context, const DoubleVal& arg);
// TimestampVal PassThroughTimestampVal(FunctionContext* context, const TimestampVal& arg);
// StringVal PassThroughStringVal(FunctionContext* context, const StringVal& arg);

// BooleanVal StringEq1(FunctionContext* context, const StringVal& arg1, const StringVal& arg2);
// BooleanVal StringEq2(FunctionContext* context, const StringVal& arg1, const StringVal& arg2);
bool StringEq(FunctionContext* context, const StringVal& arg1, const StringVal& arg2);
// uint8_t GetThird(FunctionContext* context, const StringVal& arg1, const IntVal& arg2);

#endif
