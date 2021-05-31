#!/usr/bin/python3
""" module for to_json_string function
"""
import json


def to_json_string(my_obj):
    """ interpret my_obj as json an return it
    """
    return json.dumps(my_obj)
