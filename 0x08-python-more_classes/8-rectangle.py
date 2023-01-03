#!/usr/bin/python3
"""
This is a Rectangle class
"""


class Rectangle:

    """
    This is a Rectangle class
    """
    number_of_instances = 0

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

        Rectangle.number_of_instances = + 1
        self.number_of_instances = Rectangle.number_of_instances
        self.print_symbol = '#'

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if rect_1.area < rect_2.area():
            return rect_2

    def __repr__(self):
        return "Rectangle(%r, %r)" % (self.__width, self.__height)

    def __str__(self):
        a = []
        for i in range(0, self.__height):
            a.append(self.print_symbol * self.__width)
        return "\n".join(a)

    def __del__(self):
        Rectangle.number_of_instances = - 1
        print('Bye rectangle...')
