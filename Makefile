PYTHON ?= python3

.PHONY: install doctor-build doctor-test doctor-health test check

install:
	$(PYTHON) -m pip install -e .

doctor-build:
	$(PYTHON) -m compileall -q src

doctor-test:
	PYTHONPATH=src $(PYTHON) -m pytest -q

doctor-health:
	PYTHONPATH=src $(PYTHON) -c "import urirun_declarative"

test: doctor-test

check: doctor-build doctor-test doctor-health
