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

# This package is here to clean up references to thrift, because we're using
# thriftpy for Py3 at the moment.  This should all be temporary, as Apache
# Thrift gains Py3 compatibility.

import os
import sys
import six


if six.PY2:
    # import Apache Thrift code
    from thrift.transport.TSocket import TSocket
    from thrift.transport.TTransport import (
        TBufferedTransport, TTransportException)
    from thrift.protocol.TBinaryProtocol import (
        TBinaryProtocolAccelerated as TBinaryProtocol)


if six.PY3:
    # import thriftpy code
    from thriftpy import load
    from thriftpy.thrift import TClient
    # TODO: reenable cython
    # from thriftpy.protocol import TBinaryProtocol
    from thriftpy.protocol.binary import TBinaryProtocol
    from thriftpy.transport import TSocket, TTransportException
    # TODO: reenable cython
    # from thriftpy.transport import TBufferedTransport
    from thriftpy.transport.buffered import TBufferedTransport

    # dynamically load modules
    thrift_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                              'thrift')
    ExecStats = load(os.path.join(thrift_dir, 'ExecStats.thrift'),
                     include_dirs=[thrift_dir])
    ImpalaService = load(os.path.join(thrift_dir, 'ImpalaService.thrift'),
                         include_dirs=[thrift_dir])
    sys.modules[ExecStats.__name__] = ExecStats
    sys.modules[ImpalaService.__name__] = ImpalaService

    # import objects
    from ExecStats import TExecStats
    ThriftClient = TClient
