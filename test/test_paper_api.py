# coding: utf-8

"""
    Literature Graph Service

    Fetch paper and author data from the Semantic Scholar corpus

"""
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
    expected_author_fields = [
        'authorId', 'externalIds', 'url', 'name', 'aliases', 'affiliations',
        'homepage'
    ]
    expected_paper_fields = [
        'authors', 'paper_id', 'title', 'url', 'venue', 'year'
    ]
    expected_reference_fields = [
        'paperId', 'url', 'title', 'venue', 'year', 'authors'
    ]
    paper = paper_api.get_paper('453a16fa8969e420d95e7d762030b4b933f47aec')
    assert paper[1] == 200
    for field in expected_fields:
        assert hasattr(paper[0], field)
    for field in expected_author_fields:
        assert field in paper[0].authors[0]
    for field in expected_paper_fields:
        assert hasattr(paper[0].citations[0], field)
    for field in expected_reference_fields:
        assert field in paper[0].references[0]


def test_get_paper_authors(paper_api):
    """Test case for get_graph_get_paper_authors

    Details about a paper's authors
    """
    expected_fields = ['data', 'next', 'offset']
    expected_data_fields = [
        'authorId', 'externalIds', 'url', 'name', 'aliases', 'affiliations',
        'homepage', 'papers'
    ]
    authors = paper_api.get_paper_authors(
        '453a16fa8969e420d95e7d762030b4b933f47aec'
    )
    assert authors[1] == 200
    for field in expected_fields:
        assert hasattr(authors[0], field)
    for field in expected_data_fields:
        assert field in authors[0].data[0]


def test_get_paper_citations(paper_api):
    """Test case for get_graph_get_paper_citations

    Details about a paper's citations
    """
    expected_fields = ['data', 'next', 'offset']
    expected_data_fields = [
        'intents', 'isInfluential', 'contexts', 'citingPaper'
    ]
    citations = paper_api.get_paper_citations(
        '453a16fa8969e420d95e7d762030b4b933f47aec'
    )
    assert citations[1] == 200
    for field in expected_fields:
        assert hasattr(citations[0], field)
    for field in expected_data_fields:
        assert field in citations[0].data[0]


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
