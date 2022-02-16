#!/usr/bin/python3
""" Passing params to print desiren hot posts """
import requests


def recurse(subreddit, hot_list=[], after=''):
    """ queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit """
    agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0)'
    agent += ' Gecko/20100101 Firefox/47.0'
    url = 'https://www.reddit.com/r/{}/hot/.json?after={}'\
        .format(
            subreddit, after)
    headers = {"user-Agent": agent}
    response = requests.get(
        url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None
    results = response.json().get('data')
    after = results.get('after')
    children = results.get('children')
    [hot_list.append(result.get('data').get('title')) for result in children]

    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list
