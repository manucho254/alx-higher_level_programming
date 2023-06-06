#!/usr/bin/python3

"""
  remove_char_at - function to remove character from string
  @string: string to remove character
  @n: index of the string

  Return: new string without the removed character
"""


def remove_char_at(string: str, n: int) -> str:

    new = ""
    # check if the index is greater
    # the the length of the string
    if n > len(string) or n < 0:
        return string

    for x in string:
        if x != string[n]:
            new += x

    return new
