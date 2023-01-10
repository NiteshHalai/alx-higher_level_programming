#!/usr/bin/python3

"""Function description here"""


def write_file(filename="", 'a', text=""):
    """Function description here"""
    with open(filename, encoding="utf-8") as f:
        f.write(text)
