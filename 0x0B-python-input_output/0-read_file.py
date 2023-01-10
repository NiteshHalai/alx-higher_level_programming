#!/usr/bin/python3

"""Function description here"""


def read_file(filename=""):
    """Function description here"""
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data)
