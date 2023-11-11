#!/usr/bin/python3
"""
Python script containing required function
"""
import requests


def print_keyword_count(hot_list, word_list):
    """
    Function to group and print keywords and their count

    Args:
        word_list: List of keywords to be counted
        hot_list(`list`): Populated list of titles
    """
    c_obj = {}
    l_wordlist = list(map(lambda x: x.lower(), word_list))

    for title in hot_list:
        l_title_list = title.lower().split()
        for word in l_wordlist:
            if word in l_title_list:
                c_obj[word] = c_obj.get(word, 0) + 1

    sortL = sorted(sorted(c_obj.items()), key=lambda x: x[1], reverse=True)
    for item in sortL:
        print('{}: {}'.format(*item))


def count_words(subreddit, word_list, hot_list=[], aft=None):
    """
    Python recursive function that queries the Reddit API, parses the title
    of all hot articles, and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces. Javascript should count as
    javascript, but java should not)

    Endpoint:
    https://www.reddit.com/r/{subreddit}/hot.json

    Args:
        subreddit(`str`): Name of subreddit
        word_list: List of keywords to be counted
        hot_list(`list`): Populated list of titles
        aft(`str`): Token for pagination. Initiaally None
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-Agent': 'el-Ynot/1.0 (Linux)'}
    param = {'after': aft}

    r = requests.get(url, headers=header, allow_redirects=False, params=param)
    if 'application/json' not in r.headers.get('Content-Type', ''):
        return
    res_json = r.json()

    aft = res_json.get('data', {}).get('after')
    r_data_child = res_json.get('data', {}).get('children')

    if not r_data_child:
        return None

    all_titl = list(map(lambda x: x.get('data', {}).get('title'),
                        r_data_child))
    hot_list.extend(all_titl)

    if aft is None:
        print_keyword_count(hot_list, word_list)
        return
    count_words(subreddit, word_list, hot_list, aft)
