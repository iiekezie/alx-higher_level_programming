#!/usr/bin/python3
# 3-infinite_add.py
# Ifeanyi I Ekezie
from sys import argv

if __name__ == "__main__":
    args = argv[1:]
    num_args = len(args)

    if num_args == 0:
        print("0")
    else:
        i = sum(int(arg) for arg in args)
        print(i)
