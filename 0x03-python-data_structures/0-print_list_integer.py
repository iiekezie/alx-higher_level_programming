#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
    Print integers of a list.

    :param my_list: List of integers
    :type my_list: list
    """
    for letter in my_list:
        print("{:d}".format(letter))

# Example usage
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print_list_integer(my_list)
