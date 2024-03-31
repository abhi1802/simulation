# Simulating a container terminal

This repository is created to simulate the container terminal using python simpy library.

<img width="835" alt="simulation" src="https://github.com/abhi1802/simulation/assets/12717362/229bc005-d74b-4c07-a368-eb5635ffffbe">

### Local setup required to run this application
- You need at least [Python 3.8.0](https://www.python.org/downloads/)
- [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) to create the virtualenv and install required packages

### Setup Development Environment

```bash
# create and go into already created workspace directory.
mkdir project
cd project

# clone this repository
git clone https://github.com/abhi1802/simulation.git
cd simulation

# create python virtual environment
virtualenv -p python3 venv

# activate the new virtual environment
source ./venv/bin/activate

# install required python packages
pip install -r requirements.txt

# run the application
python main.py

```

### Setup environment to run the test cases
- pytest testing framework is used here to write the unit tests.

```bash

# install required python test packages
pip install -r test-requirements.txt

# to run the test cases
pytest test-terminal.py

# to generate the coverage report
pytest --cov=. --cov-report=html test-terminal.py

```
## 100% code coverage achieved as shown below
<img width="581" alt="Screenshot 2024-03-31 at 11 09 12 PM" src="https://github.com/abhi1802/simulation/assets/12717362/80dd1965-9933-427b-bda0-ccb91ac6971f">

