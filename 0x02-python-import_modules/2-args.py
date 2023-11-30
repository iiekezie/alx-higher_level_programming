#!/usr/bin/python3
# 2-args.py
# Ifeanyi I Ekezie
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    from sys import argv
    argc = len(argv) - 1
    plural_s = 's' if argc != 1 else ''
    period = '.' if argc == 0 else ':'

    print("{} argument{}{}{}".format(argc, plural_s, period, '\n' * (argc > 0)))

    for i, arg in enumerate(argv[1:], 1):
        print("{}: {}".format(i, arg))
