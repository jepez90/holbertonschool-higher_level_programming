#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list) != 0:
        return sum([a * b for a, b in my_list]) / sum([b for a, b in my_list])
    return 0
