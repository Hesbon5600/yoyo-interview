#@-- help command to show usage of make commands --@#
help:
	@echo "----------------------------------------------------------------------------"
	@echo "-                     Available commands                                   -"
	@echo "----------------------------------------------------------------------------"
	@echo "---> make env              - To create virtual environment"
	@echo "---> make activate         - To activate virtual environment"
	@echo "---> make install          - To install dependencies from Pipfile.lock"
	@echo "---> make update           - To update the Pipfile.lock"
	@echo "---> make test             - To run all tests and show coverage"
	@echo "---> make lint             - To run the flake8 linter"
	@echo "---> make run              - To start the server"
	@echo " "


env:
	@ echo '<<<<<<<<<<Creating virtual environment>>>>>>>>>'
	pipenv shell --python 3.9
	@ echo ''

activate:
	@ echo '<<<<<<<<<<Activating virtual environment>>>>>>>>>'
	pipenv shell
	@ echo ''

install:
	@ echo '<<<<<<<<<<installing requirements>>>>>>>>>'
	pipenv install --dev
	@ echo ''


update:
	@ echo '<<<<<<<<<<updating Pipfile.lock>>>>>>>>>'
	pipenv update
	@ echo ''

test:
	@ echo '<<<<<<<<<<Run tests>>>>>>>>>'
	coverage run --source=app/api manage.py test --verbosity=2  && coverage report -m
	@ echo ''

run:
	@ echo '<<<<<<<<<<starting server>>>>>>>>>'
	python manage.py runserver
	@ echo ''


lint:
	@ echo '<<<<<<<<<<linting>>>>>>>>>'
	flake8 .
	@ echo ''

#@-- help should be run by default when no command is specified --@#
default: help
