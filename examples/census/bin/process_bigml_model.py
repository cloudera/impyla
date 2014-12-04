#! /usr/bin/env python

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

import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', required=True)  # input python model
parser.add_argument('-o', '--output', required=True)  # output python model
# data csv with schema as first row
parser.add_argument('-d', '--data', required=True)
args = parser.parse_args()

signature_re = r"^def (.+)\(data={}\):"
is_none_re = r"not '(.*)' in data or data\['\1'\] is None"
dict_key_re = r"data\['(.*)'\]"
unicode_re = r"u'(.*)'"

# get the schema from the data file
with open(args.data, 'r') as ip:
    line = ip.next()
    schema = [token.strip().replace(' ', '_') for token in line.split(',')]

# load the raw model
with open(args.input, 'r') as ip:
    old_model = ip.readlines()


# -----------------------------------------------------------------------------
# collect all the keys from the model
keys = set()
for line in old_model:
    keys.update(re.findall(dict_key_re, line))

if set(schema) < keys:
    print "ids unique to keys: %s" % (keys - set(schema))
    raise ValueError("keys has ids not present in schema")


# -----------------------------------------------------------------------------
# replace fn signature with actual args and add a slot for the FunctionContext
new_model = []
arg_string = ', '.join(['impala_function_context'] + schema)
num_sigs = 0
for line in old_model:
    m = re.match(signature_re, line)
    if m:
        new_model.append('def %s(%s):\n' % (m.group(1), arg_string))
        num_sigs += 1
    else:
        new_model.append(line)

if num_sigs != 1:
    raise ValueError("Expected a single signature line; found %i" % num_sigs)

old_model = new_model


# -----------------------------------------------------------------------------
# change all unicode strings to regular ascii
new_model = []
for line in old_model:
    new_line = re.sub(unicode_re, r"'\1'", line)
    new_model.append(new_line)

old_model = new_model


# -----------------------------------------------------------------------------
# replace all the "is None" tests
new_model = []
for line in old_model:
    new_line = re.sub(is_none_re, r'\1 is None', line)
    new_model.append(new_line)

old_model = new_model


# -----------------------------------------------------------------------------
# replace references to data dict with actual args
new_model = []
for line in old_model:
    new_line = re.sub(dict_key_re, r'\1', line)
    new_model.append(new_line)


# -----------------------------------------------------------------------------
# write out new model
new_model = ''.join(new_model)
with open(args.output, 'w') as op:
    print >>op, new_model
