#!/usr/bin/python3
"""

This function is used for indentation


"""


def text_indentation(text):
    '''The text is printed for the new line.

    Args:
        The text is the string to be printed.

    Raises:
        TypeError: Its not a string.

    '''

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    count = 0
    while count < len(text) and text[count] == " ":
        count = count + 1

    while count < len(text):
        print(text[count], end="")
        if text[count] == "\n" or text[count] in ".?:":
            if text[count] in ".?:":
                print("\n")
            count = count + 1
            while count < len(text) and text[count] == " ":
                count = count + 1
            continue
        count = count + 1
