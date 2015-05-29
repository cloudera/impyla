#### Contribute

The code is currently being developed on GitHub: https://github.com/cloudera/impyla

Fork the repo and send a pull request against `master`.  Contributions welcome!


#### Thrift Codegen

0. To clean up

    ```bash
    rm -rf $IMPYLA_REPO/impala/_thrift_gen
    rm -rf $IMPYLA_REPO/impala/thrift/*.thrift
    ```

1. Execute `$IMPYLA_REPO/impala/thrift/process_thrift.sh`

This should only need to be done very irregularly, as the generated code is
committed to the repo.  Only when the original thrift IDL files change. People
checking out the repo to develop on it do NOT need to run the codegen.  Codegen
performed with Thrift 0.9.x.


#### UDF maintenance

Copy a fresh copy of the `udf.h` header file

    ```bash
    cp $IMPALA_REPO/be/src/udf/udf.h $IMPYLA_REPO/impala/udf/precompiled
    ```

#### Release

1. Generate a summary of all the commits since the last release

    ```bash
    git log $LAST_RELEASE_TAG..HEAD
    ```

2. Set the release version in `setup.py` (remove the `-dev` tag if applicable)
and commit the version number change.  Also set the new version number in the
readme (under "Installation")

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
