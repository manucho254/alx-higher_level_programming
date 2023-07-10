#!/usr/bin/python3

""" class that inherits from list
"""


class MyList(list):
    """ defines MyList and inherits from list
    """
    def print_sorted(self):
        """ print list sorted in ascending order
        """

        if any(not isinstance(x, int) for x in self):
            print(self)
            return

        arr = self.copy()
        arr.sort()
        print(arr)
