# Copyright 2013 Cloudera Inc.
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

import time
import string
import random

try:
    import pandas as pd
except ImportError:
    print "Failed to import pandas"

def to_pandas(cursor):
    names = [metadata[0] for metadata in cursor.description]
    return pd.DataFrame([dict(zip(names, row)) for row in cursor], columns=names)

def generate_random_table_name():
    date = time.localtime(time.time())
    date_string = "%04i%02i%02i%02i%02i%02i" % (date.tm_year, date.tm_mon,
            date.tm_mday, date.tm_hour, date.tm_min, date.tm_sec)
    random_string = ''.join(random.sample(string.ascii_lowercase, 8))
    name = "temp%s%s" % (date_string, random_string)
    return name

def compute_result_schema(cursor, query_string):
    temp_name = generate_random_table_name()
    cursor.execute("CREATE VIEW %s AS %s" % (temp_name, query_string))
    cursor.execute("SELECT * FROM %s LIMIT 0" % temp_name)
    schema = cursor.description
    cursor.execute("DROP VIEW %s" % temp_name)
    return schema
    