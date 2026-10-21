#!/usr/bin/python3
"""Returns information about an employee's TODO list progress."""
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(base_url + "users/{}".format(user_id)).json()
    todos = requests.get(base_url + "todos",
                         params={"userId": user_id}).json()

    done = [t.get("title") for t in todos if t.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done), len(todos)))
    for title in done:
        print("\t {}".format(title))
