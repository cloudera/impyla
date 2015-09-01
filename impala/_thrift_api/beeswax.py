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

# pylint: disable=unused-import

import os
import sys
import six


if six.PY2:
    # pylint: disable=import-error
    # import Apache Thrift code
    from thrift.Thrift import TApplicationException

    # import beeswax codegen objects
    from impala._thrift_gen.beeswax import BeeswaxService
    from impala._thrift_gen.ImpalaService import ImpalaService
    from impala._thrift_gen.Status.ttypes import TStatus, TStatusCode
    from impala._thrift_gen.ExecStats.ttypes import TExecStats
    from impala._thrift_gen.beeswax.BeeswaxService import QueryState
    ThriftClient = ImpalaService.Client


if six.PY3:
    # import thriftpy code
    from thriftpy import load
    from thriftpy.thrift import TClient, TApplicationException  # noqa

    # dynamically load the beeswax modules
    from impala._thrift_api import thrift_dir
    ExecStats = load(os.path.join(thrift_dir, 'ExecStats.thrift'),
                     include_dirs=[thrift_dir])
    Status = load(os.path.join(thrift_dir, 'Status.thrift'),
                  include_dirs=[thrift_dir])
    ImpalaService = load(os.path.join(thrift_dir, 'ImpalaService.thrift'),
                         include_dirs=[thrift_dir])
    beeswax = load(os.path.join(thrift_dir, 'beeswax.thrift'),
                   include_dirs=[thrift_dir])
    sys.modules[ExecStats.__name__] = ExecStats
    sys.modules[Status.__name__] = Status
    sys.modules[ImpalaService.__name__] = ImpalaService
    sys.modules[beeswax.__name__] = beeswax

    # import the beeswax objects
    from ExecStats import TExecStats  # noqa
    from Status import TStatus, TStatusCode  # noqa
    from ImpalaService import ImpalaService  # noqa
    from beeswax import QueryState  # noqa
    import beeswax as BeeswaxService  # noqa
    ThriftClient = TClient
