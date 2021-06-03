#!/usr/bin/python3
"""Modulo 3-Square

this module define a class Square with a method area

"""


class Square():
    """Empty class Square

    this is an empty class that define an square

    __size:
    the size of the square as integer.

    _position:
    The position of the square, since the current position of the cursor, as
    a tuple of two integers.
    (x , y)
    __ __ __ x
    |
    |
    |
    y

    """

    def __init__(self, size=0, position=(0, 0)):
        """Constructor of the class

        Args:
            size (int): the initial size of the square, can't be negative
            position (int, int): the initial position of the square,
                cant be negatives
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """return the value of the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """set the value of the position of the square

        Args:
            value (int, int): the initial position of the square,
                cant be negatives
        """
        if (type(value) != tuple or
                len(value) != 2 or
                type(value[0]) != int or
                value[0] < 0 or
                type(value[1]) != int or
                value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints the Square with # symbols"""

        if self.__size == 0:
            print()
        else:
            print('\n' * self.__position[1], end='')
            for i in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
