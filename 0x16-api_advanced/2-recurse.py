#!/usr/bin/python3
"""
Python script containing required function
"""
import requests


def recurse(subreddit, hot_list=[], aft=None):
    """
    Python recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit

    Endpoint:
    https://www.reddit.com/r/{subreddit}/hot.json

    Args:
        subreddit(`str`): Name of subreddit
        hot_list(`list`): List to be populated
        aft(`str`): Token for pagination. Initially None
    Return:
        List of posts else None if invalid subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-Agent': 'el-Ynot/1.0 (Linux)'}
    param = {'after': aft, 'limit': 100}

    r = requests.get(url, headers=header, allow_redirects=False, params=param)
    if r.status_code != 200:
        return None
    res_json = r.json()

    aft = res_json.get('data', {}).get('after')
    r_data_child = res_json.get('data', {}).get('children')
    if not r_data_child:
        r_data_child = []

    all_titl = list(map(lambda x: x.get('data', {}).get('title'),
                    r_data_child))
    hot_list.extend(all_titl)

    if aft is None:
        return hot_list
    return recurse(subreddit, hot_list, aft)
