#!/usr/bin/python3
""" Script to list 10 commits
    (from the most recent to oldest)
    of the repository “rails” by the user “rails”
"""
import requests
import sys


if __name__ == "__main__":
    args = sys.argv
    url = f"https://api.github.com/repos/\
            {args[2]}/{args[1]}/commits?per_page=10"

    # send request to get commit data
    response = requests.get(url, headers={})

    data = response.json()

    for commit in data:
        user_name = commit.get('author').get('login')
        url = f"https://api.github.com/users/{user_name}"
        user = requests.get(url)
        user_data = user.json()

        print(commit.get("sha"), user_data.get("name"))
