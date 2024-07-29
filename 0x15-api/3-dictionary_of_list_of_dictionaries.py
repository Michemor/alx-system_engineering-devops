#!/usr/bin/python3
""" Records all tasks from all employees into json """
import json
import requests


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    tasks = requests.get(url + "todos").json()

    employees_dict = {}

    for user in users:
        task_list = []
        for task in tasks:
            if user.get("id") == task.get("userId"):
                task_dict = {
                    "username": user.get("username"),
                    "task": task.get("title"),
                    "completed": task.get("completed")
                }
            task_list.append(task_dict)
        employees_dict[user.get("id")] = task_list

    with open("todo_all_employees.json", "w") as f:
        json.dump(employees_dict, f)
