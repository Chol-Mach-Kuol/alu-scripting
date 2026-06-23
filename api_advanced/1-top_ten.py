#!/usr/bin/python3
"""Module to query the Reddit API for top 10 hot posts."""
import requests


def top_ten(subreddit):
    """Print titles of the first 10 hot posts for a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:api_advanced:v1.0 (by /u/api_advanced)"}
    params = {"limit": 10}
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )
    if response.status_code != 200:
        print(None)
        return
    data = response.json().get("data")
    if data is None:
        print(None)
        return
    posts = data.get("children", [])
    for post in posts[:10]:
        print(post.get("data", {}).get("title"))
