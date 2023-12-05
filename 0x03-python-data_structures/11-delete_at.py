#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Deletes the item at a specific position in a list
    """
    if idx >= 0 and idx < len(my_list): # check if idx is valid
        del my_list[idx] # delete the item at idx
    return my_list # return the modified list
