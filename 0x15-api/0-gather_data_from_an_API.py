#!/usr/bin/python3
"""
script that, using this REST API,
for a given employee ID,
returns information about
his/her TODO list progress
"""

import sys
import requests


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/users/"
    user = requests.get(url + sys.argv[1]).json()
    todo = requests.get(url + sys.argv[1] + "/todos").json()

    tasks = []
    for task in todo:

        if task.get("completed") is True:
            tasks.append(task.get("title"))
    print("employee {} is done with tasks({}/{}):".format
          (user.get("name"), len(tasks), len(todo)))

    for task in tasks:
        print("\t {}".format(task))
