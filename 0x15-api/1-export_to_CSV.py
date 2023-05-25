#!/usr/bin/python3
""" Using a REST API for todo lists of employees"""
"""Accessing a REST API for todo lists of employees"""

import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    baseurl = "https://jsonplaceholder.typicode.com/users"
    url = baseurl + "/" + employeeId

    response = requests.get(url)
    username = response.json().get('username')

    todourl = url + "/todos"
    response = requests.get(todourl)
    tasks = response.json()

    with open('{}.csv'.format(employeeId), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(employeeId, username, task.get('completed'),
                               task.get('title')))
