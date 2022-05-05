#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    str = "{}"
    i = len(my_list) - 1
    for i in range(len(my_list) - 1, -1, -1):
        print(str.format(my_list[i]))
