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
