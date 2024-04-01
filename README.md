# Data Science Sample Project Cookie Cutter

This is a fork from the following [project](https://github.com/khuyentran1401/data-science-template). I modified it for my personal needs. The idea is to provide template for typical notebook driven experience with transition to modular and maintainable code.

## Tools used in this project
* pre commit plugins
    * [pre-commit](https://pre-commit.com/): Automate code reviewing formatting
    * [flake8](https://flake8.pycqa.org/en/latest/)
    * [isort](https://pypi.org/project/isort/)
    * [black](https://black.readthedocs.io/en/stable/)
    * [nbstripout](https://github.com/kynan/nbstripout): to strip output of jupyter notebooks during commit
    * [nbQA](https://github.com/nbQA-dev/nbQA?tab=readme-ov-file#-installation): to be able to run black and isort with jupyter notebooks
* Supported dependency managers 
    * [Poetry](https://towardsdatascience.com/how-to-effortlessly-publish-your-python-package-to-pypi-using-poetry-44b305362f9f): Dependency management - [article](https://mathdatasimplified.com/poetry-a-better-way-to-manage-python-dependencies/)
    * [pip](https://pypi.org/project/pip/)

## How to use this project

Install Cookiecutter:
```bash
pip install cookiecutter
```

Create a project based on the template:
```bash
cookiecutter https://github.com/zzzzzzzzzzzzz/data-science-template
```

## Recommendation
- Once the template is compiled into your project, you may consider to install virtualenv with certain python version before proceeding with installation of dependencies. E.g. you can use [conda](https://docs.anaconda.com/free/miniconda/miniconda-install.html).
- Conda gives the opportunity to install non-python packages(e.g. CUDA with GPU support), while Poetry can be considered as **powerful doge** version of pip. This combination does not limit your ability to manage isolated environment and at the same time gives you the flexibility of Poetry.
- Using development docker container is also a good option.