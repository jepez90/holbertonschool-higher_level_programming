#!/usr/bin/python3
def uppercase(str):
    for character in str:
        if ord('a') <= ord(character) <= ord('z'):
            char_upper = ord(character) - 32
        else:
            char_upper = ord(character)
        print("{:c}".format(char_upper), end="")
    print("")
