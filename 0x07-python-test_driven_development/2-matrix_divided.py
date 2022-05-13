#!/usr/bin/python3
"""Divides all elements of a matrix"""


def matrix_divided(matrix, div):
    def_list_len = len(matrix[0])
    current_row = -1
    current_num = -1
    for check_row in matrix:
        current_row += 1
        if len(matrix[current_row]) != def_list_len:
            raise TypeError("Each row of the matrix must have the same size")
        for check_num in matrix:
            current_num += 1
            if isinstance(check_row[current_num], int) is False and \
               isinstance(check_row[current_num], float) is False:
                    raise TypeError("matrix must be a matrix (list of lists) of\
 integers/foats")
        current_num = -1
    if isinstance(div, float) is False and isinstance(div, int) is False:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return ([list(map(lambda i: round(i / div, 2), row)) for row in matrix])
