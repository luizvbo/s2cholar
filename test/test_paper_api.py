# coding: utf-8

"""
    Literature Graph Service

    Fetch paper and author data from the Semantic Scholar corpus

"""
PAPER_ID = '453a16fa8969e420d95e7d762030b4b933f47aec'

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
    paper = paper_api.get_paper(PAPER_ID)
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
    """Test case for get_paper_authors

    Details about a paper's authors
    """
    expected_fields = ['data', 'next', 'offset']
    expected_data_fields = [
        'authorId', 'externalIds', 'url', 'name', 'aliases', 'affiliations',
        'homepage', 'papers'
    ]
    authors = paper_api.get_paper_authors(PAPER_ID)
    assert authors[1] == 200
    for field in expected_fields:
        assert hasattr(authors[0], field)
    for field in expected_data_fields:
        assert field in authors[0].data[0]


def test_get_paper_citations(paper_api):
    """Test case for get_paper_citations

    Details about a paper's citations
    """
    expected_fields = ['data', 'next', 'offset']
    expected_data_fields = [
        'intents', 'isInfluential', 'contexts', 'citingPaper'
    ]
    citations = paper_api.get_paper_citations(PAPER_ID)
    assert citations[1] == 200
    for field in expected_fields:
        assert hasattr(citations[0], field)
    for field in expected_data_fields:
        assert field in citations[0].data[0]


def test_get_paper_references(paper_api):
    """Test case for get_paper_references

    Details about a paper's references
    """
    expected_fields = ['data', 'next', 'offset']
    expected_data_fields = [
        'intents', 'isInfluential', 'contexts', 'citedPaper'
    ]
    references = paper_api.get_paper_references(PAPER_ID)
    assert references[1] == 200
    for field in expected_fields:
        assert hasattr(references[0], field)
    for field in expected_data_fields:
        assert field in references[0].data[0]


def test_get_paper_search(paper_api):
    """Test case for get_paper_search

    Search for papers by keyword
    """
    expected_fields = ['data', 'next', 'offset']
    expected_data_fields = [
        'paperId', 'externalIds', 'url', 'title', 'abstract', 'venue', 'year',
        'referenceCount', 'citationCount', 'influentialCitationCount',
        'isOpenAccess', 'fieldsOfStudy', 'authors'
    ]
    papers = paper_api.get_paper_search('weasul')
    assert papers[1] == 200
    for field in expected_fields:
        assert hasattr(papers[0], field)
    for field in expected_data_fields:
        assert field in papers[0].data[0]
