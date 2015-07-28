#!/usr/bin/env python
# Copyright (c) 2012 Cloudera, Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Thrift utility functions

from impala._thrift_api import (TSocket, TBufferedTransport)

import getpass
import sasl

def get_socket(host, port, use_ssl, ca_cert):
    # based on the Impala shell impl
    if use_ssl:
        from thrift.transport.TSSLSocket import TSSLSocket
        if ca_cert is None:
            return TSSLSocket(host, port, validate=False)
        else:
            return TSSLSocket(host, port, validate=True, ca_certs=ca_cert)
    else:
        return TSocket(host, port)


def get_transport(socket, host, kerberos_service_name, auth_mechanism='NOSASL',
                  user=None, password=None):
    '''Creates a new Thrift Transport using the specified auth_mechanism.
    Supported auth_mechanisms are:
    - None or 'NOSASL' - returns simple buffered transport (default)
    - 'PLAIN'  - returns a SASL transport with the PLAIN mechanism
    - 'GSSAPI' - returns a SASL transport with the GSSAPI mechanism
    '''
    if auth_mechanism == 'NOSASL':
        return TBufferedTransport(socket)

    # Set defaults for PLAIN SASL / LDAP connections.
    if auth_mechanism in ['LDAP', 'PLAIN']:
        if user is None:
            user = getpass.getuser()
        if password is None:
            if auth_mechanism == 'LDAP':
                password = ''
            else:
                # PLAIN always requires a password for HS2.
                password = 'password'

    # Initializes a sasl client
    import sasl
    from impala.thrift_sasl import TSaslClientTransport
    def sasl_factory():
        sasl_client = sasl.Client()
        sasl_client.setAttr('host', host)
        sasl_client.setAttr('service', kerberos_service_name)
        if auth_mechanism.upper() in ['PLAIN', 'LDAP']:
            sasl_client.setAttr('username', user)
            sasl_client.setAttr('password', password)
        sasl_client.init()
        return sasl_client
    return TSaslClientTransport(sasl_factory, auth_mechanism, socket)
