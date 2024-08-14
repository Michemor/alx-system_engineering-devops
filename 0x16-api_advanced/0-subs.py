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

    The subreddit is passed as an argument to this function
    1. Checks if the subreddit is valid and proceeds otherwise
    the program returns 0.
    2. fetch the result and counts the number of subscribers
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    search_reddit = f"https://www.reddit.com/r/{subreddit}/about.json"
    heads = {"User-Agent": "0-subs/1.0 (Python 3.10; Ubuntu 20.04)"}

    try:
        response = requests.get(search_reddit,
                                headers=heads,
                                allow_redirects=False)
        result = response.json().get("data")
        return result.get("subscribers")
    except Exception as e:
        return 0
