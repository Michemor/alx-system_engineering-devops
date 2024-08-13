#!/usr/bin/python3
"""
API MODULE: makes requests to Reddit and filters according to specifications
"""
from requests.exceptions import HTTPError
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

    search_reddit = f'https://www.reddit.com/r/{subreddit}/about.json'
    heads = {'User-Agent': '0-subs/1.0 (Python 3.10; Ubuntu 20.04)'}

    try:
        response = requests.get(search_reddit,
                                headers=heads,
                                allow_redirects=False)
        response.raise_for_status()
        result = response.json().get('data')
        print(result)
        return result.get('subscribers')
    except HTTPError as http_err:
        return 0
    except Exception as e:
        return 0
