#!/usr/bin/python3
"""
fetches data from a REST API
Manipulates the data for simple display to user
"""
import requests
from sys import argv


if __name__ == "__main__":
    employee_id = argv[1]

    # url
    url = 'https://jsonplaceholder.typicode.com/'

    # obtain users name
    users = requests.get(url + f'users/{employee_id}').json()
    name = users.get('name')

    # fetch the todo list
    todos = requests.get(url + 'todos', params={'userId': employee_id}).json()

    done = [d.get('title') for d in todos if d.get('completed') is True]

    print(f"Employee {name} is done with tasks({len(done)}/{len(todos)}):")
    [print(f"\t {title}") for title in done]
