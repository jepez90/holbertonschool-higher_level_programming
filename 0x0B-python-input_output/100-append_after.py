#!/usr/bin/python3
""" module for append_after function
"""


def append_after(filename="", search_string="", new_string=""):
    """ insert new_string in the next line of the search_string give match

    args:
        filename (str): the name of the file to modify
        search_string (str): the string to find it in the string
        new_string (str): string to be inserted in the next line where
        search_string whas find
    """
    with open(filename, "+r") as open_file:
        final_string = ''
        # reads each linw of the file
        line = open_file.readline()
        while line != '':
            # copy each line into final_string
            final_string += line
            if search_string in line:
                # if search_string exist into line, add newstring into final
                final_string += new_string
            line = open_file.readline()

        # move the cursor to begin of the file
        open_file.seek(0)

        # writes all text in the file, it overrides the content.
        open_file.write(final_string)
