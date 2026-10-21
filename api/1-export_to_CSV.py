#!/usr/bin/python3
"""Exports an employee's TODO list to a CSV file."""
import csv
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(base_url + "users/{}".format(user_id)).json()
    todos = requests.get(base_url + "todos",
                         params={"userId": user_id}).json()
    username = user.get("username")

    with open("{}.csv".format(user_id), "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for t in todos:
            writer.writerow([user_id, username,
                             t.get("completed"), t.get("title")])
