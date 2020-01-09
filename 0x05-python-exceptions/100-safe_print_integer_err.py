#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError as msg_error:
        print("Exception: {}".format(msg_error), file=sys.stderr)
        return False
    except TypeError as msg_error:
        print("Exception: {}".format(msg_error), file=sys.stderr)
        return False
    return True
