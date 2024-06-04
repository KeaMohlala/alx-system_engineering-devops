#!/usr/bin/python3
"""
script that queries REDDIT API for top 10 hot posts
of a given subreddit and prints the titles
"""
import requests


def top_ten(subreddit):
    """
    function that queries the REDDIT API for the top 10 posts in a given
    subreddit.

    Args: subreddit
    Return: prints title of posts or None if subreddit is not valid
    """
    base_url = "https://www.reddit.com"

    url = f"{base_url}/r/{subreddit}/hot.json?limit=10"

    headers = {
        "User-Agent": "MyCustomBot/0.1",
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return 0
        data = response.json()
        titles = [
             child['data']['title'] for child in data['data']['children']
        ]

        for title in titles:
            print(title)

    except Exception as e:
        print(None)
