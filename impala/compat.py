# Copyright 2015 Cloudera Inc.
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

# pylint: disable=unused-import,wrong-import-position

from __future__ import absolute_import

import six

if six.PY3:
    def lzip(*x):
        return list(zip(*x))

    from decimal import Decimal
elif six.PY2:
    lzip = zip

    try:
        from cdecimal import Decimal
    except ImportError:
        from decimal import Decimal  # noqa

try:
  _xrange = xrange
except NameError:
  _xrange = range  # python3 compatibilty
