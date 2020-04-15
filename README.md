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

# run the application
flask run
```
