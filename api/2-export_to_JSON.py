#!/usr/bin/python3
"""Exports an employee's TODO list to a JSON file."""
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(base_url + "users/{}".format(user_id)).json()
    todos = requests.get(base_url + "todos",
                         params={"userId": user_id}).json()
    username = user.get("username")

    data = {user_id: [{"task": t.get("title"),
                       "completed": t.get("completed"),
                       "username": username} for t in todos]}

    with open("{}.json".format(user_id), "w") as f:
        json.dump(data, f)
