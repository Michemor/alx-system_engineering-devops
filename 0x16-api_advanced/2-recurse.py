#!/usr/bin/python3
"""
API for reddit
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    queries Reddit API
    Returns a list containing the titles of all hot articles

    Return: list of titles, return None
    Uses recursive function
    """

    if subreddit is None or not isinstance(subreddit, str):
        return None

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-agent": "2-recurse/1.0 (Python 3.4.3; Ubuntu 20.04)"}
    page_filter = {
        "after": after,
        "limit": 100,
        "count": count
    }

    try:
        response = requests.get(url,
                                headers=headers,
                                params=page_filter,
                                allow_redirects=False)
        data = response.json().get("data")
        after = data.get("after")
        count += data.get("dist")
        for child in data.get("children"):
            hot_list.append(child.get("data").get("title"))

        if after is not None:
            return recurse(subreddit, hot_list, after, count)

        return hot_list
    except Exception as e:
        return None
