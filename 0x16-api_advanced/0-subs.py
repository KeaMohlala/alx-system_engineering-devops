#!/usr/bin/python3
"""
script that queries REDDIT API and returns number of subscribers
for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    function that queries the REDDIT API and returns the number of
    subscribers for a given subreddit

    Args: subreddit
    Return: number of subscribers for subreddit or 0 if
    subreddit is not valid
    """
    base_url = "https://www.reddit.com"

    url = f"{base_url}/r/{subreddit}/about.json"

    headers = {
        "User-Agent": "MyRedditApp/0.1",
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return 0
        data = response.json()
        subscriber_count = data.get("data", {}).get("subscribers", 0)
        return subscriber_count

    except Exception as e:
        return 0
