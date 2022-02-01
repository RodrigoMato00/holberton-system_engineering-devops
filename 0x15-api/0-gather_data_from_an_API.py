#!/usr/bin/python3
"""
script that, using this REST API,
for a given employee ID,
returns information about
his/her TODO list progress
"""

import requests
from sys import argv


if __name__ == "__main__":

    users = "https://jsonplaceholder.typicode.com/users"
    todos = "https://jsonplaceholder.typicode.com/todos"

    id = argv[1]
    request_u = requests.get(users, params={'id': id})
    request_t = requests.get(todos, params={'userId': id})

    tasks = request_t.json()
    all_tasks = []
    for task in tasks:
        if task.get("completed") is True:
            all_tasks.append(task)

    user = request_u.json()
    name = user[0].get("name")
    print("Employee {} is done with tasks({}/{}):".format(name, len(all_tasks), len(tasks)))

    for task in all_tasks:
        print("\t {}".format(task.get("title")))
