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
            Base.__nb_objects += 1
            self.__id = Base.__nb_objects
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
        file_name = cls.__name__ + ".json"
        list_of_dicts = []
        if list_objs is not None:
            for obj in list_objs:
                list_of_dicts.append(obj.to_dictionary())
        with open(file_name, 'w', encoding='utf8') as file:
            file.write(cls.to_json_string(list_of_dicts))

    @classmethod
    def save_to_file_csv(cls, list_objs):
        file_name = cls.__name__ + ".csv"
        string = ""
        for obj in list_objs:
            string.append(obj.to_dictionary())
        with open(file_name, 'w', encoding='utf8') as file:
            file.write(cls.to_json_string(string))

    @classmethod
    def create(cls, **dictionary):
        instance = cls(1, 1)
        # if cls is square, x = 1 then now reset it
        instance.x = 0
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """ return a list of instances with the attributes in the file  """
        list_of_instances = []
        list_of_dict = []
        file_name = cls.__name__ + '.json'
        with open(file_name, 'r', encoding='utf8') as file:
            list_of_dict = Base.from_json_string(file.read())
        for dictionary in list_of_dict:
            list_of_instances.append(cls.create(**dictionary))
        return list_of_instances

    @staticmethod
    def to_json_string(list_dictionaries):
        """ obtains the string json representation from an object  """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries, sort_keys=True)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)
