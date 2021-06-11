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
        """ save a list of objects serialized in a json file """
        file_name = cls.__name__ + ".json"
        list_of_dicts = []
        if list_objs is not None:
            for obj in list_objs:
                list_of_dicts.append(obj.to_dictionary())
        with open(file_name, 'w', encoding='utf8') as file:
            file.write(cls.to_json_string(list_of_dicts))

    @classmethod
    def create(cls, **dictionary):
        """ return an instance of a object with the attr in dictionary  """
        instance = cls(1, 1)
        # if cls is square, x = 1 then now reset it
        instance.x = 0
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """ return a list of instances with the attributes in the file  """
        list_of_instances = []
        file_name = cls.__name__ + '.json'
        try:
            with open(file_name, 'r', encoding='utf8') as file:
                list_of_dict = Base.from_json_string(file.read())
        except:
            list_of_dict = []

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
        """ obtains the json object from a formatting string  """
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save a list of objects serialized in a csv file """
        file_name = cls.__name__ + ".csv"
        list_dictionaries = []
        for obj in list_objs:
            list_dictionaries.append(obj.to_dictionary())
        with open(file_name, 'w', encoding='utf8') as file:
            file.write(cls.to_csv_string(list_dictionaries))

    @classmethod
    def load_from_file_csv(cls):
        """ return a list of instances with the attributes in the csv file  """
        list_of_instances = []
        file_name = cls.__name__ + '.csv'
        try:
            with open(file_name, 'r', encoding='utf8') as file:
                list_of_dict = Base.from_csv_string(file.read())
        except:
            list_of_dict = []

        for dictionary in list_of_dict:
            list_of_instances.append(cls.create(**dictionary))
        return list_of_instances

    @staticmethod
    def to_csv_string(list_dictionaries):
        """ obtains the string csv representation from an object  """
        string = ""
        if list_dictionaries is not None or list_dictionaries != []:
            for dictionary in list_dictionaries:
                string += (str(dictionary["id"]) + ',')
                if "size" in dictionary:
                    string += (str(dictionary["size"]) + ',')
                else:
                    string += (str(dictionary["width"]) + ',')
                    string += (str(dictionary["height"]) + ',')
                string += (str(dictionary['x']) + ',')
                string += (str(dictionary['y']) + '\n')
        return string

    @staticmethod
    def from_csv_string(csv_string):
        """ obtains the object from a formatting csv string  """
        if csv_string is None or csv_string == "":
            return []
        else:
            list_od_dict = []
            csv_lines = csv_string.splitlines()
            for line in csv_lines:
                new_dict = {}
                list_numbers = line.split(',')
                new_dict['id'] = int(list_numbers[0])
                if len(list_numbers) == 4:
                    new_dict['size'] = int(list_numbers[1])
                    new_dict['x'] = int(list_numbers[2])
                    new_dict['y'] = int(list_numbers[3])
                else:
                    new_dict['width'] = int(list_numbers[1])
                    new_dict['height'] = int(list_numbers[2])
                    new_dict['x'] = int(list_numbers[3])
                    new_dict['y'] = int(list_numbers[4])
                list_od_dict.append(new_dict)
            return list_od_dict
