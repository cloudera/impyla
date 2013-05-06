from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as ip:
    return ip.read()

setup(
  name='impyla',
  version='0.7',
  description='Python client for Cloudera Impala',
  long_description=readme(),
  author='Uri Laserson',
  author_email='laserson@cloudera.com',
  url='https://github.com/laserson/impyla',
  package_dir={'': 'lib'},
  packages=find_packages('lib'),
  keywords='cloudera impala python hadoop sql hdfs mpp',
  install_requires=[
    'distribute',
    'thrift>=0.9'
  ],
  license='Apache License, Version 2.0'
)
