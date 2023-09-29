#!/usr/bin/python3

"""
The function that prints the names.

"""


def say_my_name(first_name, last_name=""):
    '''This function prints name.

    Args:
        firstname (str):The first name.
        lastname (str):It will print the last name.

    Raises:
        TypeError: It prints the names.

    '''

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
