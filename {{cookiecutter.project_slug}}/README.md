# Python Packaging with `setup.py`, `setup.cfg` and `pyproject.toml`

```sh
# Editable install
pip install -e .
pip install -e .[testing]

# Build
pip install build
python -m build -s
python -m build

unzip -l ./dist/*.whl

# Publish
pip install twine
twine upload dist/*
```

Packing stacks:

- frontend: pip, build, cibuildwheel
- backend: setuptools, distlib, flit, hatch
- publish: twine

[Configuring setuptools](https://setuptools.pypa.io/en/latest/userguide/index.html)

[Python Packaging with Setuptools. This article will explain the best… | by Insight in Plain Sight | ITNEXT](https://itnext.io/python-packaging-12ef040c4ea0)

[Packaging Python Projects — Python Packaging User Guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
