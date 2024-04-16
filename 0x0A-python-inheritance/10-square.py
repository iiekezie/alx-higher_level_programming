#!/usr/bin/python3
"""Module defining a class Square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square"""
    def __init__(self, size):
        """ constructor, init square """
        if self.integer_validator("size", size) is None:
            self.__size = size

        super().__init__(size, size)

    def area(self):
        """ returns the rectangle area """
        return (self.__size * self.__size)
