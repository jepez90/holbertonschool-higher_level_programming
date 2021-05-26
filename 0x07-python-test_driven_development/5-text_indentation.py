#!/usr/bin/python3
"""Modulo text_indentation

This module defines a function that prints a given text after replace
all symbols . : and ? for two new lines

Example:
    print_square = __import__('4-print_square').print_square
    print_square(4)
"""


def text_indentation(text):
    """prints a given text after replace all symbols . : and ? for two new lines
    and remove blank spaces at first and end

    Args:
        text (str): string to be printed

    Returns:
        Doesn't return

    Raises:
        TypeError: when text is not a string
    """
    out = ''
    if type(text) != str:
        raise TypeError("text must be a string")

    for letter in text:
        out += letter

        if letter in '.?:':
            out += '\n\n'

    out = out.splitlines()

    for i, line in enumerate(out):
        if i != 0:
            print()
        print(line.strip(), end='')
