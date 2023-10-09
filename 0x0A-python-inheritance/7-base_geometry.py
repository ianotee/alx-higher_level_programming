#!/usr/bin/python3
"""Defines a class"""


class BaseGeometry:
    """A class"""

    def area(self):
        """The method is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the integer
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
