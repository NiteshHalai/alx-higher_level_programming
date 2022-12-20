#!/usr/bin/python3
"""
This is a square class
"""


class Square:

    """
    This is a square class
    """

    def __init__(self, size=0):
        try:
            self.__size = size
            if size < 0:
                raise ValueError
            if type(size) is not int:
                raise TypeError
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    def area(self):
        self.area = self.__size * self.__size
        return self.area
