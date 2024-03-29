#!/usr/bin/python3
"""
This is a class
"""

from models.base import Base


class Rectangle(Base):
    """
    This is a class
    """

    def __init__(self, width, height, x=0, y=0, id=None):

        try:
            self.__width = width
            if width <= 0:
                raise ValueError
            if type(width) is not int:
                raise TypeError
        except TypeError:
            raise TypeError("width must be an integer")
        except ValueError:
            raise ValueError("width must be > 0")

        try:
            self.__height = height
            if height <= 0:
                raise ValueError
            if type(height) is not int:
                raise TypeError
        except TypeError:
            raise TypeError("height must be an integer")
        except ValueError:
            raise ValueError("height must be > 0")

        try:
            self.__x = x
            if x < 0:
                raise ValueError
            if type(x) is not int:
                raise TypeError
        except TypeError:
            raise TypeError("x must be an integer")
        except ValueError:
            raise ValueError("x must be >= 0")

        try:
            self.__y = y
            if y < 0:
                raise ValueError
            if type(y) is not int:
                raise TypeError
        except TypeError:
            raise TypeError("y must be an integer")
        except ValueError:
            raise ValueError("y must be >= 0")

        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        try:
            self.__width = value
            if value <= 0:
                raise ValueError
            if type(value) is not int:
                raise TypeError
        except TypeError:
            raise TypeError("width must be an integer")
        except ValueError:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def width(self, value):
        try:
            self.__height = value
            if value <= 0:
                raise ValueError
            if type(value) is not int:
                raise TypeError
        except TypeError:
            raise TypeError("height must be an integer")
        except ValueError:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        try:
            self.__x = value
            if value < 0:
                raise ValueError
            if type(value) is not int:
                raise TypeError
        except TypeError:
            raise TypeError("x must be an integer")
        except ValueError:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        try:
            self.__y = value
            if value < 0:
                raise ValueError
            if type(value) is not int:
                raise TypeError
        except TypeError:
            raise TypeError("y must be an integer")
        except ValueError:
            raise ValueError("y must be >= 0")

    def area(self):
        """Function description here"""
        self.area = self.__width * self.__height
        return self.area

    def display(self):
        """Function description here"""
        for x in range(self.__y):
            print('')
        for j in range(self.__height):
            print(' ' * self.__x, end='')
            for i in range(self.__width):
                print('#', end='')
            print('')

    def __str__(self):
        """Function description here"""
        id1 = str(self.id)
        x = str(self.__x)
        y = str(self.__y)
        w = str(self.__width)
        h = str(self.__height)
        return "[Rectangle] (" + id1 + ") " + x + "/" + y + " - " + w + "/" + h

    def update(self, *args, **kwargs):
        """Function description here"""
        if args is not None:
            attr = [self.id, self.__width, self.__height, self.__x, self.__y]

            for i in range(len(args)):
                attr[i] = args[i]

            self.id = attr[0]
            self.__width = attr[1]
            self.__height = attr[2]
            self.__x = attr[3]
            self.__y = attr[4]

        if len(args) == 0:
            self.id = kwargs.get('id', self.id)
            self.__width = kwargs.get('width', self.__width)
            self.__height = kwargs.get('height', self.__height)
            self.__x = kwargs.get('x', self.__x)
            self.__y = kwargs.get('y', self.__y)

    def to_dictionary(self):
        """Function description here"""
        pass
