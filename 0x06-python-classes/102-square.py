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

    def __eq__(self, square) -> bool:
        """ Check if if two Square objects are equal.

            Args:
                square: Sqaure object
        """
        return self.__size == square.size

    def _ne__(self, square) -> bool:
        """ Check if two Square objects are not equal
            Args:
                 square: Square object.
        """
        return self.__size != square.size

    def __gt__(self, square) -> bool:
        """ Check if one Square object is greater than the other
            Args:
                square: Square object.
        """
        return self.__size > square.size

    def __ge__(self, square) -> bool:
        """ Check if one Square object is greater than or equal to the other
            Args:
                square: Square object
        """
        return self.__size >= square.size

    def __lt__(self, square) -> bool:
        """ nethod to check if one Square object is less than the other
            Args:
                square: Square object
        """
        return self.__size < square.size

    def __le__(self, square) -> bool:
        """ Check if one Square object is less than or equal to the other
            Args:
                square: Square object.
        """
        return self.__size <= square.size
