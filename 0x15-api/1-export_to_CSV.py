#!/usr/bin/python3
""" Export data in the CSV format.. """
import json
import requests
import sys


if __name__ == "__main__":
    req = requests.get("https://jsonplaceholder.typicode.com/users/" +
                       sys.argv[1])
    dic = json.loads(req.text)
    username = dic.get('username')
    req = requests.get("https://jsonplaceholder.typicode.com/todos/" +
                       "?userId=" + sys.argv[1])

    todos = json.loads(req.text)
    tasks = [task for task in todos]

    with open(sys.argv[1] + ".csv", "w") as file:

        for task in tasks:
            data = ['"' + sys.argv[1] + '"', '"' +
                    username + '"', '"' +
                    str(task.get('completed')) + '"', '"' +
                    task.get('title') + '"']

            file.write(",".join(data) + '\n')
