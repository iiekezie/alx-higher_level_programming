#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Use the symmetric difference operator ^ to get the elements that are in either set but not both
    return set_1 ^ set_2
