#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return False
    except TypeError as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return False
