#!/usr/bin/python3

islower = __import__('7-islower').islower


"""
  uppercase - function to convert all lowercase letters in,
  string to uppercse
  @string: the string to convert character from
"""


def uppercase(string: str) -> None:
    for x in string:
        ch = x
        if islower(ch):
            ch = chr(ord(x) - 32)
        print("{}".format(ch), end="")
    print()
