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
    username = info.get("name")

    tasks = requests.get(url + f"{employee_id}/todos").json()
    done = []
    undone = []
    for task in tasks:
        if task.get("completed") is True:
            done.append(task.get("title"))
        else:
            undone.append(task.get("title"))

    completed = len(done) + len(undone)

    print("Employee {} is done with tasks({}/{}):".format
                                        (username,
                                        len(done),
                                        completed))
    [print("\t {}".format(t)) for t in done]

