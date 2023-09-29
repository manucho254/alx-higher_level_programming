#!/usr/bin/python3
""" Script that takes in a URL,
    sends a request to the URL
    and displays the body of the response.
"""
import requests
import sys


if __name__ == "__main__":
    args = sys.argv
    response = requests.get(args[1])

    status_code = response.status_code
    if status_code >= 400:
        print("Error code: {}".format(status_code))
    else:
        print(response.text)
