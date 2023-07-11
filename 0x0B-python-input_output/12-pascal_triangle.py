#!/usr/bin/python3

""" module that returns a list of lists of integers,
    representing the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """ create pascal triangle
        Args:
            n: number to draw pascal triangle upto
        Return:
              list of list of integers
    """

    # n less or equal to zero return an empty list
    if n <= 0:
        return []

    triangle = []  # pascal triangle list
    for x in range(n):
        tmp = []
        if x == 0:
            tmp.append(1)
        elif x == 1:
            tmp = triangle[0].copy()
            tmp.append(1)
        else:
            prev = triangle[x - 1]
            for i in range(len(prev) - 1):
                two_sum = prev[i] + prev[i + 1]
                tmp.append(two_sum)
            tmp.insert(0, 1)
            tmp.append(1)
        triangle.append(tmp)

    return triangle
