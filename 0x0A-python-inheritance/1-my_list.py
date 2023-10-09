#!/usr/bin/python3
"""This is a module that will inherit from a list"""


class MyList(list):
    """Thisclass will inherit a list"""
    def print_sorted(self):
        """prints a list"""
        print(sorted(self))
