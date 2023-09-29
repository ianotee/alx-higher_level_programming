#!/usr/bin/python3
"""

The module has got one function.

"""


def add_integer(a, b=98):
    """This function returns the summation of integers.

    Args:
        a:The first arg
        b: The second arg

    Returns:
        This returns the sum.

    Raises:
        TypeError: None of the integer is a float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
