.PHONY : all dist docs doctests lint tests

all : doctests docs lint tests dist

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
	pytest -v --cov=collectiontools --cov-report=term-missing --cov-fail-under=100

dist :
	python -m build
	twine check dist/*
