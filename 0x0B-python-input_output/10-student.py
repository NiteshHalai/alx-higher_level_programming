#!/usr/bin/python3
"""
This is a Student class
"""


class Student:

    """
    This is a Student class
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dict = self.__dict__
        if attrs is None:
            return dict
        else:
            return {key: dict[key] for key in attrs}
