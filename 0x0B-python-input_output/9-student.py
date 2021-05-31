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

    def to_json(self):
        return self.__dict__
