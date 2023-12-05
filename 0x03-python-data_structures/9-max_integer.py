#!/usr/bin/python3
# 9-max_integer.py
# Ifeanyi I Ekezie
def max_integer(my_list=[]):
    # Initialize the max value to None
    max_value = None
    for num in my_list:
        if max_value is None or num > max_value:
            max_value = num
    return max_value

if __name__ == "__main__":
    my_list = [1, 90, 2, 13, 34, 5, -13, 3]
    max_value = max_integer(my_list)
    print("Max: {}".format(max_value))
