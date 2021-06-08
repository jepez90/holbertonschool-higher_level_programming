#!/usr/bin/python3
""" Defines Rectangle class """
from models.base import Base


class Rectangle(Base):
    """ Defines a rectangle representation. inherits if Base class
    """

    __msg_negative_error = "{} must be >= 0"
    __msg_neg_or_0_error = "{} must be > 0"
    PROPERTIES = ('id', 'width', 'height', 'x', 'y')

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

    def area(self):
        """ Calc the area of the rectangle (width * height) and return it """
        return (self.width * self.height)

    def display(self):
        """ prints a representation of the square by # """
        print('\n' * self.y, end='')
        for i in range(self.height):
            print(' ' * self.x, end='')
            print('#' * self.width)

    def update(self, *args, **kwargs):
        """ change the properties by way list or dictionary
        if only values are passed, it will be interpreted as in __properties
        """
        if args is not None and len(args) != 0:
            # search the arg name in __properties class attribute
            for i, arg in enumerate(args):
                if i < len(type(self).PROPERTIES):
                    setattr(self, type(self).PROPERTIES[i], arg)
        else:
            if kwargs is not None:
                for arg_name, arg in kwargs.items():
                    if arg_name in type(self).PROPERTIES:
                        setattr(self, arg_name, arg)

    def to_dictionary(self):
        """ that returns the dictionary representation of a Rectangle """
        dictionary = {}
        for prop in type(self).PROPERTIES:
            dictionary[prop] = getattr(self, prop)

        return dictionary

    def __str__(self):
        txt = "[Rectangle] ({}) {}/{} - {}/{}"
        return txt.format(self.id, self.x, self.y, self.width, self.height)
