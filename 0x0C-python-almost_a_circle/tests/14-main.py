#!/usr/bin/python3
""" 14-main """
import sys
import os
sys.path.append(os.path.abspath('..'))
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    dictionary = r1.to_dictionary()
    json_dictionary = Base.to_json_string([dictionary])
    print(dictionary)
    print(type(dictionary))
    print(json_dictionary)
    print(type(json_dictionary))

    dictionaries = [dictionary]

    r2 = Square(10, 4, 2, 8)
    dictionaries.append(r2.to_dictionary())
    json_dictionary = Base.to_json_string(dictionaries)
    print(dictionaries)
    print(type(dictionaries))
    print(json_dictionary)
    print(type(json_dictionary))
