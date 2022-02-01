#!/usr/bin/python3
"""
Using what you did in the task #0,
extend your Python script to export data in the CSV format.
Requirements:
Records all tasks that are owned by this employee
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv
"""

if __name__ == "__main__":
    import json
    import requests
    import sys

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
