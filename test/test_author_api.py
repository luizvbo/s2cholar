# coding: utf-8

"""
    Literature Graph Service

    Fetch paper and author data from the Semantic Scholar corpus

"""
AUTHOR_ID = '145872832'

def test_get_author(author_api):
    """Test case for get_graph_get_author

    Details about an author
    """
    expected_fields = [
        'author_id', 'external_ids', 'url', 'name', 'aliases', 'affiliations',
        'homepage', 'papers'
    ]
    author = author_api.get_author(AUTHOR_ID)
    assert author[1] == 200
    for field in expected_fields:
        assert hasattr(author[0], field)


def test_get_author_papers(author_api):
    """Test case for get_graph_get_author_papers

    Details about an author's papers
    """
    expected_fields = ['data', 'next', 'offset']
    expected_data_fields = [
        'paperId', 'externalIds', 'url', 'title', 'abstract', 'venue', 'year',
        'referenceCount', 'citationCount', 'influentialCitationCount',
        'isOpenAccess', 'fieldsOfStudy', 'authors', 'citations', 'references'
    ]
    author = author_api.get_author_papers(AUTHOR_ID)
    assert author[1] == 200
    for field in expected_fields:
        assert hasattr(author[0], field)
    for field in expected_data_fields:
        assert field in author[0].data[0]
