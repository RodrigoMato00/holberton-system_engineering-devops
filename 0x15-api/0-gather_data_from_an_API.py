#!/usr/bin/python3
"""
script that, using this REST API,
for a given employee ID,
returns information about
his/her TODO list progress
"""
import requests
from sys import argv

if __name__ == '__main__':

    if len(argv) == 2 and argv[1].isdigit():
        url = 'https://jsonplaceholder.typicode.com/'
        user = requests.get(url+'users/{}'.format(argv[1])).json()["name"]
        request = requests.get(url+'todos?userId={}'.format(argv[1]))

        dic = request.json()
        number = 0
        t_name = ""

        for task in dic:
            if task['completed'] is True:
                number += 1
                t_name += "\t " + task["title"] + '\n'
        print("Employee {} is done with tasks({}/20):".format(user, number))
        print(t_name, end="")
