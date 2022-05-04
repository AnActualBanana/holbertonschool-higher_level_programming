#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        quotient = a / b
    except:
        quotient = "none"
        raise ValueError("Divide by 0 error")
    finally:
        print("Inside result: {}".format(quotient))
        return(quotient)
