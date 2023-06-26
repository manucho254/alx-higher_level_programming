#!/usr/bin/python3

def safe_print_integer(value) -> bool:
    """ safe_print_integer - function that prints an integer.

        Args:
            value: value to print.

        Return:
            True if value is correctly printed else return False.
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        return False
