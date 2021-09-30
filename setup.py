# coding: utf-8

"""
    s2cholar: Python API client for Semantic Scholar

    Fetch paper and author data from the Semantic Scholar corpus
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "s2cholar"
VERSION = "0.1.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]

setup(
    name=NAME,
    version=VERSION,
    license="MIT license",
    description="Python API client for Semantic Scholar",
    author_email="luiz.vbo@gmail.com",
    author="Luiz Otavio Vilas Boas Oliveira",
    url="https://github.com/luizvbo/s2cholar",
    keywords=["Swagger", "Literature Graph Service"],
    install_requires=REQUIRES,
    packages=find_packages(),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 2.7',
    ],
    include_package_data=True,
    long_description="""\
    Fetch paper and author data from the Semantic Scholar corpus
    """
)
