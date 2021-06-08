#!/usr/bin/python3
""" Defines Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Defines a square representation. inherits of Rectangle class
    """

    PROPERTIES = ("id", "size", "x", "y")

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ integer as the size of the square, size = width = height """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        txt = "[Square] ({}) {}/{} - {}"
        return txt.format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """ change the properties by way list or dictionary
        if only values are passed, it will be interpreted as in __properties
        """
        if args is not None and type(args) is tuple and len(args) != 0:
            # search the arg name in __properties class attribute
            for i, arg in enumerate(args):
                if i < len(type(self).PROPERTIES):
                    setattr(self, type(self).PROPERTIES[i], arg)
        else:
            if kwargs is not None:
                if type(kwargs) is dict and len(kwargs) != 0:
                    for arg_name, arg in kwargs.items():
                        if arg_name in type(self).PROPERTIES:
                            setattr(self, arg_name, arg)
