#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Use a set to store unique integers."""
    result = 0
    for x in set(my_list):
        result += x
    # Sum all the unique integers in the set
    return (result)
