#!/usr/bin/python3
"""Modulo say_my_name

This module defines a function that two string in specific format

Example:
    say_my_name = __import__('3-say_my_name').say_my_name
    say_my_name("John", "Smith")
"""


def say_my_name(first_name, last_name=""):
    """prints the first an last name as My name is first_name last_name
    and don't return anything

    Args:
        first_name (string): first text to be printed
        last_name (string): second text to be printed

    Returns:
        Don't return

    Raises:
        TypeError: when any argument is not a string
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")

    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
