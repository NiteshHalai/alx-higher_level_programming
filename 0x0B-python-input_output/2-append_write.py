#!/usr/bin/python3

"""Function description here"""


def append_write(filename="", text=""):
    """Function description here"""
    with open(filename, access_mode="a", encoding="utf-8") as f:
        f.write(text)
