.PHONY: install test run clean

install:
	pip install -e ".[test]"

test:
	pytest

run:
	physex --constants

clean:
	rm -rf build dist .pytest_cache .mypy_cache .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name '*.egg-info' -exec rm -rf {} +
