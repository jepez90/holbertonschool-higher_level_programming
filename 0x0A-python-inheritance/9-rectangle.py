#!/usr/bin/python3
""" This module define a basic class Rectangle that inherits of the
class BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ This is a implementation of the class Rectangle that inherits of the
    class BaseGeometry
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calc and return the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """return an representation for the rectangle in the form:
        [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
