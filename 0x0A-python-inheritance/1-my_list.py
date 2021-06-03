#!/usr/bin/python3
""" This module define a basic class MyList
"""


class MyList(list):
    """this class inherits from list and implement the method print_sorted"""

    def print_sorted(self):
        print(sorted(self))
