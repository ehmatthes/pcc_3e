import pytest

from python_repos_tested import get_repos_info, get_response_dict, get_repo_dicts


@pytest.fixture
def response():
    """Get a response object."""
    r = get_repos_info()
    return r

def test_response_status_code(response):
    """Test that a response has a successful status code."""
    assert response.status_code == 200

def test_response_dict(response):
    """Verify an appropriate number of repositories are represented,
    and the results are complete.
    """
    response_dict = get_response_dict(response)

    total_count = response_dict['total_count']
    complete_results = not response_dict['incomplete_results']

    assert total_count > 240
    assert complete_results

def test_repo_dicts(response):
    """Verify the results in repo_dicts are correct."""
    response_dict = get_response_dict(response)
    repo_dicts = get_repo_dicts(response_dict)

    assert len(repo_dicts) == 30

    # Check that all repos returned have over 10k stars.
    for repo_dict in repo_dicts:
        assert repo_dict['stargazers_count'] > 10_000