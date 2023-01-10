#!/usr/bin/python3

"""Function description here"""


def pascal_triangle(n):
    """Function description here"""
    if n <= 0:
        return []
    else:
        for i in range (n):
            print([int(x) for x in str(11**i)])
