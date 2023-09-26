#!/usr/bin/python3
# 0-square.py 
"""A  square """


class Square:
    """A  square"""

    def __init__(self, size=0):
        """ The square
            size: This is the size.
            Error: size.
            Error: lower is zero.
        """

        if not isinstance(size, int):
            raise TypeError('size is integer')
        if size < 0:
            raise ValueError('size is  >= 0')

        self.__size = size

    def area(self):
        """
        Compute the  area
        Returns: The area
        """

        return (self.__size ** 2)
