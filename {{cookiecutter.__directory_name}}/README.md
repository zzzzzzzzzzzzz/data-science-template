# {{cookiecutter.project_name}}

Built from cookiecutter project [`data-science-template`](https://github.com/zzzzzzzzzzzzz/data-science-template)

## Tools used in this project
* pre commit plugins
  * [pre-commit](https://pre-commit.com/): Automate code reviewing formatting
  * [flake8](https://flake8.pycqa.org/en/latest/)
  * [isort](https://pypi.org/project/isort/)
  * [black](https://black.readthedocs.io/en/stable/)
  * [nbstripout](https://github.com/kynan/nbstripout): to strip output of jupyter notebooks during commit
  * [nbQA](https://github.com/nbQA-dev/nbQA?tab=readme-ov-file#-installation): to be able to run black and isort with jupyter notebooks
{% if cookiecutter.dependency_manager == "poetry" -%}
* [Poetry](https://towardsdatascience.com/how-to-effortlessly-publish-your-python-package-to-pypi-using-poetry-44b305362f9f): Dependency management - [article](https://mathdatasimplified.com/poetry-a-better-way-to-manage-python-dependencies/)
{% else -%}
* [pip](https://pypi.org/project/pip/)
{% endif -%}

## Project Structure

```bash
.
├── data            
│   ├── input                       # raw input data
│   └── output                      # all outputs that occur in your project
├── Makefile                        # store useful commands to set up the environment
├── models                          # store models
├── notebooks                       # store notebooks
│   ├── shareable                   # put a notebook here if you want to share it in repo
├── .flake8                         # flake8 linter configuration
├── .gitignore                      # ignore files that cannot commit to Git
{% if cookiecutter.dependency_manager == "poetry" -%}
├── pyproject.toml                  # dependencies for poetry
{% else -%}
├── pyproject.toml                  # Configure isort and other pre-commit utilities
├── requirements.txt                # prod requirements
├── requirements-dev.txt            # prod requirements, including dev requirements
{% endif -%}
├── .pre-commit-config.yaml         # configurations for pre-commit
├── README.md                       # describe your project
├── src                             # store source code
│   └── __init__.py                 # make src a Python module 
└── tests                           # store tests
    └── __init__.py                 # make tests a Python module
```

## Set up the environment
1. You should have dedicated [conda](https://docs.anaconda.com/free/miniconda/miniconda-install.html) environment with certain python version. You might want to consider python version not less than: {{ cookiecutter.compatible_python_versions | regex_format('\d\.\d{1,2}') }}
{% if cookiecutter.dependency_manager == "poetry" %}
2. Install [Poetry](https://python-poetry.org/docs/#installation). E.g. with conda
```bash
conda install poetry
```
3. To setup everything for development, including pre-commit hooks, run
```bash
make deps
```
{% else %}
2. To setup everything for development, including pre-commit hooks, run
```bash
make deps
```
{% endif %}

## Manual management
{% if cookiecutter.dependency_manager == "poetry" %}
- To install only production dependencies, run:
```bash
poetry install --only main
```
- To install a new package, run:
```bash
poetry add <package-name>
```
{% else %}
- To install only production dependencies, run:
```bash
pip install -r requirements.txt
```
- To install a new package, run:
```bash
pip install <package-name>
```
{% endif %}