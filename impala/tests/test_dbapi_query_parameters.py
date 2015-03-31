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
#
# Additional tests specific for query parameters
#

from __future__ import absolute_import
import sys

if sys.version_info[:2] <= (2, 6):
    import unittest2 as unittest
else:
    import unittest

import pytest

from impala.dbapi.interface import _bind_parameters, ProgrammingError


@pytest.mark.dbapi_query_parameters
class ImpalaDBAPIQueryParameters(unittest.TestCase):

    def dt(self, expected, query, params):
        result = _bind_parameters(query, params)
        self.assertEquals(expected, result)

    def test_pyformat(self):
        # technically these tests shouldn't need the full sql query
        # syntax, but it makes it easier to show how the formats are
        # used
        self.dt("select * from test where int = 1",
                "select * from test where int = %(int)s",
                {'int': 1})
        self.dt("select * from test where str = 'foo'",
                "select * from test where str = %(str)s",
                {'str': "foo"})
        self.dt("select * from test where flt = 0.123",
                "select * from test where flt = %(flt)s",
                {'flt': 0.123})
        self.dt("select * from test where nul = NULL",
                "select * from test where nul = %(nul)s",
                {'nul': None})
        self.dt("select * from test where int = 1 and str = 'foo' and " +
                "flt = 0.123 and nul = NULL",
                "select * from test where int = %(int)s and str = " +
                "%(str)s and flt = %(flt)s and nul = %(nul)s",
                {'int': 1, 'str': "foo", 'flt': 0.123, 'nul': None})
        # Make sure parameters are not replaced twice
        self.dt("select * from test where a=':b' and b=':c' and c=':a'",
                "select * from test where a=%(a)s and b=%(b)s and c=%(c)s",
                {'a': ":b", 'b': ":c", 'c': ":a"})

        # Unused parameters should be fine
        self.dt("select * from test where a=1",
                "select * from test where a=1",
                {'unused': 3})

        # But nonexistent should not
        with self.assertRaises(KeyError):
            self.dt("select * from test where int = 1",
                    "select * from test where int = %(nosuchkeyword)s",
                    {'wrong': 1})

    def test_named(self):
        self.dt("select * from test where int = 1",
                "select * from test where int = :int",
                {'int': 1})
        self.dt("select * from test where str = 'foo'",
                "select * from test where str = :str",
                {'str': "foo"})
        self.dt("select * from test where flt = 0.123",
                "select * from test where flt = :flt",
                {'flt': 0.123})
        self.dt("select * from test where nul = NULL",
                "select * from test where nul = :nul",
                {'nul': None})
        self.dt("select * from test where int = 1 and str = 'foo' and " +
                "flt = 0.123 and nul = NULL",
                "select * from test where int = :int and str = " +
                ":str and flt = :flt and nul = :nul",
                {'int': 1, 'str': "foo", 'flt': 0.123, 'nul': None})
        # Characters around keywords
        self.dt("select * from test where int=(1) and str='foo' and " +
                "flt=0.123 and nul=NULL",
                "select * from test where int=(:int) and str=" +
                ":str and flt=:flt and nul=:nul",
                {'int': 1, 'str': "foo", 'flt': 0.123, 'nul': None})

        # Partially overlapping names
        self.dt("select * from test where a=1 and b=2 and c=3",
                "select * from test where a=:f and b=:fo and c=:foo",
                {'f': 1, 'fo': 2, 'foo': 3})
        self.dt("select * from test where a=1 and b=2 and c=3",
                "select * from test where a=:foo and b=:fo and c=:f",
                {'foo': 1, 'fo': 2, 'f': 3})

        # Make sure parameters are not replaced twice
        self.dt("select * from test where a=':b' and b=':c' and c=':a'",
                "select * from test where a=:a and b=:b and c=:c",
                {'a': ":b", 'b': ":c", 'c': ":a"})

        with self.assertRaises(KeyError):
            self.dt("select * from test where int = 1",
                    "select * from test where int = :nosuchkeyword",
                    {'wrong': 1})
        
    def test_numeric(self):
        self.dt("select * from test where int = 1",
                "select * from test where int = :1",
                [1])
        self.dt("select * from test where str = 'foo'",
                "select * from test where str = :1",
                ["foo"])
        self.dt("select * from test where flt = 0.123",
                "select * from test where flt = :1",
                [0.123])
        self.dt("select * from test where nul = NULL",
                "select * from test where nul = :1",
                [None])
        self.dt("select * from test where int = 1 and str = 'foo' and " +
                "flt = 0.123 and nul = NULL",
                "select * from test where int = :1 and str = " +
                ":2 and flt = :3 and nul = :4",
                [1, "foo", 0.123, None])
        # reverse list
        self.dt("select * from test where int = 1 and str = 'foo' and " +
                "flt = 0.123 and nul = NULL",
                "select * from test where int = :4 and str = " +
                ":3 and flt = :2 and nul = :1",
                [None, 0.123, "foo", 1])
        # characters around them
        self.dt("select * from test where int=1 and str='foo' and " +
                "flt=(0.123) and nul=NULL",
                "select * from test where int=:1 and str=" +
                ":2 and flt=(:3) and nul=:4",
                [1, "foo", 0.123, None])
        # tuple instead of list
        self.dt("select * from test where int = 1 and str = 'foo' and " +
                "flt = 0.123 and nul = NULL",
                "select * from test where int = :1 and str = " +
                ":2 and flt = :3 and nul = :4",
                (1, "foo", 0.123, None))

        # more than 9
        self.dt("select * from test where a=1 and b=2 and c=3 and d=4 "+
                "and e=5 and f=6 and g=7 and h=8 and i=9 and j=10",
                "select * from test where a=:1 and b=:2 and c=:3 and d=:4 "+
                "and e=:5 and f=:6 and g=:7 and h=:8 and i=:9 and j=:10",
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.dt("select * from test where a='a' and b='b' and c='c' "+
                "and d='d' and e='e' and f='f' and g='g' and h='h' "+
                "and i='i' and j='j' and k='k'",
                "select * from test where a=:1 and b=:2 and c=:3 and "+
                "d=:4 and e=:5 and f=:6 and g=:7 and h=:8 and i=:9 and "+
                "j=:10 and k=:11",
                ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'])
        
    def test_qmark(self):
        self.dt("select * from test where int = 1",
                "select * from test where int = ?",
                [1])
        self.dt("select * from test where str = 'foo'",
                "select * from test where str = ?",
                ["foo"])
        self.dt("select * from test where flt = 0.123",
                "select * from test where flt = ?",
                [0.123])
        self.dt("select * from test where nul = NULL",
                "select * from test where nul = ?",
                [None])
        self.dt("select * from test where int = 1 and str = 'foo' and " +
                "flt = 0.123 and nul = NULL",
                "select * from test where int = ? and str = " +
                "? and flt = ? and nul = ?",
                [1, "foo", 0.123, None])
        # no spaces around =
        # characters around them
        self.dt("select * from test where int=1 and str='foo' and " +
                "flt=(0.123) and nul=NULL",
                "select * from test where int=? and str=" +
                "? and flt=(?) and nul=?",
                [1, "foo", 0.123, None])
        # tuple instead of list
        self.dt("select * from test where int=1 and str='foo' and " +
                "flt=0.123 and nul=NULL",
                "select * from test where int=? and str=" +
                "? and flt=? and nul=?",
                (1, "foo", 0.123, None))
                
        # bad number of bindings
        for q in [
            ("select * from test where int = ?", []),
            ("select * from test where int = ? or int = ?", [1]),
            ("select * from test where int = ?", [1, 2]),
            ("select * from test where int = ? or int = ? or int = ?",
             [1, 2, 3, 4]),
        ]:
            with self.assertRaises(ProgrammingError):
                self.dt("should have raised exception", q[0], q[1])

    def test_bad_argument_type(self):
        self.assertRaises(ProgrammingError, _bind_parameters,
                          "select * from test", 1)
        self.assertRaises(ProgrammingError, _bind_parameters,
                          "select * from test", "a")
        
