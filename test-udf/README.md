Make sure to

    export IMPYLA_HOME=/Users/laserson/repos/impyla




scp numba.bc bottou01-10g.pa.cloudera.com:~/test-udf

hadoop fs -put ~/test-udf/numba.bc test-udf

use laserson;
create function numba_add(int, int) returns int location '/user/laserson/test-udf/numba.ll' symbol='numba_udf.__main__.add_udf.impala-function-context.IntVal.IntVal';
create function cpp_add(int, int) returns int location '/user/laserson/test-udf/test-udf.ll' symbol='_Z6AddUdfPN10impala_udf15FunctionContextERKNS_6IntValES4_';
select numba_add(3, 4);
