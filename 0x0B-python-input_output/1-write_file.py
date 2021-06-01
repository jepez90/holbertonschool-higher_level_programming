#!/usr/bin/python3
""" module for write_file function
"""


def write_file(filename="", text=""):
    """ write the content of text into the file called filename and
    returns the number of characters written

    args:
        filename (str): name of the file to be written.
        text (str): string to be written in the file
    """
    with open(filename, 'w', encoding='utf-8') as output_file:
        return output_file.write(text)
