#!/usr/bin/python3
"""function that reads a file and prints it to stdout"""


def read_file(filename=""):
    """reads a file, prints it"""
    with open(filename, encoding="utf-8") as file:
        read_data = file.read()
        print("{}".format(read_data), end='')
