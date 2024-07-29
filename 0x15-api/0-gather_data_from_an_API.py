#!/usr/bin/python3
"""
fetches data from a REST API
Manipulates the data for simple display to user
"""
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/users/"

    info = requests.get(url + f"{employee_id}").json()
    EMPLOYEE_NAME = info.get("name")

    tasks = requests.get(url + f"{employee_id}/todos").json()
    done = []
    undone = []
    for task in tasks:
        if task.get("completed") is True:
            done.append(task.get("title"))
        else:
            undone.append(task.get("title"))

    NUMBER_OF_DONE_TASKS = len(done)
    TOTAL_NUMBER_OF_TASKS = NUMBER_OF_DONE_TASKS + len(undone)

    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    [print(f"\t {TASK_TITLE}") for TASK_TITLE in done]
