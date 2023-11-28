#!/usr/bin/python3
# 2-print_alphabet.py
# Ifeanyi I Ekezie

for letter in range(ord('a'), ord('z') + 1):
    print("{:c}".format(letter), end="")

print()  # Print a new line after the alphabet
