#!/usr/bin/python3
"""Module defining a function to read a text file and print its contents to stdout"""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
