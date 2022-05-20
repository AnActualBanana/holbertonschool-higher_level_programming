#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, encoding="utf-8") as file:
        read_data = file.read()
        print("{}".format(read_data), end='')
