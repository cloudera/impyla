#### Contribute

The code is currently being developed on GitHub: https://github.com/cloudera/impyla

Fork the repo and send a pull request against `master`.  Contributions welcome!


#### Thrift Codegen

1. Get the HiveServer 2 `.thrift` file from the Impala repo

    ```bash
    cp $IMPALA_REPO/common/thrift/cli_service.thrift $IMPYLA_REPO/thrift
    ```

2. Generate the Python client code (from the root dir)

    ```bash
    thrift -gen py:new_style -out $IMPYLA_REPO/impala $IMPYLA_REPO/thrift/cli_service.thrift
    ```

This should only need to be done very irregularly, as the generated code is
committed to the repo.  Only in cases where `cli_service.thrift` changes. People
checking out the repo to develop on it do NOT need to run the codegen.  Codegen
performed with Thrift 0.9.


#### Release

1. Generate a summary of all the commits since the last release

    ```bash
    git log $LAST_RELEASE_TAG..HEAD
    ```

2. Set the release version in `setup.py` (remove the `-dev` tag if applicable)
and commit the version number change

3. Tag version number and summarize changes in the tag message

    ```bash
    git tag -a vX.Y.Z
    ```

4. Push the tag upstream

    ```bash
    git push upstream vX.Y.Z
    ```
    
    or
    
    ```bash
    git push upstream --tags
    ```

5. Register the release with PyPI

    ```bash
    python setup.py register sdist bdist_egg upload
    ```

6. If working on master, bump up to the next anticipated version with a `-dev`
tag and commit


*Backporting*

1. Checkout the tag for the version to backport onto and create a new branch

    ```bash
    git checkout vX.Y.Z
    git checkout -b backport
    ```

2. Cherry pick the relevant commits onto the `backport` branch

3. Goto #1 for main release flow

4. Remove the `backport` branch
