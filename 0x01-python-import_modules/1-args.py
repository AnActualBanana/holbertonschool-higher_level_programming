#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    print("{} ".format(len(argv) - 1) ,end='')
    if len(argv) - 1 == 1:
        print("argument", end='')
    else:
        print("arguments", end='')
    if len(argv) - 1 == 0:
        print(".")
    else:
        print(":")
        for arg in range(1, len(argv)):
            print("{}: {}".format(arg, argv[arg]))
