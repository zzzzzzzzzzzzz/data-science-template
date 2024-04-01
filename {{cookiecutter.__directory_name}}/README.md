# {{cookiecutter.project_name}}

Built from cookiecutter project [`data-science-template`](https://github.com/zzzzzzzzzzzzz/data-science-template)

## Tools used in this project
* * pre commit plugins
    * [pre-commit](https://pre-commit.com/): Automate code reviewing formatting
    * [flake8](https://flake8.pycqa.org/en/latest/)
    * [isort](https://pypi.org/project/isort/)
    * [black](https://black.readthedocs.io/en/stable/)
    * [nbstripout](https://github.com/kynan/nbstripout): to strip output of jupyter notebooks during commit
    * [nbQA](https://github.com/nbQA-dev/nbQA?tab=readme-ov-file#-installation): to be able to run black and isort with jupyter notebooks
{% if cookiecutter.dependency_manager == "poetry" %}
* [Poetry](https://towardsdatascience.com/how-to-effortlessly-publish-your-python-package-to-pypi-using-poetry-44b305362f9f): Dependency management - [article](https://mathdatasimplified.com/poetry-a-better-way-to-manage-python-dependencies/)
{% endif %}

## Project Structure

```bash
.
├── data            
│   ├── input                       # raw input data
│   └── raw                         # all outputs that occur in your project
├── .gitignore                      # ignore files that cannot commit to Git
├── Makefile                        # store useful commands to set up the environment
├── models                          # store models
├── notebooks                       # store notebooks
{% if cookiecutter.dependency_manager != "poetry" -%}
├── pyproject.toml                  # Configure isort and other pre-commit utilities
{% elif cookiecutter.dependency_manager == "poetry" -%}
├── .pre-commit-config.yaml         # configurations for pre-commit
├── pyproject.toml                  # dependencies for poetry
{%- endif %}
├── README.md                       # describe your project
├── src                             # store source code
│   └── __init__.py                 # make src a Python module 
└── tests                           # store tests
    └── __init__.py                 # make tests a Python module 
```

## Set up the environment

{% if cookiecutter.dependency_manager == "poetry" %}
1. Install [Poetry](https://python-poetry.org/docs/#installation)
2. Activate the virtual environment:
```bash
poetry shell
```
3. Install dependencies:
- To install all dependencies from pyproject.toml, run:
```bash
poetry install
```
- To install only production dependencies, run:
```bash
poetry install --only main
```
- To install a new package, run:
```bash
poetry add <package-name>
```
{% else %}
1. Create the virtual environment:
```bash
python3 -m venv venv
```
2. Activate the virtual environment:

- For Linux/MacOS:
```bash
source venv/bin/activate
```
- For Command Prompt:
```bash
.\venv\Scripts\activate
```
3. Install dependencies:
- To install all dependencies, run:
```bash
pip install -r requirements-dev.txt
```
- To install only production dependencies, run:
```bash
pip install -r requirements.txt
```
- To install a new package, run:
```bash
pip install <package-name>
```
{% endif %}