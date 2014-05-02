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
parser.add_argument('-i', '--input', required=True) # input python model
parser.add_argument('-o', '--output', required=True) # output python model
args = parser.parse_args()

string_re = r"'(.*)'"

# load the raw model
with open(args.input, 'r') as ip:
    old_model = ip.readlines()

# -----------------------------------------------------------------------------
# replace strings with their hash
new_model = []
for line in old_model:
    new_line = re.sub(string_re, lambda m: str(hash(m.group(1))), line)
    new_model.append(new_line)

# -----------------------------------------------------------------------------
# write out new model
new_model = ''.join(new_model)
with open(args.output, 'w') as op:
    print >>op, new_model
