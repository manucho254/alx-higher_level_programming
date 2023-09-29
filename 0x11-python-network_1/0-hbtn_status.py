#!/usr/bin/python3
""" Script that fetches https://alx-intranet.hbtn.io/status
"""
from urllib.request import urlopen


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urlopen(url) as response:
        page_obj = response.read()

        print("Body response:")
        print("\t- type: {}".format(type(page_obj)))
        print("\t- content: {}".format(page_obj))
        print("\t- utf8 content: {}".format(page_obj.decode("utf-8")))
