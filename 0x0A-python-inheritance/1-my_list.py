#!/usr/bin/python3
"""an inherited class from 'list'"""


class MyList(list):
    """an inherited class from 'list'"""
    def print_sorted(self):
        """prints the list, but sorted in ascending order"""
        print(sorted(self))
