#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    index = 0
    while index < x:
        try:
            print("{:d}".format(my_list[index]), end='')
            counter += 1
            index += 1
        except TypeError:
            index += 1
        except ValueError:
            index += 1
    print()
    return counter
