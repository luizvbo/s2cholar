# coding: utf-8

"""
    s2cholar: Python API client for Semantic Scholar

    Fetch paper and author data from the Semantic Scholar corpus
"""


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    'certifi>=2017.4.17',
    'python-dateutil>=2.1',
    'six>=1.10',
    'urllib3>=1.23'
]

setup(
    name='s2cholar',
    version='0.0.0',
    keywords=['Swagger', 'Literature Graph Service'],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
)
