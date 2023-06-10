#!/usr/bin/python3

def print_reversed_list_integer(my_list: list = []) -> None:
    """ function to print all intergers in a list in reverse

        Args:
            my_list: a list of integers

        Return:
              None
    """

    if len(my_list) == 0:
        print("None")

    for x in reversed(my_list):
        print("{:d}".format(x))
