VIRTUALENV_BINARY?=virtualenv
VIRTUALENV_PYTHON_BINARY?=python2

PYTHON_BINARY=./bin/python
PIP_BINARY=./bin/pip


all: virtualenv requirements

virtualenv:
	test -x $(PYTHON_BINARY) || $(VIRTUALENV_BINARY) --python $(VIRTUALENV_PYTHON_BINARY) .

requirements:
	$(PIP_BINARY) install -r requirements.txt
