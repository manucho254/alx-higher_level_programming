#!/usr/bin/python3

""" class Rectangle that defines a rectangle
    Attributes:
              number_of_instances: hold value for number of instances created
              print_symbol": symbol to print rectangle with
"""


class Rectangle:
    """ class Rectangle
        Attributes:
                  number_of_instances: hold value for number of instances created
                  print_symbol: symbol to print rectangle with
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ initialize class
            Args:
                width: width of a rectangle
                height: height of a rectangle
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """ getter to get width of a rectangle
            Return:
                   width of a rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter to set new width of a rectangle
            Args:
                value: new width ofa rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter to get height of a rectangle
            Return:
                   height of a rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter to set new height of a rectangle
            Args:
                value: new height of rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ get area of a rectangle
            Return:
                   the area of a rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """ get perimeter of a rectangle
            Return:
                   the perimeter of a rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0

        return (self.__height * 2) + (self.__width * 2)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ compare two Rectangle objects
            Args:
                 rect_1: object Rectangle one
                 rect_2: object Rectangle two
            Return:
                   biggest rectangle based on square.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1

        return rect_2

    @classmethod
    def square(cls, size=0):
        """ create a new Rectangle instance
            Args:
                size: new size of width and height
        """
        return cls(width=size, height=size)

    def __str__(self):
        """ print rectangle
            Return:
                  ngle.pyation of a circle
        """
        if self.__height == 0 or self.__width == 0:
            return ""

        arr = []
        if self.print_symbol:
            for x in range(self.__height):
                tmp = (self.print_symbol * self.__width)
                arr.append(f"{tmp}")
                if x != self.__height - 1:
                    arr.append("\n")

        return "".join(arr)

    def __repr__(self):
        """ return a string representation of the rectangle
            Return:
                  string representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ distructor function called,
            when instance is about to be destroyed
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
