#!/usr/bin/python3
def safe_print_division(a, b):
    divide = None
    try:
        divide = a / b
    except ZeroDivisionError:
        pass
    finally:
        if divide is not None:
            print("Inside result: {:.1f}".format(divide))
        else:
            print("Inside result: {}".format(divide))
    return divide
