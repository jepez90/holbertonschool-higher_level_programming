#!/usr/bin/python3
"""Modulo Empty Square

this module define an empty class Square

"""


class Square():
    """Empty class Square

    this is an empty class that define an square

    """
    def __init__(self, size):
        """Constructor of the class

        Args:
            size (int): the initial size of the square, can't be negative
        """
        self.__size = size
