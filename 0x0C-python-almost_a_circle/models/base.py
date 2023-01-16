#!/usr/bin/python3
"""
This is a class
"""


class Base:
    """
    This is a class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        
        Base.__nb_objects = Base.__nb_objects + 1
        
        if id is None:
            self.id = Base.__nb_objects
        else:
            self.id = id
