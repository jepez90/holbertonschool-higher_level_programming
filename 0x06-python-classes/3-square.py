#!/usr/bin/python3
"""Modulo 3-Square

this module define a class Square with a method area

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

    def area(self):
        """Calculate and retrun the Square area based in its size"""
        return (self.__size**2)
