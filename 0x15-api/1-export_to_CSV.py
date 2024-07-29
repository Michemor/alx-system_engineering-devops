#!/usr/bin/python3
"""
fetches data from a REST API
Manipulates the data for simple display to user
"""
import csv
import pandas as pd
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/users/"
    filename = f"{employee_id}.csv"
    info = requests.get(url + f"{employee_id}").json()
    name = info.get("username")
    tasks = requests.get(url + f"{employee_id}/todos").json()

    data = []

    for task in tasks:
        task_dict = {
            "id": f"{employee_id}",
            "name": f"{name}",
            "status": task.get("completed"),
            "title": task.get("title")
        }
        data.append(task_dict)

    keys = ["id", "name", "status", "title"]
    with open(filename, "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys,
                                quoting=csv.QUOTE_ALL)
        writer.writerows(data)
