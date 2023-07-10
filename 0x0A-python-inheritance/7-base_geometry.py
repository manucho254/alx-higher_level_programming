#!/usr/bin/python3

""" class BaseGeometry
"""


class BaseGeometry:
    """ defines BaseGeometry class
    """

    def area(self):
        """ calculate area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validate values
            Args:
                name: arg name
                value: arg value
        """
        if not isinstance(value, int) or type(value) != int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
