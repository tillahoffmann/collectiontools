.PHONY : all docs doctests lint tests

all : docs doctests lint tests

requirements.txt : requirements.in pyproject.toml
	pip-compile -v

docs :
	rm -rf docs/_build
	sphinx-build -vW . docs/_build

doctests :
	rm -rf docs/_build
	sphinx-build -b doctest . docs/_build

lint :
	black --check .

tests :
	pytest -v --cov=containertools --cov-report=term-missing --cov-fail-under=100
