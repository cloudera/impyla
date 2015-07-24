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


if six.PY2:
    # import HS2 codegen objects
    from impala._thrift_gen.TCLIService.ttypes import (
        TOpenSessionReq, TFetchResultsReq, TCloseSessionReq,
        TExecuteStatementReq, TGetInfoReq, TGetInfoType, TTypeId,
        TFetchOrientation, TGetResultSetMetadataReq, TStatusCode,
        TGetColumnsReq, TGetSchemasReq, TGetTablesReq, TGetFunctionsReq,
        TGetOperationStatusReq, TOperationState, TCancelOperationReq,
        TCloseOperationReq, TGetLogReq, TProtocolVersion)
    from impala._thrift_gen.ImpalaService.ImpalaHiveServer2Service import (
        TGetRuntimeProfileReq, TGetExecSummaryReq)
    from impala._thrift_gen.ImpalaService import ImpalaHiveServer2Service
    from impala._thrift_gen.ExecStats.ttypes import TExecStats
    ThriftClient = ImpalaHiveServer2Service.Client


if six.PY3:
    # import thriftpy code
    from thriftpy import load
    from thriftpy.thrift import TClient

    # dynamically load the HS2 modules
    from impala._thrift_api import thrift_dir
    ExecStats = load(os.path.join(thrift_dir, 'ExecStats.thrift'),
                     include_dirs=[thrift_dir])
    TCLIService = load(os.path.join(thrift_dir, 'TCLIService.thrift'),
                       include_dirs=[thrift_dir])
    ImpalaService = load(os.path.join(thrift_dir, 'ImpalaService.thrift'),
                         include_dirs=[thrift_dir])
    sys.modules[ExecStats.__name__] = ExecStats
    sys.modules[TCLIService.__name__] = TCLIService
    sys.modules[ImpalaService.__name__] = ImpalaService

    # import the HS2 objects
    from TCLIService import (
        TOpenSessionReq, TFetchResultsReq, TCloseSessionReq,
        TExecuteStatementReq, TGetInfoReq, TGetInfoType, TTypeId,
        TFetchOrientation, TGetResultSetMetadataReq, TStatusCode,
        TGetColumnsReq, TGetSchemasReq, TGetTablesReq, TGetFunctionsReq,
        TGetOperationStatusReq, TOperationState, TCancelOperationReq,
        TCloseOperationReq, TGetLogReq, TProtocolVersion)
    from ImpalaService import (
        TGetRuntimeProfileReq, TGetExecSummaryReq, ImpalaHiveServer2Service)
    from ExecStats import TExecStats
    ThriftClient = TClient
