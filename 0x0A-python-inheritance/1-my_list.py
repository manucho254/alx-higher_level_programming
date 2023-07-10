#!/usr/bin/python3

""" class that inherits from list
"""


class MyList(list):
    """ defines MyList and inherits from list
    """
    def print_sorted(self):
        """ print list sorted in ascending order
        """

        arr = self.copy()
        arr.sort()
        print(arr)
