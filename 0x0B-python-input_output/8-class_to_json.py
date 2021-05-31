#!/usr/bin/python3
""" module for class_to_json function
"""
import json


def class_to_json(obj):
    """ return the __dict__ information of the given object
    """
    return obj.__dict__
