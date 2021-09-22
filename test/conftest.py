import pytest
import s2cholar


@pytest.fixture(scope='session')
def author_api():
    return s2cholar.AuthorApi(s2cholar.ApiClient())


@pytest.fixture(scope='session')
def paper_api():
    return s2cholar.PaperApi(s2cholar.ApiClient())
