#!/usr/bin/python3
""" This module define a basic class MyInt
"""


class MyInt(int):
    """this class inherits from int and implement the methods
    __eq__ and __ne__
    """

    def __eq__(self, other_int):
        return int.__ne__(self, other_int)

    def __ne__(self, other_int):
        return int.__eq__(self, other_int)
