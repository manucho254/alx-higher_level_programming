#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    length = len(argv) - 1
    if length == 1:
        print("{} argument:".format(length))
    if length == 0:
        print("{} arguments.".format(length))
    if length > 1:
        print("{} arguments:".format(length))

    if length > 1:
        for x in range(1, length + 1):
            print("{}: {}".format(x, argv[x]))
