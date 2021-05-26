#!/usr/bin/python3
"""Modulo matrix_divided

This module defines a function that divide all numbers of a matrix
by a gived number

Example:
    matrix_divided = __import__('2-matrix_divided').matrix_divided
    print(add_integer([[1, 2],[3, 4]], 2))
"""


def matrix_divided(matrix, div):
    """divide all values in a matrix by div, return the a new matrix

    Args:
        matrix [[]](int, float): list of lists of numbers
        div (int, float): second number to be add

    Returns:
        [[float]]: new matrix

    Raises:
        TypeError: when the first argument is not a list of list of numbers or
        div is not a number
        ZeroDivisionError: when second argument is 0
    """
    new_matrix = []
    type_error_msg = "matrix must be a matrix (list of lists) \
of integers/floats"

    if not matrix and type(matrix) != list or len(matrix) == 0:
        raise TypeError(type_error_msg)

    if not (type(div) == int or type(div) == float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        if type(row) != list:
            raise TypeError(type_error_msg)

        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []
        for data in row:
            if not (type(data) == int or type(data) == float):
                raise TypeError(type_error_msg)
            new_row.append(round(data/div, 2))
        new_matrix.append(new_row)

    return new_matrix
