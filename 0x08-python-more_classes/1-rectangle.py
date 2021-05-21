#!/usr/bin/python3
"""Modulo Empty Rectangle

This module defines basic class Rectangle
"""


class Rectangle():
    """basic class Rectangle

    This class define an rectangle

    Attributes:
        width (int): define the width of the rectangle
        height (int): define the height of the rectangle

    Raises:
        TypeError: when the width or hight are not integers
        ValueError: when the width or height are less than 0
    """

    def __init__(self, width=0, height=0):
        """build an rectangle and set its initial with and height

        Args:
            width (int): initial with of the rectangle
            height (int): initial height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of the rectangle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
