#!/usr/bin/python3
"""
This is a square class
"""


class Square:

    """
    This is a square class
    """

    def __init__(self, size=0):
        self.__size = size

    def size(self):
        return self.__size

    def size(self, value):
        self.__size = value

    def area(self):
        self.area = self.size * self.size
        return self.area
