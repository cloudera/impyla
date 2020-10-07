Changelog
=========

0.16.3
------
* **Bug Fixes**
  - Fix thrift package requirement

0.16a3
------
* **Improvements**
  - Better documentation regarding SASL prerequisites (#394)

* **Bug Fixes**
  - Fix compatibility with Python 3.9 (#386)
  - Fix interoperability with Hive client version >= V10 (#396) (#397)
  - Fix documentation bug reL cursor iteration (#388)
  - Fix connecting over HTTP using Python 3 (#378)

0.16.2
------
* **Bug Fixes**
  - Fix an issue that prevented use of Impyla with Python 2.6 (#375)

0.16.1
------
* **Bug Fixes**
  - Fix an issue whereby impyla incorrectly assumes there's no more data to fetch (#369)

0.16.0
------
* **Improvements**
  - Add HTTP endpoint support (#359)
  - Add rowcounts property to cursor object to return the number of rows affected (#346)

* **Bug Fixes**
  - Set long_description_content_type to markdown in setup.py (#364)
  - Fix ImportError 'THttpClient' in python3+ (#363)
  - Enable executemany() to pass parameter configuration to inner execute() (#361)
  - Minor docstring corrections (#355)
  - Make thriftpy2 range locked, not specific-version locked (#353)
  - Fixed numeric parameter substitution bug (#348)
  - Add thrift_sasl as an official dependency (#273)

0.15.0
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
