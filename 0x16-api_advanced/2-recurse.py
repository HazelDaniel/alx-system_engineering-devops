#!/usr/bin/python3
"""this modules queries for a given subreddit and returns
    the title of all articles of that sub-reddit"""
import requests
import sys


def recurse(subreddit, hot_list=None, after=None):
    """this returns the title of all hot
        articles of a given subreddit"""
    headers = {"User-Agent": "2_recurse/1.0"}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        if 'error' in data:
            print(f"Subreddit '{subreddit}' not found.")
            return None

        if hot_list is None:
            hot_list = []

        for post in data['data']['children']:
            hot_list.append(post['data']['title'])

        if data['data']['after']:
            return recurse(subreddit, hot_list, after=data['data']['after'])
        else:
            return hot_list
    else:
        return None


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        exit(98)
    res = recurse(sys.argv[1])

    if res:
        for idx, title in enumerate(res, start=1):
            print(f"{idx}. {title}")
