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

"""Typing declarations for the Python string module"""

from __future__ import absolute_import

import string

from numba import types as ntypes
from numba.typing.templates import (AttributeTemplate, ConcreteTemplate,
                                    signature, Registry)

from .types import StringVal, IntVal


registry = Registry()
register_attribute = registry.register_attr
register_global = registry.register_global


@register_attribute
class StringModuleAttr(AttributeTemplate):
    key = ntypes.Module(string)

    def resolve_capitalize(self, mod):
        return ntypes.Function(String_capitalize)

    def resolve_split(self, mod):
        return ntypes.Function(String_split)


class String_capitalize(ConcreteTemplate):
    key = string.capitalize
    cases = [signature(StringVal, StringVal)]


class String_split(ConcreteTemplate):
    key = string.split
    cases = [signature(ntypes.Array(StringVal, 1, 'C'), StringVal),
             signature(ntypes.Array(StringVal, 1, 'C'), StringVal, StringVal),
             signature(ntypes.Array(StringVal, 1, 'C'), StringVal, StringVal, IntVal)]


register_global(string, ntypes.Module(string))
register_global(string.capitalize, ntypes.Function(String_capitalize))
register_global(string.split, ntypes.Function(String_split))
