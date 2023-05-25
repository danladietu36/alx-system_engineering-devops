#!/usr/bin/python3
""" A script to access REST API for employee's todo list"""

import json
import requests
import sys


if __name__ == "__main__":
    employeeId = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = base_url + "/" + employeeId

    res = requests.get(url)
    username = res.json().get('username')

    todo_url = url + "/todos"
    tasks = requests.json().get('todo_url')


    dic = {employeeId: []}
    for task in tasks:
        dic[employeeId].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
            })
    with open("{}.json".format(employeeId), 'w') as file_name:
        json.dump(dic, file_name)
