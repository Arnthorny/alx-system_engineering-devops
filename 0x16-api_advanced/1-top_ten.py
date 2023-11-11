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

    r = requests.get(url, headers=header, allow_redirects=False)
    if 'application/json' not in r.headers.get('Content-Type', ''):
        print(None)
        return
    res_json = r.json()

    r_data_child = res_json.get('data', {}).get('children')
    if not r_data_child:
        print(None)
        return
    # Incase returned list has less than 10 posts
    num_to_print = min(10, len(r_data_child))

    for i in range(num_to_print):
        print(r_data_child[i].get('data', {}).get('title'))
