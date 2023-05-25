#!/usr/bin/python3
""" Using a REST API for todo lists of employees"""

import requests
import sys


if __name__ == '__main__':
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = base_url + "/" + employee_id

    response = requests.get(url)
    user_name = response.json().get('user_name')

    todo_url = url + "/todos"
    response = requests.get(todo_url)
    tasks = response.json()

    with open('{}.csv'.format(employee_id), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(employee_id, user_name, task.get('completed'),
                               task.get('title')))
