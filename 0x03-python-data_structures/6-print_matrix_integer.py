#!/usr/bin/python3

def print_matrix_integer(matrix: list = [[]]) -> None:
    """ function that print a matrix of integers

       Args:
           a two dimensional array of integers

       Return:
             None
    """
    if len(matrix) == 1 and len(matrix[0]) == 0:
        return
    for x in matrix:
        for j in range(len(x)):
            if j == len(x) - 1:
                print("{:d}".format(x[j]))
            else:
                print("{:d}".format(x[j]), end=" ")
