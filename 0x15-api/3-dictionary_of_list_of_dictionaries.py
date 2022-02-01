#!/usr/bin/python3
""" script to export data in the JSON format. """
import json
import requests
import sys

if __name__ == '__main__':
    users = requests.get(
        'https://jsonplaceholder.typicode.com/users', verify=False).json()
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos', verify=False).json()

    userdictionary = {}
    usernamedict = {}
    for user in users:
        uid = user.get("id")
        userdictionary[uid] = []
        usernamedict[uid] = user.get("username")

    for todo in todos:
        taskdictionary = {}
        uid = todo["userId"]
        taskdictionary["task"] = todo['title']
        taskdictionary["completed"] = todo['completed']
        taskdictionary["username"] = usernamedict[uid]
        userdictionary[uid].append(taskdictionary)
    with open("todo_all_employees.json", 'w') as jfle:
        json.dump(userdictionary, jfle)
