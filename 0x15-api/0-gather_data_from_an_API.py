#!/usr/bin/env python3
"""
script that, using this REST API,
for a given employee ID,
returns information about
his/her TODO list progress
"""
import json
import requests
from sys import argv

if __name__ == '__main__':

    req = requests.get("https://jsonplaceholder.typicode.com/users/" +
                       argv[1])
    dic = json.loads(req.text)
    name = dic.get('name')
    req1 = requests.get("https://jsonplaceholder.typicode.com/todos/" +
                        "?userId=" + argv[1])

    todos = json.loads(req1.text)
    tasks = len(todos)
    done = [task for task in todos if task.get('completed')]
    tasks_done = len(done)
    print("Employee {} is done with tasks({}/{}):".
          format(name, tasks_done, tasks))

    for task in done:
        print("\t", task.get('title'))
