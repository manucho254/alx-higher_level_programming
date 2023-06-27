#!/usr/bin/python3

"""class Square that defines a square

   Attributes:
            __size: Private instance attribute
"""


class Square:
    """class Square that defines a square.

       Attributes:
            __size: Private instance attribute
    """

    def __init__(self, size: int = 0) -> None:
        """ Initializes the instance based on size

            Desc:
                size must be an integer,
                otherwise raise a TypeError exception,
                with the message size must be an integer.

                if size is less than 0,
                raise a ValueError exception,
                with the message size must be >= 0.

            Args:
                size: The size of a square.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self) -> int:
        """ get the current square area.

            Return:
                  the current square area
        """
        return self.__size * self.__size

    @property
    def size(self) -> int:
        """ getter property, to get current size of square.
        """
        return self.__size

    @size.setter
    def size(self, value: int) -> None:
        """ setter method to set new values for __size.

            Args:
                new value for __size
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self) -> None:
        """ print in stdout the square with the character #

            Desc:
                if __size == 0 print empty line
        """
        if self.__size == 0:
            print("")
        area = self.area()  # area of the square
        while area != 0:
            for x in range(self.__size):
                print("#", end="")
            print("")
            area -= self.__size
