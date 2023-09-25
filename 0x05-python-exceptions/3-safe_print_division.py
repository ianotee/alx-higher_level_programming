#!/usr/bin/python3
def safe_print_division(a, b):
    """Divides the two numbers"""
    try:
        division = a / b
    except (TypeError, ZeroDivisionError):
        division = None
    finally:
        print("Inside result: {}".format(division))
    return (division)
