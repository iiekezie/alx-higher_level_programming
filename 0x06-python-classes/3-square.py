#!/usr/bin/python3


class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            # otherwhise raise a TypeError
            raise TypeError("size must be an integer")
        # if size is less than 0
        if size < 0:
            # raise a ValueError
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return (self.__size ** 2)
