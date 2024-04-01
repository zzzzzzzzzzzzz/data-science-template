.PHONY: tests

deps: 
	@echo "Initializing Git..."
	git init
	{% if cookiecutter.dependency_manager == "poetry" %}
	@echo "Installing dependencies..."
	poetry install --no-root
	poetry run pre-commit install
	{% else %}
	pip install --upgrade pip
	@echo "Installing dependencies..."
	pip install -r requirements-dev.txt
	pre-commit install
	{% endif %}
tests:
	pytest
