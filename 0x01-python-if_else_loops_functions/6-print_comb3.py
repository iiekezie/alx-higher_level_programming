#!/usr/bin/python3
# 6-print_comb3.py
# Ifeanyi I Ekezie

for unit_digit1 in range(0, 10):
    for unit_digit2 in range(unit_digit1 + 1, 10):
        if unit_digit1 == 8 and unit_digit2 == 9:
            print("{}{}".format(unit_digit1, unit_digit2))
        else:
            print("{}{}".format(unit_digit1, unit_digit2), end=", ")
