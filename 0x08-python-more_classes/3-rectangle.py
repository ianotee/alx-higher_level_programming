#!/usr/bin/python3
"""The rectangle."""


class Rectangle:
    """the class of rectangle."""

    def __init__(self, width=0, height=0):
        """
        Args:
            width: The width.
            height: The height.
        Raises:
            TypeError: integer
            ValueError: zero.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """The  width """
        return self.__width

    @width.setter
    def width(self, value):
        """ width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """The height """
        return self.__height

    @height.setter
    def height(self, value):
        """The height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """The Area."""
        return (self.__width * self.__height)

    def perimeter(self):
        """The perimeter."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self) -> str:
        """The diagram."""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                rectangle += "#"
            if column < self.__height - 1:
                rectangle += "\n"
        return (rectangle)
