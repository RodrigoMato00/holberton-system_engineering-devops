#!/usr/bin/python3
"""
extend your Python script to export
data in the CSV format
"""


if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    req = requests.get("https://jsonplaceholder.typicode.com/users/" +
                       argv[1])
    dic = json.loads(req.text)
    name = dic.get('username')
    req = requests.get("https://jsonplaceholder.typicode.com/todos/" +
                       "?userId=" + argv[1])

    todos = json.loads(req.text)
    tasks = [task for task in todos]
    ar = {sys.argv[1]: []}

    for task in tasks:
        task_dict = {"task": task.get('title'), 'completed':
                     task.get('completed'), 'username': name}
        ans.get(sys.argv[1]).append(task_dict)
    with open(sys.argv[1] + ".json", "w") as file:
        json.dump(ar, file)
