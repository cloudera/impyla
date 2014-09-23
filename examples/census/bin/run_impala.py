import sys
sys.path.append('/Users/laserson/repos/impyla/examples/census/models')
from time import time

from impala.dbapi import connect
from impala.udf import ship_udf, udf, FunctionContext, StringVal, IntVal

from model_0 import predict_income as predict_income_0
from model_100 import predict_income as predict_income_100
from model_500 import predict_income as predict_income_500
from model_1000 import predict_income as predict_income_1000
from model_1500 import predict_income as predict_income_1500
from model_2000 import predict_income as predict_income_2000

sizes = [0, 100, 500, 1000, 1500, 2000]

udfs = {0: predict_income_0,
	100: predict_income_100,
	500: predict_income_500,
	1000: predict_income_1000,
	1500: predict_income_1500,
	2000: predict_income_2000}

conn = connect(host='bottou01-10g.pa.cloudera.com', port=21050)
cursor = conn.cursor()
cursor.execute('USE laserson')

signature = StringVal(FunctionContext, IntVal, StringVal, IntVal, StringVal,
	IntVal, StringVal, StringVal, StringVal, StringVal, StringVal, IntVal,
	StringVal, StringVal)

create_table_query = """
    CREATE EXTERNAL TABLE IF NOT EXISTS census_text (age INT, workclass STRING,
	    final_weight INT, education STRING, education_num INT,
	    marital_status STRING, occupation STRING, relationship STRING,
	    race STRING, sex STRING, hours_per_week INT, native_country STRING,
	    income STRING)
    ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
    STORED AS TEXTFILE
    LOCATION '/user/laserson/bigml/census_text'
"""

score_obs_query = """
    SELECT DISTINCT predict_income(age, workclass, final_weight, education,
	    education_num, marital_status, occupation, relationship, race, sex,
	    hours_per_week, native_country, income) FROM census_text
"""

cursor.execute(create_table_query)

for size in sizes:
    start_compile = time()
    predict_income = udf(signature)(udfs[size])
    end_compile = time()

    ship_udf(cursor, predict_income, '/user/laserson/test-udf/census_%i.ll' % size, 'bottou01-10g.pa.cloudera.com', user='laserson', overwrite=True)

    start_score = time()
    cursor.execute(score_obs_query)
    distinct = cursor.fetchall()
    end_score = time()

    print "impala,%i,%i,%.2f,%.2f" % (size, len(udfs[size].func_code.co_code), end_score - start_score, end_compile - start_compile)
