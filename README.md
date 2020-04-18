# balsam
A skeleton project for a python flask api

## Setup
```bash
# Clone the repo

# setup a virtual env
cd balsam
python -m venv .venv
source .venv/bin/activate

# install stuff
pip install requirements.txt

# install the package in development mode
pip install -e .
```

## Running
```bash
# setup some env vars
export FLASK_APP=balsam
export FLASK_ENV=development
export BALSAM_API_KEY=demo_key

# run the application
flask run
```
## Test the application
Navigate to: 
* http://127.0.0.1:5000/
* http://127.0.0.1:5000/balsam/api/v1/tests/simple-object
* http://127.0.0.1:5000/balsam/api/v1/tests/secure-object?api_key=demo_key
