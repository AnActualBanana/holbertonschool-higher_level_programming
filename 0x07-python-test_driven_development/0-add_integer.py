#!/usr/bin/python3
"""

add_integer is a function which adds two integers
"""
def add_integer(a, b=98):
    """

    >>>add_integer(2, 2)
    4
    >>>add_integer(1)
    99
    >>>add_integer(5.3, 5.8)
    10
    >>>add_integer(none)
    TypeError: a must be an integer
    >>>add_integer(a, "string")
    TypeError: b must be an integer
    >>>add_integer(-4, -4)
    -8
    >>>add_integer(5, none)
    TypeError: b must be an integer
    >>>add_integer(False, 5)
    TypeError: a must be an integer
    >>>add_integer(5.8)
    103
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    if a is None or b is None:
        return
    return(a + b)
