#!/usr/bin/python3
"""function to find the peak in an unsorted list of integers

idea:       * the peak number is surrounded for numbers smaller than,
              or for a number smaller than if is in the edge of the list
            * could be more than one  peak number

inputs:     the unsorted list of integers
output:     the number considered the peak
edge cases: * the list is void
            * the list countains the same number in all positions
proccess:   1. obtains a cocpy of sorded numbers in desc order
            2. goes through the sorted list,
            3. get its index in the unsorted list
            4. check if it is a peak number

"""


def find_peak(list_of_integers):
    """ retuns a peak number from a unsorted list"""
    if list_of_integers is None or len(list_of_integers) == 0:
        return None
    list_of_integers.sort(reverse=True)
    return list_of_integers[0]
