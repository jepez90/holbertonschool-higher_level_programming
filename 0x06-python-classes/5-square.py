#!/usr/bin/python3
"""Modulo 3-Square

this module define a class Square with a method area

"""


class Square():
    """Empty class Square

    this is an empty class that define an square

    __size:
    the size of the square as integer.

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
        """Calculate and retrun the area of the square based in its size"""
        return (self.__size**2)

    @property
    def size(self):
        """returns the size of the Square"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size of the Square
        Args:
            value (int): the initial size of the square, can't be negative
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """prints the Square with # symbols"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
