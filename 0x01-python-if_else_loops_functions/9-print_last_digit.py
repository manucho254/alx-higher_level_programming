#!/usr/bin/python3

"""
  print_last_digit - function to print last digit of a number
  @number: integer to get last digit
  Return: the last digit
"""


def print_last_digit(number: int) -> int:
    last_digit = (abs(number) % 10)

    print("{}".format(last_digit), end="")
    return last_digit
