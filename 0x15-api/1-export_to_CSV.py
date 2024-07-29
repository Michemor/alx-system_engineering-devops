#!/usr/bin/python3
""" exports data into csv format """
import csv
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/users/"
    filename = f"{employee_id}.csv"
    user = requests.get(url + f"{employee_id}").json()
    tasks = requests.get(url + f"{employee_id}/todos").json()

    data = []

    for task in tasks:
        task_dict = {
            "id": user.get("id"),
            "name": user.get("username"),
            "status": task.get("completed"),
            "title": task.get("title")
        }
        data.append(task_dict)

    keys = ["id", "name", "status", "title"]
    with open(filename, "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys,
                                quoting=csv.QUOTE_ALL)
        writer.writerows(data)
