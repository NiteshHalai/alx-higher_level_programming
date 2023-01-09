#!/usr/bin/python3
"""
This is a class
"""


class MyList(list):
    """
    This is a class
    """

    def print_sorted(self):
        """ This is my function """
        a = self.copy()
        print(sorted(a))
        return sorted(a)
