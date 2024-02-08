#!/usr/bin/python3
"""defines a class square"""


class Square:
    """define the attributes of the square
    Attribute:
    size: size of a square"""

    def __init__(self, size):
        """
        creates a an instance of square

        Args:
        size: size of the square
        """
        self.__size = size
