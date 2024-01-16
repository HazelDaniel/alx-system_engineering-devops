#!/usr/bin/python3
"""This module queries the Reddit API and
    returns the number of subscribers of a given subreddit"""
import requests
import sys


def get_subreddit_subs(subreddit):
    """this gets the subscribers of a given subreddit"""
    headers = {"User-Agent": "0_subs/1.0"}

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=headers,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        exit(98)
    sub_count = get_subreddit_subs(sys.argv[1])
    print(sub_count)
