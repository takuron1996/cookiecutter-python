SHELL = /bin/bash
PYLINT = poetry run pylint
FORMAT = poetry run black
LINTRCF	= pylintrc.txt
LINTRST = pylintresult.txt
RUN_FILE = {{cookiecutter.project_name}}/example.py
TEST = tests
COVERAGE = htmlcov
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
	@$(FORMAT) .

clean:
	@if [ -d $(VENV) ]; then echo "sudo rm -rf $(VENV)"; sudo rm -rf $(VENV); fi
	@if [ -d $(COVERAGE) ]; then echo "sudo rm -rf $(COVERAGE)"; sudo rm -rf $(COVERAGE); fi
	@if [ -e $(LINTRST) ] ; then echo "rm -f $(LINTRST)" ; rm -f $(LINTRST) ; fi
	@find . -maxdepth 1 $(EXCLUDE) -type f -name ".*" -exec rm {} ";" -exec echo rm -f {} ";"
	@for each in ${PYCS} ; do echo "rm -rf $${each}" ; rm -rf $${each} ; done
	@if [ -e poetry.lock ] ; then echo "rm -f poetry.lock" ; rm -f poetry.lock; fi

install:
	poetry install

update:
	poetry update
