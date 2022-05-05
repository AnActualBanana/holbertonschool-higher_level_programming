#!/usr/bin/python3
def max_integer(my_list=[]):
    cur_int = my_list[0]
    for i in range(0, len(my_list)):
        if cur_int <= my_list[i]:
            cur_int = my_list[i]
    return(cur_int)
