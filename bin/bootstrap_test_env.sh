#!/bin/bash
# Copyright 2026 Cloudera Inc.
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

# Install dependencies to run tests on each supported Python version using tox.

sudo apt install --yes -q python3-pip
python3 -m pip install tox

# Install various python versions.
# Some dependencies in Python 3.8 and 3.9 also need distutils.
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install --yes -q python3.8 python3.8-dev python3.8-distutils
sudo apt install --yes -q python3.9 python3.9-dev python3.9-distutils
sudo apt install --yes -q python3.10 python3.10-dev
sudo apt install --yes -q python3.11 python3.11-dev
sudo apt install --yes -q python3.12 python3.12-dev
sudo apt install --yes -q python3.13 python3.13-dev
sudo apt install --yes -q python3.14 python3.14-dev
