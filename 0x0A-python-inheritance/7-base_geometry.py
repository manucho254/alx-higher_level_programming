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
        val_type = type(value)
        is_instance = isinstance(value, int)
        is_subclass = issubclass(val_type, int)
        if not is_instance or val_type != int or not is_subclass:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
