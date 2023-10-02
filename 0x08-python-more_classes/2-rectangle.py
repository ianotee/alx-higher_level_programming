#!/usr/bin/python3
"""The rectangle class."""


class Rectangle:
    """Its a rectangle."""

    def __init__(self, width=0, height=0):
        """
        Args:
            width:The width.
            height: The height.
        Raises:
            TypeError: The size is not an integer.
            ValueError: is zero.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """The width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Brings the width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Brings the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """This is the height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """The above method computes the area."""
        return (self.__width * self.__height)

    def perimeter(self):
        """The above method brings the perimeter."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
