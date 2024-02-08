#!/usr/bin/python3
"""defines a class square"""


class Square:
    """
    defines attributes of the square.
    Attribute:
    size: size of square
    """
    def __init__(self, size=0):
        """
        defines an instance size.
        Args:
        size: size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """
        Returns the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets value for size.
        Args:
        value: size of an integer
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        create an instance that returns the current
        square area
        """
        return self.__size ** 2
