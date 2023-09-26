#!/usr/bin/python3
# 0-square.py 
""" defines a square """


class Square:
    """A class of a square"""

    def __init__(self, size=0):
        """Initializing this square class
        Args:
            size:  the size of the square defined
        Raises:
            TypeError:  size is not integer
            ValueError:  size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """Takes size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calculate area of square
        Returns: Square size
        """

        return (self.__size ** 2)
