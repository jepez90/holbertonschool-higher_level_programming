#!/usr/bin/python3
""" module for append_write function
"""


def append_write(filename="", text=""):
    """ write the content of text into the file called filename and
    returns the number of characters written.
    it doesn't overrite the file content

    args:
        filename (str): name of the file to be written.
        text (str): string to be written in the file
    """
    with open(filename, 'a', encoding='utf-8') as output_file:
        return output_file.write(text)
