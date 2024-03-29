#!/usr/bin/python3
"""defines a class Square"""


class Square:
    """
    defines the attributes of the square
    Attribute:
    size: size of the square
    """
    def __init__(self, size=0):
        """
        creates an instance of square.

        Args:
        size: size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
