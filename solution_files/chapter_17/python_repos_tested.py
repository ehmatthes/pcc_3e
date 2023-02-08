import requests

def get_repos_info():
    """Get information about Python repositories on GitHub."""
    # Make an API call and check the response.
    url = "https://api.github.com/search/repositories"
    url += "?q=language:python+sort:stars+stars:>10000"

    headers = {"Accept": "application/vnd.github.v3+json"}
    r = requests.get(url, headers=headers)

    print(f"Status code: {r.status_code}")

    return r

def get_response_dict(response):
    """Convert the response object to a dictionary."""
    response_dict = response.json()
    return response_dict

def show_repos_info(response_dict):
    """Show information about the returned repositories."""
    print(f"Total repositories: {response_dict['total_count']}")
    print(f"Complete results: {not response_dict['incomplete_results']}")

def get_repo_dicts(response_dict):
    """Return list of dictionaries, one for each repository."""
    repo_dicts = response_dict['items']
    return repo_dicts

def show_repo_dicts_info(repo_dicts):
    """Summarize information about repositories."""
    print(f"Repositories returned: {len(repo_dicts)}")

    print("\nSelected information about each repository:")
    for repo_dict in repo_dicts:
        print("\nSelected information about first repository:")
        print(f"Name: {repo_dict['name']}")
        print(f"Owner: {repo_dict['owner']['login']}")
        print(f"Stars: {repo_dict['stargazers_count']}")
        print(f"Repository: {repo_dict['html_url']}")
        print(f"Created: {repo_dict['created_at']}")
        print(f"Updated: {repo_dict['updated_at']}")
        print(f"Description: {repo_dict['description']}")

response = get_repos_info()
response_dict = get_response_dict(response)
show_repos_info(response_dict)
repo_dicts = get_repo_dicts(response_dict)
show_repo_dicts_info(repo_dicts)