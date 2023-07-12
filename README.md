# Cookiecutter Python Package Slim

A slim Cookiecutter template for a Python package

* [GitHub - cookiecutter/cookiecutter: A cross-platform command-line utility that creates projects from cookiecutters (project templates), e.g. Python package projects, C projects.](https://github.com/cookiecutter/cookiecutter)

* [GitHub - liviaerxin/python-packaging-setup-cfg-toml](https://github.com/liviaerxin/python-packaging-setup-cfg-toml)

* [GitHub - audreyfeldroy/cookiecutter-pypackage: Cookiecutter template for a Python package.](https://github.com/audreyfeldroy/cookiecutter-pypackage)

## Getting Started

Install the latest Cookiecutter if you haven't installed it yet (this requires Cookiecutter 1.4.0 or higher):

```sh
pip install -U cookiecutter
```

Generate a Python package project from local project directory:

```sh
cookiecutter cookiecutter-py-package-slim/
```

Generate a Python package project from GitHub:

```sh
cookiecutter https://github.com/liviaerxin/cookiecutter-py-package-slim.git
```

## TO-DO

- [x] add github actions 
- [ ] use `pyproject.toml` and deprecate `setup.cfg`
- [ ] Unite using `setup.py`, `setup.cfg` and `pyproject.toml` files all in `pyproject.toml`.
- [ ] Use `pip` to build wheel instead of `build` tool.
- [ ] [pip wheel](https://pip.pypa.io/en/stable/cli/pip_wheel/)
- [ ] add tests

https://www.seanh.cc/2022/05/21/publishing-python-packages-from-github-actions/

## Features

## Python Packaging

* [Configuring setuptools](https://setuptools.pypa.io/en/latest/userguide/index.html)

* [Python Packaging with Setuptools. This article will explain the best… | by Insight in Plain Sight | ITNEXT](https://itnext.io/python-packaging-12ef040c4ea0)

* [Packaging Python Projects — Python Packaging User Guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
