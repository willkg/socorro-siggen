DEFAULT_GOAL := help
PROJECT=siggen

.PHONY: help
help:
	@echo "Available rules:"
	@echo ""
	@fgrep -h "##" Makefile | fgrep -v fgrep | sed 's/\(.*\):.*##/\1:/'

.PHONY: clean
clean:  ## Clean build artifacts
	rm -rf build dist ${PROJECT}.egg-info .tox .pytest-cache
	rm -rf docs/_build/*
	find ${PROJECT}/ tests/ -name __pycache__ | xargs rm -rf
	find ${PROJECT}/ tests/ -name '*.pyc' | xargs rm -rf

.PHONY: lint
lint:  ## Lint files
	tox -e py39-flake8

.PHONY: test
test:  ## Run tests
	tox

.PHONY: checkrot
checkrot:  ## Check package rot for dev dependencies
	python -m venv ./tmpvenv/
	./tmpvenv/bin/pip install -U pip
	./tmpvenv/bin/pip install -r requirements-dev.txt
	./tmpvenv/bin/pip list -o
	rm -rf ./tmpvenv/
