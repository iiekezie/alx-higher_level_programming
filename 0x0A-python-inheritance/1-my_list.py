#!/usr/bin/python3
"""
Module defining a class MyList
"""


class MyList(list):
    """
    elements of the list int type
    return my list and sorted list
    """
    def print_sorted(self):
        # sorted method
        # sorted(iterable[, key][, reverse])
        print(sorted(self))
