#!/usr/bin/python3

def safe_print_division(a: int, b: int):
    """ safe_print_division - function that divides 2,
        integers and prints the result.

        Args:
            a: integer a.
            b: integer b.

        Return:
            value of the division else None
    """

    res = None
    try:
        res = a / b

    except Exception as e:  # one common error here is zerodevision
        pass

    finally:
        print("Inside result: {}".format(res if res else None))

    return res
