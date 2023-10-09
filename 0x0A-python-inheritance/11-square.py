#!/usr/bin/python3
"""A  Rectangle subclass Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class of square."""

    def __init__(self, size):
        """Initialize a  square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
