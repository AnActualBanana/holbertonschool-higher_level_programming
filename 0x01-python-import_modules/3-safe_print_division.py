#!/usr/bin/python3
import sys

def safe_print_division(a, b):
    try:
        quotient = a / b
    except:
        quotient = "none"
        raise Exception("Divide by 0 error")
        print("Divide by 0 error", file = sys.stderr)
    finally:
        print("Inside result: {}".format(quotient))
        return(quotient)
