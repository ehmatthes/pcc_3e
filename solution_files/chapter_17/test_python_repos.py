import pytest

from python_repos_tested import get_repos_info, get_response_dict, get_repo_dicts


# DEV: Do this once without fixtures, and once with fixtures.
#   Note that there are more advanced ways to do this making only one network call.

def test_response_status_code():
    """Test that a response has a successful status code."""
    r = get_repos_info()
    assert r.status_code == "200"

def test_response_dict():
    """Verify an appropriate number of repositories are represented,
    and the results are complete.
    """
    r = get_repos_info()
    response_dict = get_response_dict(r)

    total_count = response_dict['total_count']
    complete_results = not response_dict['incomplete_results']

    assert total_count > 240
    assert complete_results

def test_repo_dicts():
    """Verify the results in repo_dicts are correct."""
    r = get_repos_info()
    response_dict = get_response_dict(r)
    repo_dicts = get_repo_dicts(response_dict)

    assert len(repo_dicts) == 30

    # Check that all repos returned have over 10k stars.
    for repo_dict in repo_dicts:
        assert repo_dict['stargazers_count'] > 10_000