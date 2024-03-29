#!/usr/bin/python3
"""
This is a class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This is a class
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Function description here"""
        id1 = str(self.id)
        x = str(self.x)
        y = str(self.y)
        w = str(self.width)
        return "[Square] (" + id1 + ") " + x + "/" + y + " - " + w

    @property
    def size(self):
        """Function description here"""
        return self.width

    @size.setter
    def size(self, value):
        """Function description here"""
        self.width = value

    def to_dictionary(self):
        """Function description here"""
        pass
