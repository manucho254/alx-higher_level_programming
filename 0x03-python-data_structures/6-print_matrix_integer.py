#!/usr/bin/python3

def print_matrix_integer(matrix: list = [[]]) -> None:
    """ function that print a matrix of integers

       Args:
           a two dimensional array of integers

       Return:
             None
    """

    for x in matrix:
        if len(x) == 0:
            break
        for j in range(len(x)):
            if j == len(x) - 1:
                print("{:d}".format(x[j]))
            else:
                print("{:d}".format(x[j]), end=" ")
