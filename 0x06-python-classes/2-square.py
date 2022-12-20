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
