#!/usr/bin/python3
"""
This is a square class
"""


class Square:

    """
    This is a square class
    """

    def __init__(self, size=0, position=(0, 0)):
        self.__position = position

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
        try:
            self.__size = value
            if value < 0:
                raise ValueError
            if type(value) is not int:
                raise TypeError
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        return self.__size

    @size.setter
    def position(self, value):
        self.__position = value

    def area(self):
        self.area = self.__size * self.__size
        return self.area

    def my_print(self):
        for i in range(0, self.__size):
            for i in range(0, self.__position[0]):
                print(' ', end='')
            for i in range(0, self.__size):
                print('#', end='')
            print('')
