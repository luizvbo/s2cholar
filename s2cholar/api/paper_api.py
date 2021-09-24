# coding: utf-8

"""
    Literature Graph Service

    Fetch paper and author data from the Semantic Scholar corpus

    OpenAPI spec version: 1.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re
from typing import List, Tuple

# python 2 and python 3 compatibility library
import six

from s2cholar.api_client import ApiClient


class PaperApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_paper(
        self, paper_id: str = "", fields_to_exclude: List[str] = [],
        async_req: bool = False, return_http_data_only: bool = False,
        preload_content: bool = True,
        request_timeout: Tuple[None, int, Tuple[int, int]] = None
    ):

        """Details about a paper

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_paper(paper_id, async_req=True)
        >>> result = thread.get()

        Args:
            paper_id (str): The following types of IDs are supported:
                - `<sha>` - a Semantic Scholar ID, e.g.
                  `649def34f8be52c8b66281af98ae884c09aef38b`
                - `CorpusId:<id>` - Semantic Scholar numerical ID, e.g.
                  `215416146`
                - `DOI:<doi>` - a Digital Object Identifier, e.g.
                  `DOI:10.18653/v1/N18-3011`
                - `ARXIV:<id>` - arXiv.rg, e.g. `ARXIV:2106.15928`
                - `MAG:<id>` - Microsoft Academic Graph, e.g. `MAG:112218234`
                - `ACL:<id>` - Association for Computational Linguistics, e.g.
                  `ACL:W12-3903`
                - `PMID:<id>` - PubMed/Medline, e.g. `PMID:19872477`
                - `PMCID:<id>` - PubMed Central, e.g. `PMCID:2323736`
                - `URL:<url>` - URL from one of the sites listed below, e.g.
                  `URL:https://arxiv.org/abs/2106.15928v1` URLs are recognized
                  from the following sites:
                - [semanticscholar.org](semanticscholar.org)
                - [arxiv.org](arxiv.org)
                - [aclweb.org](aclweb.org)
                - [acm.org](acm.org)
                - [biorxiv.org](biorxiv.org)
            fields_to_exclude (List[str]): By default, this function returns
                all fields available. In case you want to exclude some of these
                fields, you should pass as a list of strings. The fields are:
                    - paperId: Always included
                    - externalIds
                    - url
                    - title: Included if no fields are specified
                    - abstract
                    - venue
                    - year
                    - referenceCount
                    - citationCount
                    - influentialCitationCount
                    - isOpenAccess
                    - fieldsOfStudy
                    - authors.authorId
                    - authors.externalIds
                    - authors.url
                    - authors.name
                    - authors.aliases
                    - authors.affiliations
                    - authors.homepage
                    - citations.paperId
                    - citations.url
                    - citations.title
                    - citations.venue
                    - citations.year
                    - citations.authors
                    - references.paperId
                    - references.url
                    - references.title
                    - references.venue
                    - references.year
                    - references.authors
                    - embedding'

        Returns:
            FullPaper: If the method is called asynchronously, returns the
                request thread.
        """
        fields = {
            'paperId', 'externalIds', 'url', 'title', 'abstract', 'venue',
            'year', 'referenceCount', 'citationCount',
            'influentialCitationCount', 'isOpenAccess', 'fieldsOfStudy',
            'authors.authorId', 'authors.externalIds', 'authors.url',
            'authors.name', 'authors.aliases', 'authors.affiliations',
            'authors.homepage', 'citations.paperId', 'citations.url',
            'citations.title', 'citations.venue', 'citations.year',
            'citations.authors', 'references.paperId', 'references.url',
            'references.title', 'references.venue', 'references.year',
            'references.authors', 'embedding'
        }
        # Keep only fields not listed in `fields_to_exclude`
        fields = fields - set(fields_to_exclude)

        collection_formats = {}

        path_params = {'paper_id': paper_id}
        query_params = [('fields', ','.join(fields))]

        header_params = {}
        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json']
        )

        # HTTP header `Content-Type`
        header_params['Content-Type'] = (
            self.api_client.select_header_content_type(['application/json'])
        )

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/paper/{paper_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FullPaper',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=return_http_data_only,
            _preload_content=preload_content,
            _request_timeout=request_timeout,
            collection_formats=collection_formats
        )

    def get_paper_authors(
        self, paper_id, fields_to_exclude: List[str] = [],
        async_req: bool = False, return_http_data_only: bool = False,
        preload_content: bool = True,
        request_timeout: Tuple[None, int, Tuple[int, int]] = None
    ):
        """Details about a paper's authors

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_paper_authors(paper_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        Args:
            paper_id (str): The following types of IDs are supported:
                - `<sha>` - a Semantic Scholar ID, e.g.
                  `649def34f8be52c8b66281af98ae884c09aef38b`
                - `CorpusId:<id>` - Semantic Scholar numerical ID, e.g.
                  `215416146`
                - `DOI:<doi>` - a Digital Object Identifier, e.g.
                  `DOI:10.18653/v1/N18-3011`
                - `ARXIV:<id>` - arXiv.rg, e.g. `ARXIV:2106.15928`
                - `MAG:<id>` - Microsoft Academic Graph, e.g. `MAG:112218234`
                - `ACL:<id>` - Association for Computational Linguistics, e.g.
                  `ACL:W12-3903`
                - `PMID:<id>` - PubMed/Medline, e.g. `PMID:19872477`
                - `PMCID:<id>` - PubMed Central, e.g. `PMCID:2323736`
                - `URL:<url>` - URL from one of the sites listed below, e.g.
                  `URL:https://arxiv.org/abs/2106.15928v1` URLs are recognized
                  from the following sites:
                - [semanticscholar.org](semanticscholar.org)
                - [arxiv.org](arxiv.org)
                - [aclweb.org](aclweb.org)
                - [acm.org](acm.org)
                - [biorxiv.org](biorxiv.org)
            fields_to_exclude (List[str]): By default, this function returns
                all fields available. In case you want to exclude some of these
                fields, you should pass as a list of strings. The fields are:
                    - authorId
                    - externalIds
                    - url
                    - name
                    - aliases
                    - affiliations
                    - homepage
                    - papers.paperId
                    - papers.externalIds
                    - papers.url
                    - papers.title
                    - papers.abstract
                    - papers.venue
                    - papers.year
                    - papers.referenceCount
                    - papers.citationCount
                    - papers.influentialCitationCount
                    - papers.isOpenAccess
                    - papers.fieldsOfStudy
                    - papers.authors'

        Returns:
            AuthorBatch: If the method is called asynchronously, returns the
                request thread.
        """

        fields = {
            'authorId', 'externalIds', 'url', 'name', 'aliases',
            'affiliations', 'homepage', 'papers.paperId', 'papers.externalIds',
            'papers.url', 'papers.title', 'papers.abstract', 'papers.venue',
            'papers.year', 'papers.referenceCount', 'papers.citationCount',
            'papers.influentialCitationCount', 'papers.isOpenAccess',
            'papers.fieldsOfStudy', 'papers.authors'
        }
                # Keep only fields not listed in `fields_to_exclude`
        fields = fields - set(fields_to_exclude)

        collection_formats = {}

        path_params = {'paper_id': paper_id}
        query_params = [('fields', ','.join(fields))]

        header_params = {}
        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json']
        )

        # HTTP header `Content-Type`
        header_params['Content-Type'] = (
            self.api_client.select_header_content_type(['application/json'])
        )

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/paper/{paper_id}/authors', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AuthorBatch',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=return_http_data_only,
            _preload_content=preload_content,
            _request_timeout=request_timeout,
            collection_formats=collection_formats
        )

    def get_paper_citations(
        self, paper_id: str = "", fields_to_exclude: List[str] = [],
        offset: int = 0, limit: int = 100, async_req: bool = False,
        return_http_data_only: bool = False, preload_content: bool = True,
        request_timeout: Tuple[None, int, Tuple[int, int]] = None
    ):
        """Details about a paper's citations

        Fetch details about the papers the cite this paper (i.e. papers in whose bibliography this paper appears)
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_paper_citations(paper_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        Args:
            paper_id (str): The following types of IDs are supported:
                - `<sha>` - a Semantic Scholar ID, e.g.
                  `649def34f8be52c8b66281af98ae884c09aef38b`
                - `CorpusId:<id>` - Semantic Scholar numerical ID, e.g.
                  `215416146`
                - `DOI:<doi>` - a Digital Object Identifier, e.g.
                  `DOI:10.18653/v1/N18-3011`
                - `ARXIV:<id>` - arXiv.rg, e.g. `ARXIV:2106.15928`
                - `MAG:<id>` - Microsoft Academic Graph, e.g. `MAG:112218234`
                - `ACL:<id>` - Association for Computational Linguistics, e.g.
                  `ACL:W12-3903`
                - `PMID:<id>` - PubMed/Medline, e.g. `PMID:19872477`
                - `PMCID:<id>` - PubMed Central, e.g. `PMCID:2323736`
                - `URL:<url>` - URL from one of the sites listed below, e.g.
                  `URL:https://arxiv.org/abs/2106.15928v1` URLs are recognized
                  from the following sites:
                - [semanticscholar.org](semanticscholar.org)
                - [arxiv.org](arxiv.org)
                - [aclweb.org](aclweb.org)
                - [acm.org](acm.org)
                - [biorxiv.org](biorxiv.org)
            fields_to_exclude (List[str]): By default, this function returns
                all fields available. In case you want to exclude some of these
                fields, you should pass as a list of strings. The fields are:
                - contexts
                - intents
                - isInfluential
                - paperId: Always included
                - externalIds
                - url
                - title: Included if no fields are specified
                - abstract
                - venue
                - year
                - referenceCount
                - citationCount
                - influentialCitationCount
                - isOpenAccess
                - fieldsOfStudy
                - authors

        Returns:
            CitationBatch: If the method is called asynchronously, returns the
                request thread.
        """
        fields = [
            'contexts', 'intents', 'isInfluential', 'paperId', 'externalIds',
            'url', 'title', 'abstract', 'venue', 'year', 'referenceCount',
            'citationCount', 'influentialCitationCount', 'isOpenAccess',
            'fieldsOfStudy', 'authors'
        ]
        # Keep only fields not listed in `fields_to_exclude`
        fields = [
            field for field in fields if field not in set(fields_to_exclude)
        ]

        collection_formats = {}

        path_params = {'paper_id': paper_id}

        query_params = [
            ('fields', ','.join(fields)),
            ('offset', offset),
            ('limit', limit)
        ]

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/paper/{paper_id}/citations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CitationBatch',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=return_http_data_only,
            _preload_content=preload_content,
            _request_timeout=request_timeout,
            collection_formats=collection_formats)

    def get_graph_get_paper_references(self, paper_id, **kwargs):
        """Details about a paper's references

        Fetch details about the papers cited by this paper (i.e. appearing in this paper's bibliography)
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_graph_get_paper_references(paper_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        Args:
            paper_id (str): The following types of IDs are supported:
                - `<sha>` - a Semantic Scholar ID, e.g.
                  `649def34f8be52c8b66281af98ae884c09aef38b`
                - `CorpusId:<id>` - Semantic Scholar numerical ID, e.g.
                  `215416146`
                - `DOI:<doi>` - a Digital Object Identifier, e.g.
                  `DOI:10.18653/v1/N18-3011`
                - `ARXIV:<id>` - arXiv.rg, e.g. `ARXIV:2106.15928`
                - `MAG:<id>` - Microsoft Academic Graph, e.g. `MAG:112218234`
                - `ACL:<id>` - Association for Computational Linguistics, e.g.
                  `ACL:W12-3903`
                - `PMID:<id>` - PubMed/Medline, e.g. `PMID:19872477`
                - `PMCID:<id>` - PubMed Central, e.g. `PMCID:2323736`
                - `URL:<url>` - URL from one of the sites listed below, e.g.
                  `URL:https://arxiv.org/abs/2106.15928v1` URLs are recognized
                  from the following sites:
                - [semanticscholar.org](semanticscholar.org)
                - [arxiv.org](arxiv.org)
                - [aclweb.org](aclweb.org)
                - [acm.org](acm.org)
                - [biorxiv.org](biorxiv.org)
        :return: ReferenceBatch
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_graph_get_paper_references_with_http_info(paper_id, **kwargs)
        else:
            (data) = self.get_graph_get_paper_references_with_http_info(paper_id, **kwargs)
            return data

    def get_graph_get_paper_references_with_http_info(self, paper_id, **kwargs):
        """Details about a paper's references

        Fetch details about the papers cited by this paper (i.e. appearing in this paper's bibliography)
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_graph_get_paper_references_with_http_info(paper_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        Args:
            paper_id (str): The following types of IDs are supported:
                - `<sha>` - a Semantic Scholar ID, e.g.
                  `649def34f8be52c8b66281af98ae884c09aef38b`
                - `CorpusId:<id>` - Semantic Scholar numerical ID, e.g.
                  `215416146`
                - `DOI:<doi>` - a Digital Object Identifier, e.g.
                  `DOI:10.18653/v1/N18-3011`
                - `ARXIV:<id>` - arXiv.rg, e.g. `ARXIV:2106.15928`
                - `MAG:<id>` - Microsoft Academic Graph, e.g. `MAG:112218234`
                - `ACL:<id>` - Association for Computational Linguistics, e.g.
                  `ACL:W12-3903`
                - `PMID:<id>` - PubMed/Medline, e.g. `PMID:19872477`
                - `PMCID:<id>` - PubMed Central, e.g. `PMCID:2323736`
                - `URL:<url>` - URL from one of the sites listed below, e.g.
                  `URL:https://arxiv.org/abs/2106.15928v1` URLs are recognized
                  from the following sites:
                - [semanticscholar.org](semanticscholar.org)
                - [arxiv.org](arxiv.org)
                - [aclweb.org](aclweb.org)
                - [acm.org](acm.org)
                - [biorxiv.org](biorxiv.org)
        :return: ReferenceBatch
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['paper_id', 'offset', 'limit', 'fields']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_graph_get_paper_references" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'paper_id' is set
        if self.api_client.client_side_validation and ('paper_id' not in params or
                                                       params['paper_id'] is None):
            raise ValueError("Missing the required parameter `paper_id` when calling `get_graph_get_paper_references`")

        collection_formats = {}

        path_params = {}
        if 'paper_id' in params:
            path_params['paper_id'] = params['paper_id']

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'fields' in params:
            query_params.append(('fields', params['fields']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/paper/{paper_id}/references', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReferenceBatch',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_graph_get_paper_search(self, query, **kwargs):
        """Search for papers by keyword

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_graph_get_paper_search(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str query: Search query string.  We support boolean operators OR and AND.   If you would like to ensure the inclusion of particular search terms using a MUST operator,  simply include a plus sign before the term that must be included.  For example, searching +Epidemic +Modeling +Canada will ensure each term is included in the results.  Similarly, if you'd like to ensure the exclusion of a particular search term using a MUST NOT operator, simply include a minus sign before the term that must be excluded.  For example, searching +Epidemic +Modeling +Canada -COVID will ensure each term is included in the search results but will exclude content with the negated term.  Semantic Scholar search API does not currently support wildcards. If this is a feature you would like, please let us know. (required)
        :return: PaperSearchBatch
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_graph_get_paper_search_with_http_info(query, **kwargs)
        else:
            (data) = self.get_graph_get_paper_search_with_http_info(query, **kwargs)
            return data

    def get_graph_get_paper_search_with_http_info(self, query, **kwargs):
        """Search for papers by keyword

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_graph_get_paper_search_with_http_info(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str query: Search query string.  We support boolean operators OR and AND.   If you would like to ensure the inclusion of particular search terms using a MUST operator,  simply include a plus sign before the term that must be included.  For example, searching +Epidemic +Modeling +Canada will ensure each term is included in the results.  Similarly, if you'd like to ensure the exclusion of a particular search term using a MUST NOT operator, simply include a minus sign before the term that must be excluded.  For example, searching +Epidemic +Modeling +Canada -COVID will ensure each term is included in the search results but will exclude content with the negated term.  Semantic Scholar search API does not currently support wildcards. If this is a feature you would like, please let us know. (required)
        :param int offset: When returning a list of results, start with the element at this position in the list.
        :param int limit: The maximum number of results to return.
        :return: PaperSearchBatch
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query', 'offset', 'limit', 'fields']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_graph_get_paper_search" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if self.api_client.client_side_validation and ('query' not in params or
                                                       params['query'] is None):
            raise ValueError("Missing the required parameter `query` when calling `get_graph_get_paper_search`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'fields' in params:
            query_params.append(('fields', params['fields']))
        if 'query' in params:
            query_params.append(('query', params['query']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/paper/search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaperSearchBatch',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
