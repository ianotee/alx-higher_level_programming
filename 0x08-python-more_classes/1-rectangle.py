#!/usr/bin/python3
"""The rectangle class."""


class Rectangle:
    """This the class rectangle."""

    def __init__(self, width=0, height=0):
        """The class init
        Args:
            width: This is the width of the rectangle.
            height: This is the height of the rectangle.
        Raises:
            TypeError: This is not an integer data type.
            ValueError: The size is zero.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Brings  width"""
        return self.__width

    @width.setter
    def width(self, value):
        """The  width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Brings  height """
        return self.__height

    @height.setter
    def height(self, value):
        """The  height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
