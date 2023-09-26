#!/usr/bin/python3
"""my square"""


class Square:
    """ Square."""

    def __str__(self):
        """Square"""
        return self.pos_print()[:-1]

    def __init__(self, size=0, position=(0, 0)):
        """ initialize  square
        Args:
            size: square
            position:  square is (coordinates)
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ length of a side of square
        Raises:
            TypeError:  size is not an int.
            ValueError: size is < 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """  size of square
        Args:
            value: size
        Raises:
                TypeError: not int.
                ValueError: value is less that zero.
        """
        if not isinstance(value, int):
            raise TypeError('size')
        if value < 0:
            raise ValueError('size is  >= 0')
        self.__size = value

    @property
    def position(self):
        """ position of square
        Raises:
            TypeError: value != tuple of 2 ints >= 0.
        Returns:  position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ position
        Args:
            value: The
        Raises:
                TypeError: not tuple.
        Returns:  position
        """
        if not isinstance(value, tuple):
            raise TypeError(' A  tuple of two integers')
        if len(value) != 2:
            raise TypeError('A  tuple of two  integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError(' A  tuple of two integers')
        self.__position = value

    def area(self):
        """ area of square
        Returns:
            size *The  size
        """
        return self.__size * self.__size

    def pos_print(self):
        """ printed square with position"""
        pos = ""
        if not self.size:
            return "\n"
        for w in range(self.position[1]):
            pos += "\n"
        for w in range(self.size):
            for i in range(self.position[0]):
                pos += " "
            for j in range(self.size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """ square."""
        print(self.pos_print(), end="")
