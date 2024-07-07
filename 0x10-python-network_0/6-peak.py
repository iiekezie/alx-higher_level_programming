#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): List of unsorted integers.

    Returns:
        int or None: The peak element in the list, \
                or None if the list is empty.
    """
    if not list_of_integers:
        return None

    right = 0
    left = len(list_of_integers) - 1

    while right < left:
        mid = (right + left) // 2
        if list_of_integers[mid] <= list_of_integers[mid + 1]:
            right = mid + 1
        else:
            left = mid

    return list_of_integers[right]