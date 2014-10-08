#include "udf.h"

using namespace impala_udf;

// taken from Impala's be/src/exprs/expr-ir.cc to force inclusion of all UDF
// types.  Using pointers to prevent lowering of types
void impyla_dummy(impala_udf::FunctionContext*,
                  impala_udf::BooleanVal*,
                  impala_udf::TinyIntVal*,
                  impala_udf::SmallIntVal*,
                  impala_udf::IntVal*,
                  impala_udf::BigIntVal*,
                  impala_udf::FloatVal*,
                  impala_udf::DoubleVal*,
                  impala_udf::StringVal*,
                  impala_udf::TimestampVal*,
                  impala_udf::DecimalVal*) { }
