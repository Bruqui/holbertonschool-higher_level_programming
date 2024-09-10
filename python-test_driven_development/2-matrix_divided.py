#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix
by a given divisor.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix: A list of lists of integers or floats.
        div: The divisor, which must be a number (integer or float).

    Returns:
        A new matrix with all elements divided by div, rounded to 2 decimal
        places.

    Raises:
        TypeError: If the matrix elements are not lists of integers or floats.
        TypeError: If each row of the matrix is not of the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is zero.
    """

    if (not isinstance(matrix, list) or not all(isinstance(row, list)
                                                for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(isinstance(elem, (int, float)) for row in matrix
               for elem in row):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
