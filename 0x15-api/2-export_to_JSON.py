#!/usr/bin/python3
""" export data in the JSON format from a API """
import json
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
    with open("{}.json".format(sys.argv[1]), "w") as jsonfile:
        json.dump({sys.argv[1]: [{
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": user['username']
        } for todo in todos]}, jsonfile)
