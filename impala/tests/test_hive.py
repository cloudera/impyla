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


def test_hive_queries(cur):
    cur.execute('CREATE TABLE tmp_hive (a STRING, b INT, c DOUBLE)')

    cur.execute('SHOW TABLES')
    tables = cur.fetchall()
    assert any([t[0] == 'tmp_hive' for t in tables])

    cur.execute("INSERT INTO tmp_hive "
                "VALUES ('foo', 1, 0.5), ('bar', 2, NULL), ('baz', 3, 6.2)")

    cur.execute('SELECT b FROM tmp_hive LIMIT 2')
    assert len(cur.description) == 1
    assert cur.description[0][0] == 'b'
    results = cur.fetchall()
    assert len(results) == 2

    cur.execute('SELECT * FROM tmp_hive WHERE c IS NOT NULL')
    results = cur.fetchall()
    assert len(results) == 2

    cur.execute("SELECT c from tmp_hive WHERE a = 'foo'")
    results = cur.fetchall()
    assert len(results) == 1
    assert results[0][0] == 0.5

    cur.execute("SELECT c from tmp_hive WHERE a = 'bar'")
    results = cur.fetchall()
    assert len(results) == 1
    assert results[0][0] is None

    # Test executemany() with parameter substitution. The %s should be ignored
    # as paramstyle is "qmark".
    cur.executemany("INSERT INTO tmp_hive VALUES (?, ?, ?)",
                    [['a', 4, 1.0], ['%s', 5, None]],
                    {'paramstyle': 'qmark'})

    cur.execute("SELECT * from tmp_hive WHERE b = 4")
    results = cur.fetchall()
    assert results == [('a', 4, 1.0)]

    cur.execute("SELECT * from tmp_hive WHERE b = 5")
    results = cur.fetchall()
    assert results == [('%s', 5, None)]

    cur.execute('DROP TABLE tmp_hive')

    cur.execute('SHOW TABLES')
    tables = cur.fetchall()
    assert all([t[0] != 'tmp_hive' for t in tables])
