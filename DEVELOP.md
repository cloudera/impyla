#### Thrift Codegen

1. Get the `.thrift` file from the Impala repo

    cp $IMPALA_REPO/common/thrift/cli_service.thrift $IMPYLA_REPO/thrift

2. Generate the Python client code (from the root dir)

    thrift -gen py:new_style -out $IMPYLA_REPO/impala $IMPYLA_REPO/thrift/cli_service.thrift

This should only need to be done very irregularly, as the generated code is
committed to the repo.  Only in cases where `cli_service.thrift` changes.
People checking out the repo to develop on it do NOT need to run the codegen.


#### Contribute

The code is currently being developed on GitHub: https://github.com/laserson/impyla

Fork the repo and send a pull request.  Contributions welcome!
