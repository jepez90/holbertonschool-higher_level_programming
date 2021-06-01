#!/usr/bin/python3
import os, sys
sys.path.append(os.path.abspath('..'))
append_write = __import__('2-append_write').append_write

nb_characters_added = append_write("file_append.txt", "Holberton School is so cool!\n")
print(nb_characters_added)
