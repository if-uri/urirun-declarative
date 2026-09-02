PYTHON ?= python3

.PHONY: install doctor-build doctor-test doctor-health test check

install:
	$(PYTHON) -m pip install -e ".[test]"

doctor-build:
	$(PYTHON) -c "import ast, pathlib; [ast.parse(path.read_text(encoding='utf-8'), filename=str(path)) for path in pathlib.Path('src').rglob('*.py')]"

doctor-test:
	PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src $(PYTHON) -m pytest -q

doctor-health:
	PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src $(PYTHON) -c "import urirun_declarative"

test: doctor-test

check: doctor-build doctor-test doctor-health
