#!/usr/bin/python3
""" string"""
import math


class MagicClass:
    """setup"""

    def __init__(self, radius=0):
        """  another string """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius  must be a number')
        self.__radius = radius

    def area(self):
        """string"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """ceircumference"""
        return 2 * math.pi * self.__radius
