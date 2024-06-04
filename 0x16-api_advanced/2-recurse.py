#!/usr/bin/python3
"""
script that queries REDDIT API for all hot articles
of a given subreddit and returns a list of their titles
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API for all hot articles in a
    given subreddit and returns a list of their titles.

    Args:
    subreddit: given subreddit
    host_list: empty list to append article titles to
    after: used to page through the listing

    Returns list of article titles or None if the subreddit is invalid.
    """
    base_url = "https://www.reddit.com"
    url = f"{base_url}/r/{subreddit}/hot.json?limit=100"

    headers = {"User-Agent": "MyCustomBot/0.1"}

    if after:
        url += f"&after={after}"

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return None

        data = response.json()

        # Extract titles from the current page
        titles = [
             child['data']['title'] for child in data['data']['children']
        ]
        hot_list.extend(titles)

        # Check if there's a next page
        if data['data']['after']:
            # Recursively call the function with the 'after' token
            return recurse(subreddit, hot_list, data['data']['after'])
        else:
            return hot_list

    except Exception as e:
        return None
