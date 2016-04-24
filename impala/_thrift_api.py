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

# pylint: disable=wrong-import-position

from __future__ import absolute_import

import os
import sys
import six
import getpass

from impala.util import get_logger_and_init_null


log = get_logger_and_init_null(__name__)


if six.PY2:
    # pylint: disable=import-error,unused-import
    # import Apache Thrift code
    from thrift.transport.TSocket import TSocket
    from thrift.transport.TTransport import (
        TBufferedTransport, TTransportException)
    from thrift.protocol.TBinaryProtocol import (
        TBinaryProtocolAccelerated as TBinaryProtocol)

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
    # TODO: reenable cython
    # from thriftpy.protocol import TBinaryProtocol
    from thriftpy.protocol.binary import TBinaryProtocol  # noqa
    from thriftpy.transport import TSocket, TTransportException  # noqa
    # TODO: reenable cython
    # from thriftpy.transport import TBufferedTransport
    from thriftpy.transport.buffered import TBufferedTransport  # noqa
    thrift_dir = os.path.join(os.path.dirname(__file__), 'thrift')

    # dynamically load the HS2 modules
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
    from TCLIService import (  # noqa
        TOpenSessionReq, TFetchResultsReq, TCloseSessionReq,
        TExecuteStatementReq, TGetInfoReq, TGetInfoType, TTypeId,
        TFetchOrientation, TGetResultSetMetadataReq, TStatusCode,
        TGetColumnsReq, TGetSchemasReq, TGetTablesReq, TGetFunctionsReq,
        TGetOperationStatusReq, TOperationState, TCancelOperationReq,
        TCloseOperationReq, TGetLogReq, TProtocolVersion)
    from ImpalaService import (  # noqa
        TGetRuntimeProfileReq, TGetExecSummaryReq, ImpalaHiveServer2Service)
    from ExecStats import TExecStats  # noqa
    ThriftClient = TClient


def get_socket(host, port, use_ssl, ca_cert):
    # based on the Impala shell impl
    log.debug('get_socket: host=%s port=%s use_ssl=%s ca_cert=%s',
              host, port, use_ssl, ca_cert)

    if use_ssl:
        if six.PY2:
            from thrift.transport.TSSLSocket import TSSLSocket
            if ca_cert is None:
                return TSSLSocket(host, port, validate=False)
            else:
                return TSSLSocket(host, port, validate=True, ca_certs=ca_cert)
        else:    
            from thriftpy.transport.sslsocket import TSSLSocket
            if ca_cert is None:
                return TSSLSocket(host, port, validate=False)
            else:
                return TSSLSocket(host, port, validate=True, cafile=ca_cert)
    else:
        return TSocket(host, port)


def get_transport(socket, host, kerberos_service_name, auth_mechanism='NOSASL',
                  user=None, password=None):
    """
    Creates a new Thrift Transport using the specified auth_mechanism.
    Supported auth_mechanisms are:
    - None or 'NOSASL' - returns simple buffered transport (default)
    - 'PLAIN'  - returns a SASL transport with the PLAIN mechanism
    - 'GSSAPI' - returns a SASL transport with the GSSAPI mechanism
    """
    log.debug('get_transport: socket=%s host=%s kerberos_service_name=%s '
              'auth_mechanism=%s user=%s password=fuggetaboutit', socket, host,
              kerberos_service_name, auth_mechanism, user)

    if auth_mechanism == 'NOSASL':
        return TBufferedTransport(socket)

    # Set defaults for PLAIN SASL / LDAP connections.
    if auth_mechanism in ['LDAP', 'PLAIN']:
        if user is None:
            user = getpass.getuser()
            log.debug('get_transport: user=%s', user)
        if password is None:
            if auth_mechanism == 'LDAP':
                password = ''
            else:
                # PLAIN always requires a password for HS2.
                password = 'password'
            log.debug('get_transport: password=%s', password)

    # Initializes a sasl client
    from thrift_sasl import TSaslClientTransport
    try:
        import sasl  # pylint: disable=import-error

        def sasl_factory():
            sasl_client = sasl.Client()
            sasl_client.setAttr('host', host)
            sasl_client.setAttr('service', kerberos_service_name)
            if auth_mechanism.upper() in ['PLAIN', 'LDAP']:
                sasl_client.setAttr('username', user)
                sasl_client.setAttr('password', password)
            sasl_client.init()
            return sasl_client
    except ImportError:
        log.warn("Unable to import 'sasl'. Fallback to 'puresasl'.")
        from impala.sasl_compat import PureSASLClient

        def sasl_factory():
            return PureSASLClient(host, username=user, password=password, service=kerberos_service_name)

    return TSaslClientTransport(sasl_factory, auth_mechanism, socket)
