#!/usr/bin/python3
""" module for load_from_json_file function
"""
import json


def load_from_json_file(filename):
    """ read a file gived as filename and return its representation in JSON
    """
    with open(filename, 'r', encoding='utf-8') as input_file:
        return json.load(input_file)
