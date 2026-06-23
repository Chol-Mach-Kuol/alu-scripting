#!/usr/bin/python3
"""Module to query the Reddit API for top 10 hot posts."""
import requests


def top_ten(subreddit):
    """Print titles of the first 10 hot posts for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "MyBot/1.0 by Chol-Mach-Kuol"}
    response = requests.get(
        url,
        headers=headers,
        params={"limit": 10},
        allow_redirects=False
    )
    if response.status_code != 200:
        print("None")
        return
    try:
        posts = response.json().get("data", {}).get("children", [])
        for post in posts[:10]:
            print(post.get("data", {}).get("title"))
    except Exception:
        print("None")
