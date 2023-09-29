#!/usr/bin/python3
""" Script that fetches https://alx-intranet.hbtn.io/status
"""
from urllib.request import urlopen


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urlopen(url) as response:
        page_obj = response.read()

        print("Body response:")
        print("    - type: {}".format(type(page_obj)))
        print("    - content: {}".format(page_obj))
        content = str(page_obj).strip('b').strip("'")
        print("    - utf8 content: {}".format(content))
