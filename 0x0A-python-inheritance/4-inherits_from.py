#!/usr/bin/python3
"""looks for instance object.
"""


def inherits_from(obj, a_class):
    """Returns true if there is an instance object.
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
