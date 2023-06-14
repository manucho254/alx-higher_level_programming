#!/usr/bin/python3

def weight_average(my_list: list = []):
    """ function that returns the weighted,
        average of all integers tuple

        Args:
            my_list: a list of tuples
            tuple (<score>, <weight>)

        Return:
            average of all integers tuple
    """

    if len(my_list) == 0:
        return 0

    sum_ = 0
    div_by = 0

    for x in my_list:
        score, weight = x
        sum_ += score * weight
        div_by += weight

    return sum_ / div_by
