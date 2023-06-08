#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    idx = 0
    result = 0
    for x in argv:
        if idx > 0:
            result += int(x)
        idx += 1
    print("{:d}".format(result))
