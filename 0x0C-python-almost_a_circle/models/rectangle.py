#!/usr/bin/python3

""" class Rectangle that inherits from base.
"""
from models.base import Base


class Rectangle(Base):
    """ class Rectangle that defines a rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize class Rectangle
            Args:
                 width: width of a rectangle
                 height: height of a rectangle
                 x: xaxis position
                 y: yaxis position
                 id: Object id
        """
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError(f"width must be an integer")
        if width < 1:
            raise ValueError(f"width must be > 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError(f"height must be an integer")
        if height < 1:
            raise ValueError(f"height must be > 0")
        self.__height = height
        if not isinstance(x, int):
            raise TypeError(f"x must be an integer")
        if x < 0:
            raise ValueError(f"x must be >= 0")
        self.__x = x
        if not isinstance(y, int):
            raise TypeError(f"y must be an integer")
        if y < 0:
            raise ValueError(f"y must be >= 0")
        self.__y = y

    @property
    def width(self):
        """ get the width of the rectangle.
            Return:
                  width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, width):
        """ update the width of the rectangle
            Args:
                width: new rectangle width
        """
        if not isinstance(width, int):
            raise TypeError(f"width must be an integer")
        if width < 1:
            raise ValueError(f"width must be > 0")

        self.__width = width

    @property
    def height(self):
        """ get the height of the rectangle
            Return:
                   height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, height):
        """ update the height of a rectangle.
            Args:
                height: height of a rectangle
        """
        if not isinstance(height, int):
            raise TypeError(f"height must be an integer")
        if height < 1:
            raise ValueError(f"height must be > 0")

        self.__height = height

    @property
    def x(self):
        """ get the value of x
            Return:
                  xaxis position.
        """
        return self.__x

    @x.setter
    def x(self, x=0):
        """ update x value
            Args:
                x: new xaxis value of rectangle
        """
        if not isinstance(x, int):
            raise TypeError(f"x must be an integer")
        if x < 0:
            raise ValueError(f"x must be >= 0")

        self.__x = x

    @property
    def y(self):
        """ get value of y
            Return:
                  yaxis position
        """

        return self.__y

    @y.setter
    def y(self, y=0):
        """ update y value
            Args:
                y: new yaxis value of rectangle
        """
        if not isinstance(y, int):
            raise TypeError(f"y must be an integer")
        if y < 0:
            raise ValueError(f"y must be >= 0")

        self.__y = y

    def area(self):
        """ get area of a rectangle
            Return:
                  area of a rectangle
        """
        return self.__width * self.height

    def display(self):
        """ print rectangle instance using character #
        """
        for x in range(self.__height):
            if self.__y >= 0:
                print("\n" * self.__y, end="")
                self.__y = 0
            if self.__x >= 0:
                print(" " * self.__x, end="")
            for _ in range(self.__width):
                print("#", end="")
            print("")

    def update(self, *args, **kwargs):
        """ assign arguments to attributes
            Args:
                args: an array of arguments.
                kwargs: dict of key word arguments.
            Desc:
                1st argument should be the id attribute
                2nd argument should be the width attribute
                3rd argument should be the height attribute
                4th argument should be the x attribute
                5th argument should be the y attribute
        """

        length_args = len(args)  # length of args

        if length_args > 0:
            for x in range(length_args):
                if x == 0:
                    self.id = args[x]
                if x == 1:
                    self.width = args[x]
                if x == 2:
                    self.height = args[x]
                if x == 3:
                    self.x = args[x]
                if x == 4:
                    self.y = args[x]
        else:
            if kwargs.get("id"):
                self.id = kwargs.get("id")
            if kwargs.get("width"):
                self.width = kwargs.get("width")
            if kwargs.get("height"):
                self.height = kwargs.get("height")
            if kwargs.get("x"):
                self.x = kwargs.get("x")
            if kwargs.get("y"):
                self.y = kwargs.get("y")

    def to_dictionary(self):
        """ get dictionary representation of Rectangle.
            Return:
                  a dictionary representation of Rectangle.
        """
        new_dict = {"x": self.id, "y": self.y, "id": self.id}
        new_dict.update({"height": self.height, "width": self.width})

        return new_dict

    def __str__(self):
        """ Represent Rectangle instance as a string
            Return:
                  string representation of Rectangle
        """
        dimension = f"{self.__width}/{self.__height}"
        position = f"{self.__x}/{self.__y}"
        message = f"[Rectangle] ({self.id}) {position} - {dimension}"

        return message
