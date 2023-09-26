#!/usr/bin/python3
"""Square"""


class Square:
    """ square"""

    def __init__(self, size=0):
        """Build a  Square
        Args: size: length of a side Square
        """
        self.__size = size

    @property
    def size(self):
        """" size as length of a side Square
        Raises:
            TypeError:  size != int
            ValueErrorr: size < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """ area of a Square
        Returns:  size squared
        """
        return self.__size * self.__size

    def __le__(self, other):
        return self.area() <= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __eq__(self, other):
        return self.area() == other.area()
