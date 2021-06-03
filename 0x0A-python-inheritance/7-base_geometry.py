#!/usr/bin/python3
""" This module define a basic class BaseGeometry
"""


class BaseGeometry():
    """ This is a basic class BaseGeometry

    Raises:
        Exception: when area method is called
        TypeError: when integer_validator method is called with type of
            value arg as not int
        ValueError: when integer_validator method is called with its second
        arg less or equals to 0
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if isinstance(value, int) is False:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
