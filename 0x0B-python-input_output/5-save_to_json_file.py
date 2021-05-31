#!/usr/bin/python3
""" module for save_to_json_file function
"""
import json


def save_to_json_file(my_obj, filename):
    """write the content of my_obj into the file called filename in JSON format

    args:
        my_obj (:): object to be written in the file
        filename (str): name of the file to be written.
    """
    with open(filename, 'w', encoding='utf-8') as output_file:
        json.dump(my_obj, output_file)
