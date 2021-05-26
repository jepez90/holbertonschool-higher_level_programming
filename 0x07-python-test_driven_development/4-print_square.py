#!/usr/bin/python3
"""Modulo print_square

This module defines a function that prints an squeare represented by #

Example:
    print_square = __import__('4-print_square').print_square
    print_square(4)
"""


def print_square(size):
    """prints an square of side size represented by # and doesn't retorn anything

    Args:
        size (int): the side of the square

    Returns:
        Doesn't return

    Raises:
        TypeError: when size is not a number
        ValueError: when size is less than 0
    """
    if (type(size) == float and size < 0) or type(size) != int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print('#' * size)
