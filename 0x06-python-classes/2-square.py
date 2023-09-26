#!/usr/bin/python3
""" a square """


class Square:
    """class of square"""

    def __init__(self, size=0):
        """ square class
    
           size - The size.
        
        Error: size is not integer
          Error:The  size is lower than zero.
        """

        if not isinstance(size, int):
            raise TypeError('size is an integer')
        if size < 0:
            raise ValueError('The size is >= 0')

        self.__size = size
