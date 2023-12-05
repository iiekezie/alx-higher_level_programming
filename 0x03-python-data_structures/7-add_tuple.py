#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Initialize the result tuple with two zeros
    result = (0, 0)
    for i in range(2):
        # Get the element from tuple_a or 0 if it does not exist
        a = tuple_a[i] if i < len(tuple_a) else 0
        b = tuple_b[i] if i < len(tuple_b) else 0
        result = result[:i] + (a + b,) + result[i+1:]
    # Return the result tuple
    return result
