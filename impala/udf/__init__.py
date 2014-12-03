# Copyright 2014 Cloudera Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Module for compiling Python functions into Impala UDFs"""

from __future__ import absolute_import

import os
import pkgutil

import llvm.core as lc
from numba import sigutils
from numba.compiler import compile_extra, Flags

from impala.udf.target import ImpalaTargetContext
from impala.udf.typing import impala_typing_context
from impala.udf.types import (BooleanVal, TinyIntVal, SmallIntVal, IntVal,
                              BigIntVal, FloatVal, DoubleVal, StringVal)


# functionality to compile Python UDFs into Impala-executable IR

def udf(signature):
    def wrapper(pyfunc):
        udfobj = UDF(pyfunc, signature)
        return udfobj

    return wrapper


class UDF(object):

    def __init__(self, pyfunc, signature):
        self.py_func = pyfunc
        self.signature = signature
        self.name = pyfunc.__name__

        # recreate for each UDF, as linking is destructive to the
        # precompiled module
        impala_typing = impala_typing_context()
        impala_targets = ImpalaTargetContext(impala_typing)

        args, return_type = sigutils.normalize_signature(signature)
        flags = Flags()
        flags.set('no_compile')
        self._cres = compile_extra(typingctx=impala_typing,
                                   targetctx=impala_targets, func=pyfunc,
                                   args=args, return_type=return_type,
                                   flags=flags, locals={})
        llvm_func = impala_targets.finalize(self._cres.llvm_func, return_type,
                                            args)
        self.llvm_func = llvm_func
        # numba_module = llvm_func.module
        self.llvm_module = llvm_func.module
        # link in the precompiled module
        # bc it's destructive, load a fresh version
        precompiled = lc.Module.from_bitcode(
            pkgutil.get_data("impala.udf", "precompiled/impyla.bc"))
        self.llvm_module.link_in(precompiled)


# functionality to ship code to Impala cluster

# convert *Val name to Impala data type name
udf_to_impala_type = {'BooleanVal': 'BOOLEAN',
                      'TinyIntVal': 'TINYINT',
                      'SmallIntVal': 'SMALLINT',
                      'IntVal': 'INT',
                      'BigIntVal': 'BIGINT',
                      'FloatVal': 'FLOAT',
                      'DoubleVal': 'DOUBLE',
                      'StringVal': 'STRING',
                      'TimestampVal': 'TIMESTAMP'}

try:
    from pywebhdfs.webhdfs import PyWebHdfsClient

    def ship_udf(ic, function, hdfs_path=None, udf_name=None, database=None,
                 overwrite=False):
        # extract some information from the function
        if udf_name is None:
            udf_name = function.name
        symbol = function.llvm_func.name
        ir = function.llvm_module.to_bitcode()
        return_type = udf_to_impala_type[function.signature.return_type.name]
        arg_types = [udf_to_impala_type[arg.name]
                     for arg in function.signature.args[1:]]

        # ship the IR to the cluster
        hdfs_client = PyWebHdfsClient(host=ic._nn_host, port=ic._webhdfs_port,
                                      user_name=ic._hdfs_user)
        if hdfs_path is None:
            hdfs_path = os.path.join(ic._temp_dir, udf_name + '.ll')
        if not hdfs_path.endswith('.ll'):
            raise ValueError("The HDFS file name must end with .ll")
        hdfs_client.create_file(hdfs_path.lstrip('/'), ir, overwrite=overwrite)

        # register the function in Impala
        if database is None:
            database = ic._temp_db
        impala_name = '%s.%s(%s)' % (database, udf_name, ', '.join(arg_types))
        if overwrite:
            ic._cursor.execute("DROP FUNCTION IF EXISTS %s" % impala_name)
        register_query = "CREATE FUNCTION %s RETURNS %s LOCATION '%s' " \
                         "SYMBOL='%s'" % (
                             impala_name,
                             return_type, hdfs_path, symbol)
        ic._cursor.execute(register_query)

except ImportError:
    print "Failed to import pywebhdfs; you must ship your Python UDFs " \
          "manually."
