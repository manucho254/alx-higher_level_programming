#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    result = sum([int(x) for x in argv if x.isnumeric()])
    print("{:d}".format(result))
