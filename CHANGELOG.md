Changelog
=========

0.15a1
------
* **Improvements**
  - Selectively install thriftpy2 requirement based on python version (#342)
  - Add thrift query profile support (#333)
  - Add lastrowid to HiveServer2Cursor (#308)
  - Enable SQLAlchemy cursor configuration (#298)
  - Coerce floats if possible (#291)
  - Add SQLalchemy support storing table as Kudu (#259) (#260)
  - Add support for NULL_TYPE result column (#257)
  - Add support for optional krb_host parameter in connection (#248)
  - Various documentation improvements

* **Bug Fixes**
  - Fix unexpected SQLAlchemy keyword argument 'username' (#343)
  - Fix unicode issue in README file (#341)
  - Fix for a socket leak in HiveServer2Cursor (#327)
  - Avoid using reserved async keyword to support Python 3.7 (#322)
  - Bump required thrift version to 0.9.3 or above (#303)
  - Fix SQLalchemy connection string parsing and LDAP auth (#261)
