#!/usr/bin/python3
""" Script that takes your GitHub credentials
    (username and password) and uses the GitHub API to display your id
"""
import requests
import sys


if __name__ == "__main__":
    args = sys.argv
    url = f"https://api.github.com/user"

    # create a session
    session = requests.Session()

    # set username and password
    session.auth = (args[1], args[2])

    # send request to get user data
    response = session.get(url, headers={})

    data = response.json()

    # print id
    print(data.get("id"))
