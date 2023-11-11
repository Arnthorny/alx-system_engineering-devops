#!/usr/bin/python3
"""
Python script containing required function
"""
import requests


def number_of_subscribers(subreddit):
    """
    Python function to query the Reddit API and return the num of subscribers
    (not active users, total subscribers) for a given subreddit

    Endpoint:
    https://www.reddit.com/r/{}/about.json

    Args:
        subreddit(`str`): Name of subreddit
    Return:
        Number of subscribers else 0 if invalid subreddit.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'User-Agent': 'el-Ynot/1.0 (Linux)'}

    r = requests.get(url, headers=header)
    if 'application/json' not in r.headers.get('Content-Type', ''):
        return 0
    res_json = r.json()
    res_json_data = res_json.get('data')
    return 0 if not res_json_data else res_json_data.get('subscribers')
