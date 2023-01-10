#!/usr/bin/python3

"""Function description here"""


def pascal_triangle(n):
    """Function description here"""

    rows = []
    if n <= 0:
        return rows
    else:
        for i in range (n):
            rows.append(11**i)
