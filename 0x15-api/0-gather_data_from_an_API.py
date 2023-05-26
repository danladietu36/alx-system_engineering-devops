#!/usr/bin/python3
"""
A script that uses 'https://jsonplaceholder.typicode.com/todos/1'
RESTFUL API for a given employee ID, and returns information
about his/her TODO list progress
"""
import requests
import sys


if __name__ == "__main__":
    employeeId = sys.argv[1]
    root_url = "https://jsonplaceholder.typicode.com/users"
    url = root_url + "/" + employeeId

    response = requests.get(url)
    employee_name = response.json().get('name')

    todo_url = url + "/todos"
    response = requests.get(todo_url)
    tasks = response.json()
    done = 0
    tasks_done = []

    for task in tasks:
        if task.get('completed'):
            tasks_done.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, done, len(tasks)))

    for task in tasks_done:
        print("\t {}".format(task.get('title')))
