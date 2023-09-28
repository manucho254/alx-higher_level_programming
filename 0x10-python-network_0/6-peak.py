#!/usr/bin/python3
""" module to find peak in a list
"""


def find_peak(list_of_integers: list) -> int:
    """ find peak in a list
        Args:
            list_of_integers: an list_of_integers of lists
    """
    # base case
    if list_of_integers is None or len(list_of_integers) == 0:
        return None

    length = len(list_of_integers)

    left = 0
    right = length - 1

    while (right <= right):
        # finding mid by binary right shifting.
        mid = (left + right) >> 1

        # first case if mid is the answer
        less_equal_right = list_of_integers[mid - 1] <= list_of_integers[mid]
        less_equal_left = list_of_integers[mid + 1] <= list_of_integers[mid]
        if ((mid == 0 or less_equal_right) and
                (mid == length - 1 or less_equal_left)):
            break

        # move the right pointer
        if (mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]):
            right = mid - 1

        # move the left pointer
        else:
            left = mid + 1

    return list_of_integers[mid]
