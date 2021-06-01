#!/usr/bin/python3
import os, sys
sys.path.append(os.path.abspath('..'))
write_file = __import__('1-write_file').write_file

nb_characters = write_file("my_first_file.txt", "Holberton School is so cool!\n")
print(nb_characters)
