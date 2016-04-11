# Python-Packaging-Example
A simple example of how to package Python code for PyPI and Anaconda Cloud.

## Building for and Uploading to PyPI

Some useful commands for building, registering, and uploading a package:

    python setup.py sdist
    python setup.py register -r https://testpypi.python.org/pypi
    python setup.py sdist upload -r https://testpypi.python.org/pypi

Some useful documentation:

    http://python-packaging.readthedocs.org/en/latest/index.html
    https://www.pypa.io/en/latest/
