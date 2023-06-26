#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    """ function that executes a function safely.
       Args:
            fct: pointer to function
            args: function arguments

       Return:
             the result after invoking fct Otherwise,
             returns None if something happens during,
             the function and prints in stderr,
             the error precede by Exception:
    """
    res = None
    if len(args) == 0:
        return None
    try:
        res = fct(args[0], args[1])
    except Exception as e:
        print(f"Exception: {e}", file=stderr)

    return res
