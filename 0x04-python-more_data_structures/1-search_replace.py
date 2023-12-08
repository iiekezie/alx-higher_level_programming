#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list or not isinstance(my_list, list):
        return None
    new_list = [replace if x == search else x for x in my_list]
    return new_list
