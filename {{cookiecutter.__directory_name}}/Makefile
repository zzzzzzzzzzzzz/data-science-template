.PHONY: tests

deps: 
	@echo "Initializing Git..."
	git init
	{% if cookiecutter.dependency_manager == "poetry" %}
	@echo "Installing dependencies..."
	poetry install --no-root
	poetry run pre-commit install
	{% elif cookiecutter.dependency_manager == "conda-pip" %}
	conda create --name {{ cookiecutter.project_name.lower().replace(' ', '-').replace('_', '-') }}-{{ cookiecutter.compatible_python_versions | regex_format('\d\.\d{1,2}') }} python={{ cookiecutter.compatible_python_versions | regex_format('\d\.\d{1,2}') }}
	pip install --upgrade pip
	@echo "Installing dependencies..."
	pip install -r requirements-dev.txt
	pre-commit install
	{% else %}
	python{{ cookiecutter.compatible_python_versions | regex_format('\d\.\d{1,2}') }} -m venv {{ cookiecutter.project_name.lower().replace(' ', '_') }}_{{ cookiecutter.compatible_python_versions | regex_format('\d\.\d{1,2}').replace('.', '') }}_venv
	source {{ cookiecutter.project_name.lower().replace(' ', '_') }}_{{ cookiecutter.compatible_python_versions | regex_format('\d\.\d{1,2}').replace('.', '') }}_venv/bin/activate
	pip install --upgrade pip
	@echo "Installing dependencies..."
	pip install -r requirements-dev.txt
	pre-commit install
	{% endif %}
tests:
	pytest
