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

from pytest import raises

from impala.interface import _bind_parameters
from impala.dbapi import ProgrammingError


def dt(expected, query, params, **kwargs):
    result = _bind_parameters(query, params, **kwargs)
    assert expected == result


def test_pyformat():
    # technically these tests shouldn't need the full sql query
    # syntax, but it makes it easier to show how the formats are
    # used
    dt("select * from test where int = 1",
       "select * from test where int = %(int)s",
       {'int': 1})
    dt("select * from test where str = 'foo'",
       "select * from test where str = %(str)s",
       {'str': "foo"})
    dt("select * from test where flt = 0.123",
       "select * from test where flt = %(flt)s",
       {'flt': 0.123})
    dt("select * from test where nul = NULL",
       "select * from test where nul = %(nul)s",
       {'nul': None})
    dt("select * from test where int = 1 and str = 'foo' and " +
       "flt = 0.123 and nul = NULL",
       "select * from test where int = %(int)s and str = " +
       "%(str)s and flt = %(flt)s and nul = %(nul)s",
       {'int': 1, 'str': "foo", 'flt': 0.123, 'nul': None})
    # Make sure parameters are not replaced twice
    dt("select * from test where a=':b' and b=':c' and c=':a'",
       "select * from test where a=%(a)s and b=%(b)s and c=%(c)s",
       {'a': ":b", 'b': ":c", 'c': ":a"})
    # Unused parameters should be fine
    dt("select * from test where a=1",
       "select * from test where a=1",
       {'unused': 3})
    # But nonexistent should not
    with raises(KeyError):
        dt("select * from test where int = 1",
           "select * from test where int = %(nosuchkeyword)s",
           {'wrong': 1})


def test_named():
    dt("select * from test where int = 1",
       "select * from test where int = :int",
       {'int': 1})
    dt("select * from test where str = 'foo'",
       "select * from test where str = :str",
       {'str': "foo"})
    dt("select * from test where flt = 0.123",
       "select * from test where flt = :flt",
       {'flt': 0.123})
    dt("select * from test where nul = NULL",
       "select * from test where nul = :nul",
       {'nul': None})
    dt("select * from test where int = 1 and str = 'foo' and " +
       "flt = 0.123 and nul = NULL",
       "select * from test where int = :int and str = " +
       ":str and flt = :flt and nul = :nul",
       {'int': 1, 'str': "foo", 'flt': 0.123, 'nul': None})
    # Characters around keywords
    dt("select * from test where int=(1) and str='foo' and " +
       "flt=0.123 and nul=NULL",
       "select * from test where int=(:int) and str=" +
       ":str and flt=:flt and nul=:nul",
       {'int': 1, 'str': "foo", 'flt': 0.123, 'nul': None})
    # Partially overlapping names
    dt("select * from test where a=1 and b=2 and c=3",
       "select * from test where a=:f and b=:fo and c=:foo",
       {'f': 1, 'fo': 2, 'foo': 3})
    dt("select * from test where a=1 and b=2 and c=3",
       "select * from test where a=:foo and b=:fo and c=:f",
       {'foo': 1, 'fo': 2, 'f': 3})
    # Make sure parameters are not replaced twice
    dt("select * from test where a=':b' and b=':c' and c=':a'",
       "select * from test where a=:a and b=:b and c=:c",
       {'a': ":b", 'b': ":c", 'c': ":a"})
    with raises(KeyError):
        dt("select * from test where int = 1",
           "select * from test where int = :nosuchkeyword",
           {'wrong': 1})


def test_numeric():
    dt("select * from test where int = 1",
       "select * from test where int = :1",
       [1])
    dt("select * from test where str = 'foo'",
       "select * from test where str = :1",
       ["foo"])
    dt("select * from test where flt = 0.123",
       "select * from test where flt = :1",
       [0.123])
    dt("select * from test where nul = NULL",
       "select * from test where nul = :1",
       [None])
    dt("select * from test where int = 1 and str = 'foo' and " +
       "flt = 0.123 and nul = NULL",
       "select * from test where int = :1 and str = " +
       ":2 and flt = :3 and nul = :4",
       [1, "foo", 0.123, None])
    # reverse list
    dt("select * from test where int = 1 and str = 'foo' and " +
       "flt = 0.123 and nul = NULL",
       "select * from test where int = :4 and str = " +
       ":3 and flt = :2 and nul = :1",
       [None, 0.123, "foo", 1])
    # characters around them
    dt("select * from test where int=1 and str='foo' and " +
       "flt=(0.123) and nul=NULL",
       "select * from test where int=:1 and str=" +
       ":2 and flt=(:3) and nul=:4",
       [1, "foo", 0.123, None])
    # tuple instead of list
    dt("select * from test where int = 1 and str = 'foo' and " +
       "flt = 0.123 and nul = NULL",
       "select * from test where int = :1 and str = " +
       ":2 and flt = :3 and nul = :4",
       (1, "foo", 0.123, None))
    # more than 9
    dt("select * from test where a=1 and b=2 and c=3 and d=4 " +
       "and e=5 and f=6 and g=7 and h=8 and i=9 and j=10",
       "select * from test where a=:1 and b=:2 and c=:3 and d=:4 " +
       "and e=:5 and f=:6 and g=:7 and h=:8 and i=:9 and j=:10",
       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    dt("select * from test where a='a' and b='b' and c='c' " +
       "and d='d' and e='e' and f='f' and g='g' and h='h' " +
       "and i='i' and j='j' and k='k'",
       "select * from test where a=:1 and b=:2 and c=:3 and " +
       "d=:4 and e=:5 and f=:6 and g=:7 and h=:8 and i=:9 and " +
       "j=:10 and k=:11",
       ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'])


def test_qmark():
    dt("select * from test where int = 1",
       "select * from test where int = ?",
       [1])
    dt("select * from test where str = 'foo'",
       "select * from test where str = ?",
       ["foo"])
    dt("select * from test where flt = 0.123",
       "select * from test where flt = ?",
       [0.123])
    dt("select * from test where nul = NULL",
       "select * from test where nul = ?",
       [None])
    dt("select * from test where int = 1 and str = 'foo' and " +
       "flt = 0.123 and nul = NULL",
       "select * from test where int = ? and str = " +
       "? and flt = ? and nul = ?",
       [1, "foo", 0.123, None])
    # no spaces around =
    # characters around them
    dt("select * from test where int=1 and str='foo' and " +
       "flt=(0.123) and nul=NULL",
       "select * from test where int=? and str=" +
       "? and flt=(?) and nul=?",
       [1, "foo", 0.123, None])
    # tuple instead of list
    dt("select * from test where int=1 and str='foo' and " +
       "flt=0.123 and nul=NULL",
       "select * from test where int=? and str=" +
       "? and flt=? and nul=?",
       (1, "foo", 0.123, None))
    # bad number of bindings
    bad_bindings = [
        ("select * from test where int = ?", []),
        ("select * from test where int = ? or int = ?", [1]),
        ("select * from test where int = ?", [1, 2]),
        ("select * from test where int = ? or int = ? or int = ?",
         [1, 2, 3, 4])]
    for q in bad_bindings:
        with raises(ProgrammingError):
            dt("should have raised exception", q[0], q[1])


def test_format():
    dt("select * from test where int = 1",
       "select * from test where int = %s",
       [1])
    dt("select * from test where str = 'foo'",
       "select * from test where str = %s",
       ["foo"])
    dt("select * from test where flt = 0.123",
       "select * from test where flt = %s",
       [0.123])
    dt("select * from test where nul = NULL",
       "select * from test where nul = %s",
       [None])
    dt("select * from test where int = 1 and str = 'foo' and " +
       "flt = 0.123 and nul = NULL",
       "select * from test where int = %s and str = " +
       "%s and flt = %s and nul = %s",
       [1, "foo", 0.123, None])
    # no spaces around =
    # characters around them
    dt("select * from test where int=1 and str='foo' and " +
       "flt=(0.123) and nul=NULL",
       "select * from test where int=%s and str=" +
       "%s and flt=(%s) and nul=%s",
       [1, "foo", 0.123, None])
    # tuple instead of list
    dt("select * from test where int=1 and str='foo' and " +
       "flt=0.123 and nul=NULL",
       "select * from test where int=%s and str=" +
       "%s and flt=%s and nul=%s",
       (1, "foo", 0.123, None))
    # bad number of bindings
    bad_bindings = [
        ("select * from test where int = %s", []),
        ("select * from test where int = %s or int = %s", [1]),
        ("select * from test where int = %s", [1, 2]),
        ("select * from test where int = %s or int = %s or int = %s",
         [1, 2, 3, 4])]
    for q in bad_bindings:
        with raises(ProgrammingError):
            dt("should have raised exception", q[0], q[1])

def test_avoid_substitution():
  """Regression tests for cases where a parameter *should not* be substituted."""
  # Only markers matching the specified paramstyle should be replaced, including
  # if the parameter is embedded in a substituted string.
  dt("select :2, ?, :named from test where a='string' and b='42'",
     "select :2, ?, :named from test where a=%s and b=%s",
     ['string', '42'], paramstyle='format')
  dt("select * from test where a='string :2 ? %s :named' and b='42'",
     "select * from test where a=%s and b=%s",
     ['string :2 ? %s :named', '42'], paramstyle='format')

  dt("select :2, %s, :named from test where a='string' and b='42'",
     "select :2, %s, :named from test where a=? and b=?",
     ['string', '42'], paramstyle='qmark')
  dt("select * from test where a='string :2 ? %s :named' and b='42'",
     "select * from test where a=? and b=?",
     ['string :2 ? %s :named', '42'], paramstyle='qmark')

  dt("select ?, %s, :named from test where a='string' and b='42'",
     "select ?, %s, :named from test where a=:1 and b=:2",
     ['string', '42'], paramstyle='numeric')
  dt("select * from test where a='string :2 ? %s :named' and b='42'",
      "select * from test where a=:1 and b=:2",
     ['string :2 ? %s :named', '42'], paramstyle='numeric')

  # BUG: %s picks up named parameters as stringified dict when dict is passed.
  dt('select ?, {\'x\': "\'string\'"}, :1 from test where a=\'string\'',
     "select ?, %s, :1 from test where a=:x",
     {'x': 'string'}, paramstyle='named')
  dt("select * from test where a='string :2 ? %s :named' and b='42'",
      "select * from test where a=:x and b=:y",
      {'x': 'string :2 ? %s :named', 'y':'42'}, paramstyle='named')

  # BUG: if a parameter is substituted with a string containing another parameter
  # specifier, double substitution can occur.
  dt("select * from test where a='string '42'' and b='42'",
     "select * from test where a=%s and b=%s",
     ['string :2', '42'])

def test_date_type():
    import datetime
    today = datetime.date(2016, 5, 7)
    query = 'select %(today)s'
    dt("select '2016-05-07'", query, {'today': today})

    today = datetime.datetime(2016, 5, 7, 12, 0)
    query = 'select %(today)s'
    dt("select '2016-05-07 12:00:00'", query, {'today': today})


def test_bad_argument_type():
    with raises(ProgrammingError):
        _bind_parameters("select * from test", 1)
    with raises(ProgrammingError):
        _bind_parameters("select * from test", "a")

def test_marker_replacement():
    dt("select * from test where x = '%s'",
       "select * from test where x = %s",
       [r'%s'])
