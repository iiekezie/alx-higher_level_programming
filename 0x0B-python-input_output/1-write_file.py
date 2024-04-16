#!/usr/bin/python3

"""Module defining a function to write a string to a text file"""



def read_lines(filename="", nb_lines=0):
    """
    return lines readed
    """
    with open(filename, mode='r', encoding="utf-8") as f:
        #  nb_lines is lower or equal to 0
        if nb_lines <= 0:
            print(f.read(), end="")
        else:
            for i in range(nb_lines):
                print(f.readline(), end="")
