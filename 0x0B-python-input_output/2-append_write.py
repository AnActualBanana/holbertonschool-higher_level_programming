#!/usr/bin/python3
"""appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """appends a string to file, returns number of characters added"""
    with open(filename, "a", encoding="utf-8") as file:
        r = file.write(text)
        return r
