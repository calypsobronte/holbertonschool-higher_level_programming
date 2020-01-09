#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(args[0], args[1])
        return result
    except ValueError as msg_error:
        print("Exception: {}".format(msg_error), file=sys.stderr)
        return(None)
    except TypeError as msg_error:
        print("Exception: {}".format(msg_error), file=sys.stderr)
        return None
    except ZeroDivisionError as msg_error:
        print("Exception: {}".format(msg_error), file=sys.stderr)
        return None
    except IndexError as msg_error:
        print("Exception: {}".format(msg_error), file=sys.stderr)
        return None
