# Copyright 2015 Cloudera Inc.
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

import os
import sys
import six

from impala._thrift_api import *

if six.PY2:
    from thrift.Thrift import TApplicationException

    # import beeswax codegen objects
    from impala._thrift_gen.beeswax import BeeswaxService
    from impala._thrift_gen.ImpalaService import ImpalaService
    from impala._thrift_gen.Status.ttypes import TStatus, TStatusCode
    from impala._thrift_gen.ExecStats.ttypes import TExecStats
    from impala._thrift_gen.beeswax.BeeswaxService import QueryState
    ThriftClient = ImpalaService.Client


if six.PY3:
    from thriftpy.thrift import TApplicationException

    # dynamically load the beeswax modules
    Status = load(os.path.join(thrift_dir, 'Status.thrift'),
                  include_dirs=[thrift_dir])
    beeswax = load(os.path.join(thrift_dir, 'beeswax.thrift'),
                   include_dirs=[thrift_dir])
    sys.modules[Status.__name__] = Status
    sys.modules[beeswax.__name__] = beeswax

    # import the beeswax objects
    from Status import TStatus, TStatusCode
    from ImpalaService import ImpalaService
    from beeswax import QueryState
    import beeswax as BeeswaxService
