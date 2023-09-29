#!/usr/bin/python3
""" script that takes in a URL,
    sends a request to the URL and
    displays the value of the X-Request-Id
    variable found in the header of the response.
"""
from urllib.request import urlopen
import sys


if __name__ == "__main__":
    args = sys.argv
    with urlopen(args[1]) as response:
        page_obj = response.read()

        print(response.headers.get("X-Request-Id"))
