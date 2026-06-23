#!/usr/bin/python3
"""Module to recursively count keywords in Reddit hot post titles."""
import requests


def count_words(subreddit, word_list, counts={}, after=None):
    """Print sorted keyword counts from all hot post titles recursively."""
    if not counts:
        counts = {w.lower(): 0 for w in word_list}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:api_advanced:v1.0 (by /u/api_advanced)"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )
    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    posts = data.get("children", [])

    for post in posts:
        title = post.get("data", {}).get("title", "").lower().split()
        for word in title:
            if word in counts:
                counts[word] += 1

    next_after = data.get("after")
    if next_after is None:
        results = sorted(
            [(k, v) for k, v in counts.items() if v > 0],
            key=lambda x: (-x[1], x[0])
        )
        for word, count in results:
            print("{}: {}".format(word, count))
        return

    return count_words(subreddit, word_list, counts, next_after)
