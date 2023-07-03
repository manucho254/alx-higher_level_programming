#!/usr/bin/python3

""" divide all elements of a matrix.
    Args:
         matrix: lists of lists of integers/floats
         div: value of the divide with
"""


def matrix_divided(matrix, div):
    """ Return:
              a new matrix
    """
    new = []

    if not isinstance(matrix, list) or len(matrix) == 0:
        message = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(message)

    sizes = {len(x) for x in matrix}  # creates a set

    # if all row in matrix are the same size the set should have only one item
    if len(sizes) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    # check if div value is not a float or an int
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    # check if div value is equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for j in matrix:
        tmp = []
        for i in j:
            tmp.append(round(i / div, 2))
        new.append(tmp)

    return new
