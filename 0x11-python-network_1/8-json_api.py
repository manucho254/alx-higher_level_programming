#!/usr/bin/python3
""" Script that takes in a URL,
    sends a request to the URL
    and displays the body of the response.
"""
import requests
import sys


if __name__ == "__main__":
    args = sys.argv

    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data={"q": args[1]})

    data = response.json()

    if not isinstance(data, dict):
        print("Not a valid JSON")
    elif isinstance(data, dict) and len(data) > 0:
        print("[{}] {}".format(data.get('id'), data.get('name')))
    else:
        print("No result")
