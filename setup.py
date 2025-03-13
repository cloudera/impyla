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

import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as ip:
        return ip.read()

setup(
    name='impyla',
    # impala/__init__.py also contains the version - the two should have the same value!
    version='v0.21.0',
    description='Python client for the Impala distributed query engine',
    long_description_content_type='text/markdown',
    long_description=readme(),
    maintainer='Wes McKinney',
    maintainer_email='wes.mckinney@twosigma.com',
    author='Uri Laserson',
    author_email='laserson@cloudera.com',
    url='https://github.com/cloudera/impyla',
    packages=find_packages(),
    install_package_data=True,
    package_data={'impala.thrift': ['*.thrift']},
    install_requires=['six', 'bitarray<3', 'thrift==0.16.0', 'thrift_sasl==0.4.3'],
    extras_require={
        "kerberos": ['kerberos>=1.3.0'],
    },
    keywords=('cloudera impala python hadoop sql hdfs mpp spark pydata '
              'pandas distributed db api pep 249 hive hiveserver2 hs2'),
    license='Apache License, Version 2.0',
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
    entry_points={
        'sqlalchemy.dialects': ['impala = impala.sqlalchemy:ImpalaDialect',
                                'impala4 = impala.sqlalchemy:Impala4Dialect']
    },
    zip_safe=False)
