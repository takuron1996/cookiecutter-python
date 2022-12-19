SHELL = /bin/bash
PYLINT = poetry run pylint
FORMAT = poetry run black
FORMAT_BLACK = poetry run black
FORMAT_ISORT = poetry run isort
LINTRCF	= pylintrc.txt
LINTRST = pylintresult.txt
RUN_FILE = {{cookiecutter.project_name}}/example.py
TEST = tests
COVERAGE = htmlcov
DOCS = docs
PYCS = $(shell find . -type d -name .venv -prune -o -type d -name "__pycache__" -print)
VENV = .venv
EXCLUDE = -not -name .coveragerc -not -name .gitignore

run: format
	poetry run python $(RUN_FILE)

test: format
	poetry run pytest --cov -v --cov-report=html

html: test
	open $(COVERAGE)/index.html 


lint: format
	@if [ ! -e $(LINTRCF) ]; then $(PYLINT) --generate-rcfile > $(LINTRCF) 2> /dev/null ; fi
	@$(PYLINT) --rcfile=$(LINTRCF) --ignore=$(VENV) `find . -type d -name $(VENV) -prune -o -name "*.py" -print` > $(LINTRST); \
	less $(LINTRST)

format:
	@$(FORMAT_BLACK) .
	@$(FORMAT_ISORT) .

clean:
	@if [ -d $(VENV) ]; then echo "rm -rf $(VENV)"; rm -rf $(VENV); fi
	@if [ -d $(COVERAGE) ]; then echo "rm -rf $(COVERAGE)"; rm -rf $(COVERAGE); fi
	@if [ -e $(LINTRST) ] ; then echo "rm -f $(LINTRST)" ; rm -f $(LINTRST) ; fi
	@find . -maxdepth 1 $(EXCLUDE) -type f -name ".*" -exec rm {} ";" -exec echo rm -f {} ";"
	@for each in ${PYCS} ; do echo "rm -rf $${each}" ; rm -rf $${each} ; done
	@if [ -e poetry.lock ] ; then echo "rm -f poetry.lock" ; rm -f poetry.lock; fi

install:
	poetry install

update:
	poetry update

docs:
	poetry run pdoc {{cookiecutter.project_name}} --html -o $(DOCS) --force
	poetry run pdoc tests --html -o $(DOCS) --force


check: format
	poetry run mypy --install-types --non-interactive
