#!/usr/bin/python3
""" module for read file function
"""


def read_file(filename=""):
    """ read the file called filename and doesn't returns nothing
    """
    with open(filename, 'r', encoding='utf-8') as open_file:
        print(open_file.read(), end='')
