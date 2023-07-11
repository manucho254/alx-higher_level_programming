#!/usr/bin/python3

""" module to read a text file
"""


def read_file(filename: str = "") -> None:
    with open(filename, "r") as f:
        print(f.read(), end="")
