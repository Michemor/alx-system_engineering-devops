#!/usr/bin/python3
"""
makes requests to Reddit API and filters
according to specifications
"""
import requests


def number_of_subscribers(subreddit):
    """
    queries the Reddit API and returns the number of
    subscribers for a given subreddit
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    heads = {"User-Agent": "0-subs/1.0 (Python 3.10; Ubuntu 20.04)"}

    try:
        response = requests.get(url,
                                headers=heads,
                                allow_redirects=False)
        result = response.json().get("data")
        return result.get("subscribers")
    except Exception as e:
        return 0
