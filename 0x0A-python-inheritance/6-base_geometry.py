#!/usr/bin/python3
""" This module define a basic class BaseGeometry
"""


class BaseGeometry():
    """ This is a basic class BaseGeometry

    Raises:
        Exception: when area method is called
    """

    def area(self):
        raise Exception("area() is not implemented")
