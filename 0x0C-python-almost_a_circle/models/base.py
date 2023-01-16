#!/usr/bin/python3
"""
This is a class
"""


class Base:
    """
    This is a class
    """

    def __init__(self, id=None):
        
        __nb_objects = 0
        
        __nb_objects = __nb_objects + 1
        
        if self.id == None:
            self.id = self.__nb_objects
        else:
            self.id = self.id
