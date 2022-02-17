#!/usr/bin/python3
""" Getting count of given keywords """
import requests


def count_words(subreddit, word_list, after='', dictionary={}):
    """ prints a sorted count of given keywords
    (case-insensitive, delimited by spaces """

    word_list = list(set(word_list))

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
    for result in children:
        title = result['data']['title'].lower().split()
        processWords(title, word_list, dictionary)

    if after:
        return count_words(subreddit, word_list, after, dictionary)
    if len(dictionary) == 0:
        print('')
        return
    dictionary = dict(
        sorted(dictionary.items(), key=lambda _k: (-_k[1], _k[0])))
    [print('{}: {}'.format(key, value))
     for key, value in dictionary.items() if value != 0]


def processWords(title, word_list, dictionary):
    """ Processing words to save the count in the dictionary """
    for word in word_list:
        numberOfMatches = len(list(filter(lambda x: x == word.lower(), title)))

        if word not in dictionary.keys():
            dictionary[word] = numberOfMatches
            continue
        dictionary[word] += numberOfMatches
