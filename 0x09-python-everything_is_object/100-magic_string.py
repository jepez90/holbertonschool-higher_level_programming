#!/usr/bin/python3
def magic_string():
    magic_string.i = magic_string.i + 1 if "i" in magic_string.__dict__ else 0
    return ("Holberton, " * magic_string.i) + "Holberton"
