#! /usr/bin/env python

import os
import sys
from getpass import getuser
from subprocess import call

import llvm.core

from impala.dbapi import connect

# get some variables and set up some shell commands
# depends on the directory structure being right
user = getuser()
host = "bottou01-10g.pa.cloudera.com"
frontend = sys.argv[1]
if frontend not in ['clang', 'numba']:
    raise ValueError("Must supply one of 'clang' or 'numba'")
impyla_home = os.environ['IMPYLA_HOME']
local_path_to_ir = "%s/test-udf/%s/build/test-udf-%s.ll" % (impyla_home, frontend, frontend)
hdfs_path_to_ir = "/user/%s/test-udf/test-udf-%s.ll" % (user, frontend)
cmd_transfer_to_bottou = "scp %s %s@%s:~/test-udf" % (local_path_to_ir, user, host)
cmd_clean_hdfs = 'ssh %s@%s hadoop fs -rm test-udf/test-udf-%s.ll' % (user, host, frontend)
cmd_copy_to_hdfs = 'ssh %s@%s hadoop fs -put "~/test-udf/test-udf-%s.ll" test-udf' % (user, host, frontend)
# udf_name = 'AddUdf'
# udf_name = 'PassThroughFloatVal'
udf_name = 'PassThroughStringVal'

# get the symbol for the function of interest
with open(local_path_to_ir, 'rb') as ip:
    bc = llvm.core.Module.from_bitcode(ip)
    n1 = map(lambda f: f.name, bc.functions)
    n2 = filter(lambda name: udf_name in name, n1)
    if len(n2) != 1:
	raise ValueError("There should be exactly one %s fn; found %i" % (udf_name, len(n2)))
    name = n2[0]

call(cmd_transfer_to_bottou, shell=True)
call(cmd_clean_hdfs, shell=True)
call(cmd_copy_to_hdfs, shell=True)

conn = connect(host=host, port=21050)
cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS %s" % user)
cursor.execute("USE %s" % user)
cursor.execute("SHOW FUNCTIONS")
# if any([('%s_add' % frontend) in r[0] for r in cursor.fetchall()]):
#     cursor.execute("DROP FUNCTION %s_add(INT, INT)" % frontend)
# cursor.execute("CREATE FUNCTION %s_add(INT, INT) RETURNS INT LOCATION '%s' SYMBOL='%s'" % (frontend, hdfs_path_to_ir, name))

# if any([('%s_add' % frontend) in r[0] for r in cursor.fetchall()]):
#     cursor.execute("DROP FUNCTION %s_add(FLOAT, FLOAT)" % frontend)
# cursor.execute("CREATE FUNCTION %s_add(FLOAT, FLOAT) RETURNS FLOAT LOCATION '%s' SYMBOL='%s'" % (frontend, hdfs_path_to_ir, name))

# if any([('%s_add' % frontend) in r[0] for r in cursor.fetchall()]):
#     cursor.execute("DROP FUNCTION %s_add(DOUBLE, DOUBLE)" % frontend)
# cursor.execute("CREATE FUNCTION %s_add(DOUBLE, DOUBLE) RETURNS DOUBLE LOCATION '%s' SYMBOL='%s'" % (frontend, hdfs_path_to_ir, name))

# if any([('%s_add' % frontend) in r[0] for r in cursor.fetchall()]):
#     cursor.execute("DROP FUNCTION %s_add(BIGINT, BIGINT)" % frontend)
# cursor.execute("CREATE FUNCTION %s_add(BIGINT, BIGINT) RETURNS BIGINT LOCATION '%s' SYMBOL='%s'" % (frontend, hdfs_path_to_ir, name))


# if any([('%s_PassThroughFloatVal' % frontend) in r[0] for r in cursor.fetchall()]):
#     cursor.execute("DROP FUNCTION %s_PassThroughFloatVal(FLOAT)" % frontend)
# cursor.execute("CREATE FUNCTION %s_PassThroughFloatVal(FLOAT) RETURNS FLOAT LOCATION '%s' SYMBOL='%s'" % (frontend, hdfs_path_to_ir, name))

if any([('%s_PassThroughStringVal' % frontend) in r[0] for r in cursor.fetchall()]):
    cursor.execute("DROP FUNCTION %s_PassThroughStringVal(STRING)" % frontend)
cursor.execute("CREATE FUNCTION %s_PassThroughStringVal(STRING) RETURNS STRING LOCATION '%s' SYMBOL='%s'" % (frontend, hdfs_path_to_ir, name))
