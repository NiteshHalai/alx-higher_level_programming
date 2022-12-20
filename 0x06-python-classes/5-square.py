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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    def area(self):
        self.area = self.__size * self.__size
        return self.area

    def my_print(self):
        for i in range (0, self.__size):
            for i in range (0, self.__size):
                print('#', end ='')
            print('')
