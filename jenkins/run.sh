# Install all the necessary prerequisites
cd /tmp
virtualenv impyla-it-pyenv-$BUILD_NUMBER
source impyla-it-pyenv-$BUILD_NUMBER/bin/activate
pip install pytest
pip install thrift
pip install unittest2
pip install numpy
pip install pandas
pip install llvmpy
pip install numba
pip install pywebhdfs

# Build impyla
cd $WORKSPACE ; make ; python setup.py install

# Run testing suite
cd /tmp; py.test --dbapi-compliance $WORKSPACE/impala/tests
deactivate
