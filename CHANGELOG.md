Changelog
=========

0.17a6
------
* **Improvements**
  - Unify Python 2 and 3 thrift handling and remove thriftpy2

0.17a5
------
* **Improvements**
  - Add buffering to hs2-http (#442)
  - Remove references to 'sasl', always use 'pure-sasl' package

0.17a4
------
* **Improvements**
  - Switch to using manylinux2010 docker build environment
  - Upgrade to thrift-sasl 0.4.3a2

0.17a3
------
* **Bug Fixes**
  - Add no_utf8strings to thrift compiler option (#440)

0.17a2
------
* **Improvements**
  - Implement simple retry which throws the underlying HttpError if retrying fails
  - Ugprade Thift to 0.11.0 for Python 2
  - Add build script

* **Bug Fixes**
  - Server certs should not be verified if SSL is enabled and ca_cert is not specified
  - Added "fetchType" to TFetchResultsReq.
  - Fix Thrift compilation with current Impala

0.17a1
------
* **Improvements**
  - Implement GSSAPI authentication over http transport. (#415)
  - Vendor thrift classes with Python 3 #277 (#404)
  - Add HTTP code handling to THttpClient (#380)
  - Disable failing tests - #401 (#402)

* **Bug Fixes**
  - Fix #418, no 'message', just cast to string (#419)
  - Fix DATE, VARCHAR handling: #410 (#411)

0.16.3
------
* **Bug Fixes**
  - Fix specifying dependency on thrift package

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
