#!/usr/bin/python3

def square_matrix_simple(matrix: list = []) -> list:
    """ function that computes the square,
       value of all integers of a matrix

       Args:
           matrix: an array of lists

       Return: new matrix
    """
    if len(matrix) == 1 and len(matrix[0]) == 0:
        return matrix

    new = list(map(lambda x: list(map(lambda i: i * i, x)), matrix))

    return new
