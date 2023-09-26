#!/usr/bin/python3
"""The Square Class"""


class Square:
    """The square"""

    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError("size is integer")
        elif size < 0:
            raise ValueError("size >= 0")
        self.__size = size
