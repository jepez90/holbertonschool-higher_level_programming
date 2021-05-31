#!/usr/bin/python3
""" Student module
"""


class Student:
    """ Class Student

    Attributes:
        first_name (str): firdt name of the student
        last_name (str): firdt name of the student
        age (int): age of the student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__

        my_dict = {}
        if type(attrs) == list:
            for i in attrs:
                if i in self.__dict__:
                    my_dict[i] = self.__dict__[i]

        return my_dict
