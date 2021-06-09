#!/usr/bin/python3
""" Defines Base class """

import json


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

    @classmethod
    def save_to_file(cls, list_objs):
        list_dictionaries = []

        if list_objs is not None and len(list_objs) != 0:
            for object in list_objs:
                list_dictionaries.append(object.to_dictionary())

        file_name = cls.__name__ + ".json"
        with open(file_name, 'w', encoding='utf8') as file:
            json.dump(list_dictionaries, file)

    @classmethod
    def create(cls, **dictionary):
        instance = cls(1, 1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        list_of_instances = []
        file_name = cls.__name__ + '.json'
        with open(file_name, 'r', encoding='utf8') as file:
            list_of_dict =  Base.from_json_string(file.read())
        for dictionary in list_of_dict:
            list_of_instances.append(cls.create(**dictionary))
        return list_of_instances

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)
