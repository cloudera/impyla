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

from __future__ import absolute_import

import sys

import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as ip:
        return ip.read()


PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

# Apache Thrift does not yet support Python 3 (see THRIFT-1857).  We use
# thriftpy as a stopgap replacement
reqs = ['six', 'bitarray']
if PY2:
    packages = find_packages()
    reqs.append('thrift<=0.9.3')
elif PY3:
    packages = find_packages(exclude=['impala._thrift_gen',
                                      'impala._thrift_gen.*'])
    reqs.append('thriftpy>=0.3.5')
    reqs.append('thrift_sasl==0.2.1')


import versioneer  # noqa


setup(
    name='impyla',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Python client for the Impala distributed query engine',
    long_description=readme(),
    maintainer='Wes McKinney',
    maintainer_email='wes.mckinney@twosigma.com',
    author='Uri Laserson',
    author_email='laserson@cloudera.com',
    url='https://github.com/cloudera/impyla',
    packages=packages,
    install_package_data=True,
    package_data={'impala.thrift': ['*.thrift']},
    install_requires=reqs,
    keywords=('cloudera impala python hadoop sql hdfs mpp spark pydata '
              'pandas distributed db api pep 249 hive hiveserver2 hs2'),
    license='Apache License, Version 2.0',
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
    entry_points={
        'sqlalchemy.dialects': ['impala = impala.sqlalchemy:ImpalaDialect']},
    zip_safe=False)
