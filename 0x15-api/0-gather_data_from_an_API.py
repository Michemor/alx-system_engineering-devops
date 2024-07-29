#!/usr/bin/python3
"""
fetches data from a REST API
Manipulates the data for simple display to user
"""
import requests
import sys


def fetch_data(user_id):
    """ fetches data from API and displays employee tasks """

    users = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"

    user_resp = requests.get(users).json()
    name = user_resp.get("name")

    todo_resp = requests.get(todos).json()
    total = 0
    done = []
    for todo in todo_resp:
        if todo.get("completed") is True:
            done.append(todo.get("title"))
        total += 1
    
    count_done = len(done)
    print(f"Employee {name} is done with tasks({count_done}/{total}):")
    [print(f"\t {d}") for d in done]


if __name__ == "__main__":
    fetch_data(int(sys.argv[1]))
