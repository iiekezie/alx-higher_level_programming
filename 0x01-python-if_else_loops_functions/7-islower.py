#!/usr/bin/python3
# 7-islower.py
# Ifeanyi I Ekezie

def islower(c):
    # Check if the ASCII value of the character is within the range of lowercase letters
    return ord('a') <= ord(c) <= ord('z')
