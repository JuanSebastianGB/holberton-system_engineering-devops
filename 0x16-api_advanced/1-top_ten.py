#!/usr/bin/python3
""" Passing params to print desiren hot posts """
import requests


def top_ten(subreddit):
    """ queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit. """
    agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0)'
    agent += ' Gecko/20100101 Firefox/47.0'
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {"user-Agent": agent}
    params = {"limit": 10}
    response = requests.get(
        url, params=params, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    results = response.json().get('data').get('children')
    [print(result.get('data').get('title')) for result in results]
