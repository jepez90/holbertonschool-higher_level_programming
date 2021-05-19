#!/usr/bin/python3
"""Modulo Empty Square

this module define an empty class Square

"""


class Square():
    """Empty class Square

    this is an empty class that define an square

    """
    def __init__(self, size=0):
        """Constructor of the class

        Args:
            size (int): the initial size of the square, can't be negative
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
