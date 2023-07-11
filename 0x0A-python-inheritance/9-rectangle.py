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
        if val_type != int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")


""" class Rectangle
"""


class Rectangle(BaseGeometry):
    """ class Rectangle that defines a rectangle
        Attributes:
                   width: width of rectangle
                   height: height of rectangle
    """

    def __init__(self, width, height):
        """ initialize class
            Args:
                width: width of rectangle
                height: height of rectangle
        """
        super().__init__()
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ calculate area of a rectangle
            Return:
                  area of a rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """ represent object as a string
            Return:
                  string representation of Rectangle
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
