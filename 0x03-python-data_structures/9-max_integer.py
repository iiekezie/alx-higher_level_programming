#!/usr/bin/python3
# 9-max_integer.py
# Ifeanyi I Ekezie


def max_integer(my_list=[]):
    """Initialize the max value to None"""
    if len(my_list) == 0:
        return (None)

    max_value = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > max_value:
            max_value = my_list[i]

    return (max_value)
