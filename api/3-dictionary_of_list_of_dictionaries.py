#!/usr/bin/python3
"""Exports all employees' TODO lists to a single JSON file."""
import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"

    users = requests.get(base_url + "users").json()
    todos = requests.get(base_url + "todos").json()

    data = {}
    for user in users:
        uid = user.get("id")
        data[str(uid)] = [{"username": user.get("username"),
                           "task": t.get("title"),
                           "completed": t.get("completed")}
                          for t in todos if t.get("userId") == uid]

    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)
