#!/usr/bin/python3
""" queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit. """

import requests


def number_of_subscribers(subreddit):
    """ Retuns the number subscribers """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0)'
    agent += ' Gecko/20100101 Firefox/47.0'
    headers = {
        "user_Agent": agent}
    response = requests.get(url, headers=headers, allow_redirects=False)
    return 0 if response.status_code != 200 else response.json()\
        .get('data')\
        .get('subscribers')
