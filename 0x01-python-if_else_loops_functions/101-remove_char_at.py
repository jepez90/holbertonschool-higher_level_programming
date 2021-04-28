#!/usr/bin/python3
def remove_char_at(string, n):
    copy = ""
    i = 0
    for char in string:
        if i != n:
            copy += char
        i += 1

    return copy
