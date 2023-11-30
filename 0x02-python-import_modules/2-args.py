#!/usr/bin/python3
# 2-args.py
# Ifeanyi I Ekezie
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys
    a = len(sys.argv)
    if a == 1:
        print("{:d} arguments.".format(a - 1))
    elif a == 2:
        print("{:d} argument:".format(a - 1))
        print("{:d}: {:s}".format(a - 1, sys.argv[1]))
    else:
        print("{:d} arguments:".format(a - 1))
        for letter in range(a):
            if letter == 0:
                continue
            print("{:d}: {:s}".format(letter, sys.argv[letter]))
