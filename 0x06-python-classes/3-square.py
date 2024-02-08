#!/usr/bin/python3
"""defines a class square"""


class Square:
    """
    defines attributes of the square
    Attribute:
    size: size of the square
    """
    def __init__(self, size=0):
        """
        create an instance method ize.
        Args:
        size: size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        creates an instance method that returns the current
        square area.
        """
        return self.__size ** 2
