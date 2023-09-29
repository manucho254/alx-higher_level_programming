#!/usr/bin/python3
""" Script to list 10 commits
    (from the most recent to oldest)
    of the repository “rails” by the user “rails”
"""
import requests
import sys


if __name__ == "__main__":
    args = sys.argv

    path = f"https://api.github.com/repos/"
    args = f"{args[2]}/{args[1]}/commits"
    url = path + args

    if len(args) > 3:
        # create a session
        session = requests.Session()

        # set username and password
        session.auth = (args[3], args[4])

        response = session.get(url, headers={})
    else:
        # send request to get commit data
        response = requests.get(url, headers={})

    data = response.json()[:10]

    for commit in data:
        full_name = commit.get('commit').get('author').get("name")
        print("{}: {}".format(commit.get("sha"), full_name))
