# coding: utf-8

"""
    Literature Graph Service

    Fetch paper and author data from the Semantic Scholar corpus

"""


from __future__ import absolute_import


def test_get_paper(paper_api):
    """Test case for get_paper

    Details about a paper
    """
    expected_fields = [
        'abstract', 'authors', 'citation_count', 'citations', 'embedding',
        'external_ids', 'fields_of_study', 'influential_citation_count',
        'is_open_access', 'paper_id', 'reference_count', 'references', 'title',
        'url', 'venue', 'year'
    ]
    paper = paper_api.get_paper('17498e9bfa0dfd7c74600559e7e5440302b3f672')
    assert paper[1] == 200
    for field in expected_fields:
        assert hasattr(paper[0], field)


def test_get_authors(paper_api):
    """Test case for get_graph_get_paper_authors

    Details about a paper's authors
    """
    expected_fields = ['data', 'discriminator', 'next', 'offset']
    expected_data_fields = [
        'authorId', 'externalIds', 'url', 'name', 'aliases', 'affiliations',
        'homepage', 'papers'
    ]
    authors = paper_api.get_paper_authors(
        '17498e9bfa0dfd7c74600559e7e5440302b3f672'
    )
    assert authors[1] == 200
    for field in expected_fields:
        assert hasattr(authors[0], field)
    for field in expected_data_fields:
        assert field in authors[0].data[0]


def test_get_graph_get_paper_citations():
    """Test case for get_graph_get_paper_citations

    Details about a paper's citations
    """
    pass

def test_get_graph_get_paper_references():
    """Test case for get_graph_get_paper_references

    Details about a paper's references
    """
    pass

def test_get_graph_get_paper_search():
    """Test case for get_graph_get_paper_search

    Search for papers by keyword
    """
    pass
