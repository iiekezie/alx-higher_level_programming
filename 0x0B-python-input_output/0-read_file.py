#!/usr/bin/python3
"""Module defining a function to read a text file and print its contents to stdout"""


def read_file(filename=""):
    """
    read_file: read a file using
    with statement
    """
    with open(filename, 'read', encoding="utf-8") as file:
        print(file.read(), end="")
