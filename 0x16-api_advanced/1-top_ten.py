#!/usr/bin/python3
"""This module queries the Reddit API and prints the
    titles of the first 10 hot posts listed for a given subreddit."""
import requests
import sys


def top_ten(subreddit):
    """this returns the first 10
        hot posts listed for a given sub-reddit"""
    headers = {"User-Agent": "1_top_ten/1.0"}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        if 'error' in data:
            print(None)
            return

        for post in data['data']['children'][:10]:
            print(post['data']['title'])
    else:
        print(f"request failed, server response: {response.status_code}")


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        exit(98)
    top_ten(sys.argv[1])
