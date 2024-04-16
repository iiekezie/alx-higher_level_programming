#!/usr/bin/python3
"""Module defining a class MyList"""


class MyList(list):
    """A class that inherits from list"""

    def print_sorted(self):
        """Prints the list sorted in ascending order"""
        print(sorted(self))
