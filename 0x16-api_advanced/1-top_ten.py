#!/usr/bin/python3
"""
Python script containing required function
"""
import requests


def top_ten(subreddit):
    """
    Python function that queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit.

    Endpoint:
    https://www.reddit.com/r/{subreddit}/hot.json

    Args:
        subreddit(`str`): Name of subreddit
    Return:
        Top ten posts else None if invalid subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-Agent': 'el-Ynot/1.0 (Linux)'}
    param = {'limit': 10}

    r = requests.get(url, headers=header, allow_redirects=False, params=param)
    if r.status_code != 200:
        print(None)
        return
    res_json = r.json()

    r_data_child = res_json.get('data', {}).get('children')

    for child in r_data_child[0:10]:
        print(child.get('data', {}).get('title'))
