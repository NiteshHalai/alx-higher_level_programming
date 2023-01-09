#!/usr/bin/python3
"""
This is a class
"""


class MyList(list):
    """
    This is a function
    """
    
    def print_sorted(self):
        a = self.copy()
        print(sorted(a))
        return sorted(a)
