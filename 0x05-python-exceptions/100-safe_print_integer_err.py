#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    """ function that prints an integer.
        Args:
            value: a n item to print

        Return:
            True if value has been correctly printed,
            (it means the value is an integer) Otherwise,
            returns False and prints in stderr the,
            error precede by Exception:
    """

    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print(f"Exception: {e}", file=stderr)
        return False
