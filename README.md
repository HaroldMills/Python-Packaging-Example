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
    
## Building for and Uploading to Anaconda Cloud

Some useful commands for building and uploading a package:

    conda skeleton pypi --pypi-url https://testpypi.python.org/pypi harold_packaging_example
    anaconda upload C:\Users\Harold\Miniconda3\conda-bld\win-64\harold_packaging_example-0.1.3-py35_0.tar.bz2
