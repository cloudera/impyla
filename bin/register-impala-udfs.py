#! /usr/bin/env python
# Copyright 2014 Cloudera Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import argparse

import llvm.core as lc
from pywebhdfs.webhdfs import PyWebHdfsClient

import impala.dbapi

def log(msg):
    sys.stderr.write("%s\n" % msg)
    sys.stderr.flush()

llvm2impala = {
    'struct.impala_udf::BooleanVal': 'BOOLEAN',
    'struct.impala_udf::TinyIntVal': 'TINYINT',
    'struct.impala_udf::SmallIntVal': 'SMALLINT',
    'struct.impala_udf::IntVal': 'INT',
    'struct.impala_udf::BigIntVal': 'BIGINT',
    'struct.impala_udf::FloatVal': 'FLOAT',
    'struct.impala_udf::DoubleVal': 'DOUBLE',
    'struct.impala_udf::StringVal': 'STRING',
    'struct.impala_udf::TimestampVal': 'TIMESTAMP'
}

parser = argparse.ArgumentParser(description="Register clang-compiled UDFs with Impala")
parser.add_argument('-i', '--llvm-path', required=True,
        help="Local path to LLVM module")
parser.add_argument('-o', '--hdfs-path', required=True,
        help="Path in HDFS to store LLVM module, including the final file name")
parser.add_argument('-n', '--name', required=True, action='append',
        help="Specify the name of the C++ UDF; must be matched with a --return-type")
parser.add_argument('-t', '--return-type', required=True, action='append',
        help="Specify a return type for the corresponding function; use Impala types, e.g., STRING or INT")
parser.add_argument('-j', '--impala-host', required=False, default='localhost',
        help="Impala daemon hostname")
parser.add_argument('-q', '--impala-port', required=False, default=21050,
        help="Port for Impala daemon")
parser.add_argument('-k', '--nn-host', required=False, default='localhost',
        help="Namenode hostname")
parser.add_argument('-p', '--webhdfs-port', required=False, default=50070,
        type=int, help="Port for WebHDFS interface")
parser.add_argument('-u', '--user', required=False,
        help="User name to connect to HDFS with")
parser.add_argument('-f', '--force', action='store_true',
        help="Overwrite LLVM on HDFS if it already exists")
parser.add_argument('-d', '--db', required=False,
        help="Specify which database to add the functions to")
args = parser.parse_args()

# do some input validation
if len(args.name) != len(args.return_type):
    raise ValueError("Must supply a return type or each specified fucntion name.")
if not args.hdfs_path.endswith('.ll'):
    raise ValueError("The HDFS file name must end with .ll")

# load the LLVM IR
with open(args.llvm_path, 'rb') as ip:
    bc = ip.read()
ll = lc.Module.from_bitcode(bc)
log("Loaded the LLVM IR file %s" % args.llvm_path)

# load symbols and types for each function in the LLVM  module
functions = []
for function in ll.functions:
    try:
        symbol = function.name
        log("Loading types for function %s" % symbol)
        # skip the first argument, which is FunctionContext*
        arg_types = tuple([llvm2impala[arg.pointee.name] for arg in function.type.pointee.args[1:]])
        functions.append((symbol, arg_types))
    except (AttributeError, KeyError):
        # this process could fail for non-UDF helper functions...just ignore them,
        # because we're not going to be registering them anyway
        log("Had trouble with function %s; moving on..." % symbol)
        pass

# transfer the LLVM module to HDFS
hdfs_client = PyWebHdfsClient(host=args.nn_host, port=args.webhdfs_port, user_name=args.user)
hdfs_client.create_file(args.hdfs_path.lstrip('/'), bc, overwrite=args.force)
log("Transferred LLVM IR to HDFS at %s" % args.hdfs_path)

# register the functions with impala
conn = impala.dbapi.connect(host=args.impala_host, port=args.impala_port)
cursor = conn.cursor(user=args.user)
log("Connected to impalad: %s" % args.impala_host)
if args.db:
    cursor.execute('USE %s' % args.db)
cursor.execute("SHOW FUNCTIONS")
registered_functions = cursor.fetchall()
for (udf_name, return_type) in zip(args.name, args.return_type):
    log("Registering function %s" % udf_name)
    # find matching LLVM symbols to the current UDF name
    matches = [pair for pair in functions if udf_name in pair[0]]
    if len(matches) == 0:
        log("Couldn't find a symbol matching %s; skipping..." % name)
        continue
    if len(matches) > 1:
        log("Found multiple symbols matching %s; skipping..." % name)
        continue
    (symbol, arg_types) = matches[0]
    impala_name = '%s(%s)' % (udf_name, ','.join(arg_types))
    if args.force and impala_name in registered_functions:
        log("Overwriting function %s" % impala_name)
        cursor.execute("DROP FUNCTION %s" % impala_name)
    register_query = "CREATE FUNCTION %s RETURNS %s LOCATION '%s' SYMBOL='%s'" % (impala_name,
            return_type, args.hdfs_path, symbol)
    log(register_query)
    cursor.execute(register_query)
    log("Successfully registered %s" % impala_name)
