#!/usr/bin/python3
""" A python script for a given employee ID, returns
info about their TODO list progress
"""

import requests
import sys


if __name__ == '__main__':
    user_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users/{}".format(user_id)).json()
    params = {"userId": "{}".format(user_id)}
    todos = requests.get(url + "todos", params=params).json()
    completed_tasks = list(filter(lambda todo: todo['completed'], todos))
    print("Employee {} is done with tasks ({}/{}):"
          .format(users.get('name', None), len(completed_tasks), len(todos)))
    [print("\t {}".format(task.get('title', None)))
     for task in completed_tasks]
