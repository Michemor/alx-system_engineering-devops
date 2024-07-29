#!/usr/bin/python3
""" exports data into csv format """
import csv
import requests
import sys


if __name__ == "__main__":
    user_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/users/"
    filename = f"{user_id}.csv"
    user = requests.get(url + f"{user_id}").json()
    tasks = requests.get(url + f"{user_id}/todos").json()

    task_list = []

    for task in tasks:
        task_dict = {
            "id": user.get("id"),
            "name": user.get("username"),
            "status": task.get("completed"),
            "title": task.get("title")
        }
        task_list.append(task_dict)

    keys = ["id", "name", "status", "title"]
    with open(filename, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys,
                                quoting=csv.QUOTE_ALL)
        writer.writerows(task_list)
