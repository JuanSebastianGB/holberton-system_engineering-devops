#!/usr/bin/python3
""" export data in the CSV format from a API """
import csv
import requests
import sys

if __name__ == '__main__':
    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1]),
        verify=False).json()
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            sys.argv[1]),
        verify=False).json()
    complete = [task.get('title')
                for task in todos if task.get('completed')]
    with open('{}.csv'.format(sys.argv[1]), 'w', newline='')as csvf:
        writing = csv.writer(csvf, quoting=csv.QUOTE_ALL)
        [writing.writerow([sys.argv[1], user['username'],
                          todo['completed'], todo['title']]) for todo in todos]
