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
        super().__init__(size, x, y, id)
        
    def __str__(self):
        """Function description here"""
        return "[Square] (" + str(self.id) + ") " + str(self.__x) + "/" + str(self.__y) + " - " + str(self.__size)
