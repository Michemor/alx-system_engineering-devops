#!/usr/bin/python3
"""
fetches data from a REST API
Manipulates the data for simple display to user
"""
import requests
from sys import argv


if __name__ == "__main__":
    employee_id = int(argv[1])

    # obtain users name
    user_dict = {'id': f'{employee_id}'}
    response = requests.get('https://jsonplaceholder.typicode.com/users',
                            params=user_dict)
    e_name = [name.get('name') for name in response.json()]

    # fetch the todo list
    # url for fetching to do list
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    req = requests.get(url)
    todos_json = req.json()

    done_tasks = []
    total_number_of_tasks = 0
    number_of_done_tasks = 0
    for todo in todos_json:
        if todo.get('completed') is True:
            done_tasks.append(todo.get('title'))
            number_of_done_tasks += 1
        total_number_of_tasks += 1

    print("Employee {} is done with tasks({}/{}):".format(
                                    ' '.join(e_name),
                                    number_of_done_tasks,
                                    total_number_of_tasks))

    for task in done_tasks:
        print(f"\t {task}")
