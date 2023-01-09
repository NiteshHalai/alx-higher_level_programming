#!/usr/bin/python3
"""
This is a class
"""


class BaseGeometry:
    """
    This is a class
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        try:
            self.value = value
            self.name = name
            if value <= 0:
                raise ValueError
            if type(value) is not int:
                raise TypeError
        except TypeError:
            raise TypeError(name + " must be an integer")
        except ValueError:
            raise ValueError(name + " must be greater than 0")


class Rectangle(BaseGeometry):
    """
    This is a class
    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "Width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)


class Square(Rectangle):
    """
    This is a class
    """

    def __init__(self, size):
        self.__size = size
        Rectangle.integer_validator(self, "Size", self.__size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
