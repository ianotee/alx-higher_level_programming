#!/usr/bin/python3
"""This is a locked class"""


class LockedClass:
    """
    Only allows instatiation of attribute  first_name
    """

    __slots__ = ["first_name"]
