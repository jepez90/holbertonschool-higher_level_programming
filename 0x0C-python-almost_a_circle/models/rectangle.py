#!/usr/bin/python3
""" Defines Rectangle class """
from models.base import Base


class Rectangle(Base):
    """ Defines a rectangle representation. inherits if Base class
    """

    __msg_negative_error = "{} must be >= 0"
    __msg_neg_or_0_error = "{} must be > 0"

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ integer that represents the width of the the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        type(self).validate_integer("width", value)
        if value <= 0:
            raise ValueError(self.__msg_neg_or_0_error.format("width"))
        self.__width = value

    @property
    def height(self):
        """ integer that represents the height of the the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        type(self).validate_integer("height", value)
        if value <= 0:
            raise ValueError(self.__msg_neg_or_0_error.format("height"))
        self.__height = value

    @property
    def x(self):
        """ integer that represents the position in the `x` axis (positive to
        rigth) of the the rectangle """
        return self.__x

    @x.setter
    def x(self, value):
        type(self).validate_integer("x", value)
        if value < 0:
            raise ValueError(self.__msg_negative_error.format("x"))
        self.__x = value

    @property
    def y(self):
        """ integer that represents the position in the `y` axis (positive to
        down) of the the rectangle """
        return self.__y

    @y.setter
    def y(self, value):
        type(self).validate_integer("y", value)
        if value < 0:
            raise ValueError(self.__msg_negative_error.format("y"))
        self.__y = value
