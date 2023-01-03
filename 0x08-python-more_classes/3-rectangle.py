#!/usr/bin/python3
"""
This is a Rectangle class
"""


class Rectangle:

    """
    This is a Rectangle class
    """

    def __init__(self, width=0, height=0):
        try:
            self.__width = width
            if width < 0:
                raise ValueError
            if type(width) is not int:
                raise TypeError
        except TypeError:
            raise TypeError("width must be an integer")
        except ValueError:
            raise ValueError("width must be >= 0")

        try:
            self.__height = height
            if height < 0:
                raise ValueError
            if type(height) is not int:
                raise TypeError
        except TypeError:
            raise TypeError("height must be an integer")
        except ValueError:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        try:
            self.__width = value
            if value < 0:
                raise ValueError
            if type(value) is not int:
                raise TypeError
        except TypeError:
            raise TypeError("width must be an integer")
        except ValueError:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        try:
            self.__height = value
            if value < 0:
                raise ValueError
            if type(value) is not int:
                raise TypeError
        except TypeError:
            raise TypeError("height must be an integer")
        except ValueError:
            raise ValueError("height must be >= 0")

    def area(self):
        self.area = self.__width * self.__height
        return self.area

    def perimeter(self):
        self.perimeter = self.__width * 2 + self.__height * 2
        return self.perimeter
