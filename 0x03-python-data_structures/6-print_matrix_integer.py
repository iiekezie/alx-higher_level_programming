#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers.

    Args:
        matrix (list of lists of ints, optional): The matrix to print. Defaults to [[]].
    """
    for row in matrix:
        # Print each item of the row, separated by a space, and formatted as an integer
        print(" ".join("{:d}".format(item) for item in row))
