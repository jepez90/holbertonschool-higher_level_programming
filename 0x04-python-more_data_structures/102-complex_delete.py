#!/usr/bin/python3
def complex_delete(a_dictionary, value):

    if value in a_dictionary.values():

        keys = list(a_dictionary.keys())

        for key in keys:
            if a_dictionary[key] == value:
                del a_dictionary[key]

    return a_dictionary
