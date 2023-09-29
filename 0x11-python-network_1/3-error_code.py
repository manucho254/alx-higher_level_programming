#!/usr/bin/python3
""" Python script that takes in a URL,
    sends a request to the URL and
    displays the body of the response
    (decoded in utf-8).
"""
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

import sys


if __name__ == "__main__":
    args = sys.argv

    try:
        with urlopen(args[1]) as response:
            page_obj = response.read()

            print(page_obj.decode())
    except HTTPError as e:
        print("Error code: {}".format(e.code))
