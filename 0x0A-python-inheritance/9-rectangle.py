#!/usr/bin/python3
"""Module defining a class Rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """A class representing a rectangle"""

    def __init__(self, width, height):
        """Initializes a rectangle with a given width and height"""
        self.__width = width
        self.__height = height
        super().__init__()

        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Calculates the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

if __name__ == "__main__":
    r = Rectangle(3, 5)
    print(r)
    print(r.area())

