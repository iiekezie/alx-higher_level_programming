#!/usr/bin/python3

def magic_calculation(a, b):
    """Handle basic arithmetic operations."""
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for letter in range(4, 6):
            c = add(c, letter)
        return (c)

    else:
        return(sub(a, b))
