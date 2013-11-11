from distutils.core import setup

def readme():
  with open('README.md', 'r') as ip:
    return ip.read()

setup(
  name='impyla',
  version='1.1',
  description='Python client for Cloudera Impala',
  long_description=readme(),
  author='Uri Laserson',
  author_email='laserson@cloudera.com',
  url='https://github.com/laserson/impyla',
  package_dir={'': 'lib'},
  packages=[
    'impala',
    'cli_service',
    'ImpalaService'
  ],
  keywords='cloudera impala python hadoop sql hdfs mpp',
  install_requires=['thrift>=0.9'],
  license='Apache License, Version 2.0'
)
