#!/usr/bin/python3
""" Defines Base class """


class Base:
    """ Defines a Base from geometry objects
    """
    __nb_objects = 0
    __msg_integer_error = "{} must be an integer"

    def __init__(self, id=None):
        self.id = id

    @property
    def id(self):
        """ integer that identify the object, is given when constructor is
        called or obtains from the __nb_objects class atribute """
        return self.__id

    @id.setter
    def id(self, value):
        if value is None:
            type(self).__nb_objects += 1
            self.__id = self.__nb_objects
        else:
            self.validate_integer("id", value)
            self.__id = value

    @classmethod
    def validate_integer(cls, name, value):
        """ check if  value is an int, otherwaise, raise an type error

        args:
            name (str): name of the evaluate value, this arg is insert in the
                error mensage
            value (int): value to be checked

        raises:
            TypeError: when the given value is not an integer
        """
        if type(value) is not int:
            raise TypeError(cls.__msg_integer_error.format(name))
