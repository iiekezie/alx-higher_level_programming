#!/usr/bin/python3
# 8-multiple_returns.py
# Ifeanyi I Ekezie
def multiple_returns(sentence):
    result = (None, None)
    length = len(sentence)
    first = sentence[0] if length > 0 else None
    result = (length, first)
    return result
