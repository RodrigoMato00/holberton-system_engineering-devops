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

    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1])).json()
    todo = requests.get(url + "todos", params={"userId": argv[1]}).json()

    tasks = [task.get("title") for task in todo
             if task.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):"
          .format(user.get('name'), len(tasks), len(todo)))

    [print("\t {}".format(complete)) for complete in tasks]
