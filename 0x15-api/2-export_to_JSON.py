#!/usr/bin/python3
""" exports data into csv format """
import csv
import json
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/users/"
    filename = f"{employee_id}.json"
    user = requests.get(url + f"{employee_id}").json()
    tasks = requests.get(url + f"{employee_id}/todos").json()

    data = []

    for task in tasks:
        task_dict = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")
        }
        data.append(task_dict)

    data_dict = {f"{employee_id}": data}

    with open(filename, "w") as json_file:
        json.dump(data_dict, json_file)
