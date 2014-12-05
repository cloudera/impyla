import sys

sys.path.append('/home/laserson/models')
from time import time

from model_0 import predict_income as predict_income_0
from model_100 import predict_income as predict_income_100
from model_500 import predict_income as predict_income_500
from model_1000 import predict_income as predict_income_1000
from model_1500 import predict_income as predict_income_1500
from model_2000 import predict_income as predict_income_2000

sc.addPyFile('/home/laserson/models/model_0.py')
sc.addPyFile('/home/laserson/models/model_100.py')
sc.addPyFile('/home/laserson/models/model_500.py')
sc.addPyFile('/home/laserson/models/model_1000.py')
sc.addPyFile('/home/laserson/models/model_1500.py')
sc.addPyFile('/home/laserson/models/model_2000.py')

sizes = [0, 100, 500, 1000, 1500, 2000]

udfs = {0: predict_income_0,
        100: predict_income_100,
        500: predict_income_500,
        1000: predict_income_1000,
        1500: predict_income_1500,
        2000: predict_income_2000}

ident = lambda x: x  # do nothing for strings
types = (int, ident, int, ident, int, ident, ident, ident, ident, ident, int,
         ident, ident)
num_fields = len(types)


def parse_obs(line):
    fields = line.split('\t')
    parsed = [types[i](fields[i]) for i in xrange(num_fields)]
    # the None is where the FunctionContext would go; for Impala compatibility
    return [None] + parsed


observations = sc.textFile('/user/laserson/bigml/census_text').map(parse_obs)

results = []
for size in sizes:
    predict_income = udfs[size]
    start_score = time()
    predictions = observations.map(lambda tup: predict_income(*tup))
    distinct = predictions.distinct().collect()
    end_score = time()
    results.append("spark,%i,%i,%.2f," % (
        size, len(udfs[size].func_code.co_code), end_score - start_score))

print '\n'.join(results)
