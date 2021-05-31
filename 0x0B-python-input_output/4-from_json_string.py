#!/usr/bin/python3
""" module for from_json_string function
"""

import json


def from_json_string(my_str):
    """ convert a string in a json formart and returns it
    """
    return json.loads(my_str)
