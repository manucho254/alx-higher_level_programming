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
    try:
        if len(args) == 0:
            res = fct()
            return res
        res = fct(args[0], args[1])
        return res
    except Exception as e:
        print(f"Exception: {e}", file=stderr)
        return None
