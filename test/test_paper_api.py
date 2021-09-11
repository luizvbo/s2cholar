# coding: utf-8

"""
    Literature Graph Service

    Fetch paper and author data from the Semantic Scholar corpus  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import s2cholar
from s2cholar.api.paper_api import PaperApi  # noqa: E501
from s2cholar.rest import ApiException


class TestPaperApi(unittest.TestCase):
    """PaperApi unit test stubs"""

    def setUp(self):
        self.api = s2cholar.api.paper_api.PaperApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_graph_get_paper(self):
        """Test case for get_graph_get_paper

        Details about a paper  # noqa: E501
        """
        pass

    def test_get_graph_get_paper_authors(self):
        """Test case for get_graph_get_paper_authors

        Details about a paper's authors  # noqa: E501
        """
        pass

    def test_get_graph_get_paper_citations(self):
        """Test case for get_graph_get_paper_citations

        Details about a paper's citations  # noqa: E501
        """
        pass

    def test_get_graph_get_paper_references(self):
        """Test case for get_graph_get_paper_references

        Details about a paper's references  # noqa: E501
        """
        pass

    def test_get_graph_get_paper_search(self):
        """Test case for get_graph_get_paper_search

        Search for papers by keyword  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
