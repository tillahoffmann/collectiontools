.PHONY : all dist docs doctests lint tests typecheck

all : doctests docs lint tests dist typecheck

docs :
	rm -rf docs/_build
	sphinx-build -vW . docs/_build

doctests :
	rm -rf docs/_build
	sphinx-build -b doctest . docs/_build

lint :
	ruff format --check .
	ruff check

typecheck :
	pyright

tests :
	pytest -v --cov=collectiontools --cov-report=term-missing --cov-fail-under=100

dist :
	uv build
