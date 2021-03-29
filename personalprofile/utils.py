import json

import requests


def get_github_profile(username=""):
    """A helper utility to get more info from GitHub after SSO login.

    Args:
        A string argument representing the GitHub username.

    Returns:
        A JSON text representing the user based on their GitHub profile.

    """

    try:
        url = f"https://api.github.com/users/{username}"
        response = requests.get(url)
        return json.loads(response.text)
    except Exception as e:
        return e
