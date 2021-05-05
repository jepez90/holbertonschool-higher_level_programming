#!/usr/bin/python3
def element_at(my_list, idx):
    for i, number in enumerate(my_list):
        if (i == idx):
            return number
    else:
        return None
