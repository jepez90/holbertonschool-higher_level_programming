#!/usr/bin/python3
""" This module define a basic class Square that inherits of the
class Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Basic class Square that inherits of the class Rectangle """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calc and return the area of the square"""
        return self.__size**2
