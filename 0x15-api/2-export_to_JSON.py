#!/usr/bin/python3
""" A script to access REST API for employee's todo list"""


import json
import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    rootUrl = "https://jsonplaceholder.typicode.com/users"
    url = rootUrl + "/" + employeeId

    response = requests.get(url)
    username = response.json().get('username')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    dictionary = {employeeId: []}
    for task in tasks:
        dictionary[employeeId].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })
    with open('{}.json'.format(employeeId), 'w') as filename:
        json.dump(dictionary, filename)
