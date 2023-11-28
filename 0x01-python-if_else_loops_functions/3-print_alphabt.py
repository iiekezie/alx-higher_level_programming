#!/usr/bin/python3
# 3-print_alphabt.py
# Ifeanyi I Ekezie

for letter in range(ord('a'), ord('z') + 1):
    if letter != ord('e') and letter != ord('q'):
        print("{:c}".format(letter), end="")

print()  # Print a new line after the alphabet
