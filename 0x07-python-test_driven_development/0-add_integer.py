#!/usr/bin/python3
"""Modulo add_integer

This module defines a basic function for add 2 numbers

Example:
    add_integer = __import__('0-add_integer').add_integer
    print(add_integer(1, 2))
"""


def add_integer(a, b=98):
    """Adds 2 numbers, return the add of the numbers a and b

    Args:
        a (int, float): first number to be add
        b (int, float): second number to be add

    Returns:
        int: the add of the two args

    Raises:
        TypeError: when a or b aren't integer or float
    """
    if not (type(a) == int or type(a) == float):
        raise TypeError("a must be an integer")

    if not (type(b) == int or type(b) == float):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
