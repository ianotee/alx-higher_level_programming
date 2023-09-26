#!/usr/bin/python3
# 0-square.py 
""" defines a square """


class Square:
    """A class of a square"""

    def __init__(self, size=0):
        """The Class
            size:  The square.
    
            Error: not an integer.
            Error:  The size is lower than zero.
        """

        if not isinstance(size, int):
            raise TypeError('Interger')
        if size < 0:
            raise ValueError('size >= 0')

        self.__size = size

    @property
    def size(self):
        """The size."""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('Integer')
        if value < 0:
            raise ValueError('size  >= 0')
        self.__size = value

    def area(self):
        """
        Compute the area
        Returns:The  size
        """

        return (self.__size ** 2)
