#!/usr/bin/python3

"""Function description here"""


def write_file(filename="", text=""):
    """Function description here"""
    with open(filename, encoding="utf-8", access_mode="w") as f:
        f.write(text)
