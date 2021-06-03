#!/usr/bin/python3
""" This module define a basic class MyInt
"""


def add_attribute(obj, name, value):
    if "__dict__" in dir(obj):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
