#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list_copy = my_list[:]
    my_list_copy.reverse()
    for number in my_list_copy:
        print("{}".format(number))
