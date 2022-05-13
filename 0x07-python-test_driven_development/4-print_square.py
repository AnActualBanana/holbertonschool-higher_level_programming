#!/usr/bin/python3
def print_square(size):
    if isinstance(size, float) is True and size < 0:
        raise TypeError("size must be an integer")
    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for lines in range(0, size):
        for hashes in range(0, size):
            print("#", end='')
        print("")
