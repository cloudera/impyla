#!/bin/bash
# Copyright 2026 Cloudera Inc.
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

# Run all tests by restarting Impala cluster with different authentication flags.
# TODO: move this to tox or something like CustomClusterTest in Impala?

set -eu

TOX_ENV_ARGS=""
if [[ -n "${1:-}" ]]; then
    TOX_ENV_ARGS="-e $1"
fi

if [[ -z "$IMPALA_HOME" ]]; then
    echo "Must provide IMPALA_HOME in environment" 1>&2
    exit 1
fi
if [[ -z "$IMPYLA_HOME" ]]; then
    echo "Must provide IMPYLA_HOME in environment" 1>&2
    exit 1
fi

. "$IMPALA_HOME/bin/impala-config.sh"
. "$IMPALA_HOME/bin/set-pythonpath.sh"

unset IMPYLA_TEST_AUTH_MECH
unset IMPYLA_SSL_CERT
unset IMPYLA_SSL_WRONG_CERT


# Run tests without SSL and authentication.
$IMPALA_HOME/bin/start-impala-cluster.py
unset IMPYLA_REPORT_PREFIX
set +e
python3 -m tox $TOX_ENV_ARGS
ret=$?
set -e

# Run tests with SSL enabled.
export IMPALA_SSL_CERT_DIR=$IMPALA_HOME/be/src/testutil
export IMPYLA_SSL_CERT=$IMPALA_SSL_CERT_DIR/server-cert.pem
export IMPALA_SSL_ARGS="--ssl_client_ca_certificate=$IMPYLA_SSL_CERT --ssl_server_certificate=$IMPYLA_SSL_CERT --ssl_private_key=$IMPALA_SSL_CERT_DIR/server-key.pem --hostname=localhost"
export IMPYLA_SSL_WRONG_CERT=$IMPALA_SSL_CERT_DIR/incorrect-commonname-cert.pem
$IMPALA_HOME/bin/start-impala-cluster.py --impalad_args="$IMPALA_SSL_ARGS" --catalogd_args="$IMPALA_SSL_ARGS" --state_store_args="$IMPALA_SSL_ARGS"
export IMPYLA_REPORT_PREFIX="ssl-"
set +e
python3 -m tox $TOX_ENV_ARGS -- -m ssl
ret=$(( ret != 0 ? ret : $? ))
set -e


unset IMPYLA_SSL_CERT
unset IMPYLA_SSL_WRONG_CERT

export IMPYLA_TEST_AUTH_MECH=JWT
$IMPALA_HOME/bin/start-impala-cluster.py --impalad_args="--jwt_token_auth=true --jwt_validate_signature=false --jwt_allow_without_tls=true"
export IMPYLA_REPORT_PREFIX="jwt-"
set +e
python3 -m tox $TOX_ENV_ARGS -- -m jwt_auth
ret=$(( ret != 0 ? ret : $? ))
set -e

exit $ret


