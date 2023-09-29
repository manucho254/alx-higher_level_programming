#!/usr/bin/python3
""" Script that takes in a URL and an email,
    sends a POST request to the passed URL
    with the email as a parameter, and
    displays the body of the response (decoded in utf-8)
"""
from urllib.request import Request, urlopen
from urllib.parse import urlencode

import sys


if __name__ == "__main__":
    args = sys.argv

    data = {"email": args[2]}
    encoded_data = urlencode(data).encode("utf-8")

    url = Request(args[1], data=encoded_data)
    with urlopen(url) as response:
        page_obj = response.read()

        print(page_obj.decode())
