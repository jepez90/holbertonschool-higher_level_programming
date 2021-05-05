#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    add = [0, 0]
    for i in range(0, 2):
        if len(tuple_a) > i:
            add[i] += tuple_a[i]
        if len(tuple_b) > i:
            add[i] += tuple_b[i]

    return tuple(add)
