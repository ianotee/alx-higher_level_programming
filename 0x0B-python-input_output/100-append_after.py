#!/usr/bin/python3
"""Defines a text file insertion."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text a text.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
