#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for index in range(0, x):
            print(my_list[index], end='')
    except IndexError:
        return index
    finally:
        print()
    return index + 1
