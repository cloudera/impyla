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

"""Module for compiling Python functions into Impala UDFs"""

from __future__ import absolute_import

import llvm.core as lc
from numba import sigutils
from numba.compiler import compile_extra, Flags

from .target import ImpalaTargetContext
from .typing import impala_typing_context
from .types import (FunctionContext, BooleanVal, TinyIntVal, SmallIntVal,
                    IntVal, BigIntVal, FloatVal, DoubleVal, StringVal)



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
        numba_module = llvm_func.module
        self.llvm_module = lc.Module.new(self.name)
        self.llvm_module.link_in(numba_module)
        self.llvm_module.link_in(impala_targets.precompiled_module)


# functionality to ship code to Impala cluster

# convert *Val name to Impala data type name
udf2impala_type = {'BooleanVal': 'BOOLEAN',
                   'TinyIntVal': 'TINYINT',
                   'SmallIntVal': 'SMALLINT',
                   'IntVal': 'INT',
                   'BigIntVal': 'BIGINT',
                   'FloatVal': 'FLOAT',
                   'DoubleVal': 'DOUBLE',
                   'StringVal': 'STRING',
                   'TimestampVal': 'TIMESTAMP'}

# TODO: in the future, consider taking an "ImpalaContext" if there is some info I
# want to store.  But this could also all be in the cursor object potentially
try:
    from pywebhdfs.webhdfs import PyWebHdfsClient

    def ship_udf(cursor, function, hdfs_path, host, webhdfs_port=50070, user=None,
            udf_name=None, overwrite=False):
        # extract some information from the function
        if udf_name is None:
            udf_name = function.name
        symbol = function.llvm_func.name
        ir = function.llvm_module.to_bitcode()
        return_type = udf2impala_type[function.signature.return_type.name]
        arg_types = [udf2impala_type[arg.name] for arg in function.signature.args[1:]]

        # ship the IR to the cluster
        hdfs_client = PyWebHdfsClient(host=host, port=webhdfs_port, user_name=user)
        if not hdfs_path.endswith('.ll'):
            raise ValueError("The HDFS file name must end with .ll")
        hdfs_client.create_file(hdfs_path.lstrip('/'), ir, overwrite=overwrite)

        # register the function in Impala
        impala_name = '%s(%s)' % (udf_name, ', '.join(arg_types))
        if overwrite:
            cursor.execute("SHOW FUNCTIONS")
            registered_functions = [fn[0].lower() for fn in cursor.fetchall()]
            if impala_name.lower() in registered_functions:
                cursor.execute("DROP FUNCTION %s" % impala_name)
        register_query = "CREATE FUNCTION %s RETURNS %s LOCATION '%s' SYMBOL='%s'" % (impala_name,
                return_type, hdfs_path, symbol)
        cursor.execute(register_query)

except ImportError:
    print "Failed to import pywebhdfs; you must ship your Python UDFs manually."
