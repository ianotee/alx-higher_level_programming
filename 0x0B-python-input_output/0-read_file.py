#!/usr/bin/python3
"""A text file-reading function"""


def read_file(filename=""):
    """Prints the contents of a UTF8"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
