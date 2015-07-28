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
    # dynamically load the HS2 modules
    TCLIService = load(os.path.join(thrift_dir, 'TCLIService.thrift'),
                       include_dirs=[thrift_dir])
    sys.modules[TCLIService.__name__] = TCLIService

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
