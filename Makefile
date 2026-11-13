PYTHON ?= python

.PHONY: install test run clean

install:
	$(PYTHON) -m pip install -e ".[test]"

test:
	$(PYTHON) -m pytest

run:
	$(PYTHON) -m physex.cli --constants

clean:
	rm -rf build dist .pytest_cache .mypy_cache .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name '*.egg-info' -exec rm -rf {} +
