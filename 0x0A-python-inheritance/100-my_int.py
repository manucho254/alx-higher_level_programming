#!/usr/bin/python3

""" class MyInt that inherits from int
"""


class MyInt(int):
    """ class MyInt that inherits from int to do comparisons
    """

    def __init__(self, value):
        """ initialize MyInt class
        """
        self.value = value

    def __eq__(self, obj):
        """ check if two objects are not equal
            Args:
                 obj: object to check equality
            Return:
                  True if equal else False
        """
        return self.value != obj

    def __ne__(self, obj):
        """ check if two objects are equal
            Args:
                obj: object to check equality
            Return:
                   True if equal else False
        """
        return self.value == obj
