#!/usr/bin/python3
"""Module defining a class Square"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """A class representing a square"""

    def __init__(self, size):
        """Initializes a square with a given size"""
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns a string representation of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)

if __name__ == "__main__":
    s = Square(13)
    print(s)
    print(s.area())
