#!/usr/bin/python3
"""
extend your Python script to
export data in the JSON format
"""


if __name__ == "__main__":
    import json
    import requests

    req = requests.get("https://jsonplaceholder.typicode.com/users")
    dic = json.loads(req.text)
    ar = {}

    for user in dic:
        name = user.get('username')
        user = str(user.get('id'))
        response = requests.get("https://jsonplaceholder.typicode.com/todos/" +
                                "?userId=" + user)

        todos = json.loads(response.text)
        tasks = [task for task in todos]
        ar[user] = []

        for task in tasks:
            task_dict = {"task": task.get('title'),
                         'completed': task.get('completed'),
                         'username': name}
            ar.get(user).append(task_dict)

    with open("todo_all_employees.json", "w") as file:
        json.dump(ar, file)
