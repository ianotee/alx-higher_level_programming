#!/usr/bin/python3
"""

This functionis used in division.

"""


def matrix_divided(matrix, div):
    """This is the function that divides the entire block.

    Args:
        matrix: This is the list of the function.
        div: This is the number to be used in division.
    Raises:
        TypeError: The matrix.
        TypeError: The matrix rows.
        TypeError: Is an integer.
    Returns:
        This is a new matrix.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
