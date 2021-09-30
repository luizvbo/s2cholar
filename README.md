# s2cholar

Client for the new Semantic Scholar API.

We used the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen)
project to generate the initial version of this package, which was then
modified by the contributors.

Details of the Swagger Codegen used:

- API version: 1.0
- Package version: 0.1.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Announcement

This project is **active** and **under development**. Everyone is more than
welcome to help and contribute.

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/luizvbo/s2cholar.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/luizvbo/s2cholar.git`)

Then import the package:
```python
import s2cholar
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import s2cholar
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import s2cholar
from s2cholar.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = s2cholar.AuthorApi(s2cholar.ApiClient(configuration))
author_id = '145872832' # str

try:
    # Details about an author
    api_response = api_instance.get_graph_get_author(author_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorApi->get_graph_get_author: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.semanticscholar.org/graph/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthorApi* | [**get_graph_get_author**](docs/AuthorApi.md#get_graph_get_author) | **GET** /author/{author_id} | Details about an author
*AuthorApi* | [**get_graph_get_author_papers**](docs/AuthorApi.md#get_graph_get_author_papers) | **GET** /author/{author_id}/papers | Details about an author&#39;s papers
*PaperApi* | [**get_paper**](docs/PaperApi.md#get_paper) | **GET** /paper/{paper_id} | Details about a paper
*PaperApi* | [**get_paper_authors**](docs/PaperApi.md#get_paper_authors) | **GET** /paper/{paper_id}/authors | Details about a paper&#39;s authors
*PaperApi* | [**get_paper_citations**](docs/PaperApi.md#get_paper_citations) | **GET** /paper/{paper_id}/citations | Details about a paper&#39;s citations
*PaperApi* | [**get_paper_references**](docs/PaperApi.md#get_paper_references) | **GET** /paper/{paper_id}/references | Details about a paper&#39;s references
*PaperApi* | [**get_paper_search**](docs/PaperApi.md#get_paper_search) | **GET** /paper/search | Search for papers by keyword


## Documentation For Models

 - [Author](docs/Author.md)
 - [AuthorBatch](docs/AuthorBatch.md)
 - [AuthorInfo](docs/AuthorInfo.md)
 - [AuthorWithPapers](docs/AuthorWithPapers.md)
 - [BasePaper](docs/BasePaper.md)
 - [Citation](docs/Citation.md)
 - [CitationBatch](docs/CitationBatch.md)
 - [CitationCitingPaper](docs/CitationCitingPaper.md)
 - [Embedding](docs/Embedding.md)
 - [Error400](docs/Error400.md)
 - [Error404](docs/Error404.md)
 - [FullPaper](docs/FullPaper.md)
 - [PaperBatch](docs/PaperBatch.md)
 - [PaperInfo](docs/PaperInfo.md)
 - [PaperSearchBatch](docs/PaperSearchBatch.md)
 - [PaperWithLinks](docs/PaperWithLinks.md)
 - [Reference](docs/Reference.md)
 - [ReferenceBatch](docs/ReferenceBatch.md)
 - [ReferenceCitedPaper](docs/ReferenceCitedPaper.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author

[Luiz Otavio Vilas Boas Oliveira](http://luizvbo.github.io/)

## Contribution

Contributions are more than welcome to this package.

### Commit Messages

In order to keep our git log clean, use the tags below in your commit messages
(adapted from the [numpy workflow](https://numpy.org/doc/1.14/dev/gitwash/development_workflow.html)):

- API: an (incompatible) API change
- BUG: bug fix
- CICD: changes to the CI/CD
- DEP: deprecate something, or remove a deprecated object
- DOC: documentation
- ENH: enhancement
- MAINT: maintenance commit (refactoring, typos, etc.)
- REV: revert an earlier commit
- STY: style fix (whitespace, PEP8)
- TST: addition or modification of tests
