#!/usr/bin/python3
"""
Queries reddit API
"""
import requests


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts
    for a given reddit
    """

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "1-top_ten/1.0 (Python 3.4.3; Ubuntu 20.04)"}
    limit = {"limit": 10}

    try:
        response = requests.get(url,
                                headers=headers,
                                params=limit,
                                allow_redirects=False)
        children = response.json().get("data").get("children")

        for child in children:
            print(child.get("data").get("title"))
    except Exception as e:
        print("None")
