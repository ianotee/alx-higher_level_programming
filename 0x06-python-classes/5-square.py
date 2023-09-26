#!/usr/bin/python3
# 0-square.py 
""" that defines a square """


class Square:
    """A square"""

    def __init__(self, size=0):
        """Init this square class
        Args:
            size: size of the square defined
        Raises:
            TypeError:  size is not integer
            ValueError: size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """Returns  size of square"""

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
        Calculate area of a square
        Returns: The square of size
        """

        return (self.__size ** 2)

    def my_print(self):
        """print square in # """

        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)
