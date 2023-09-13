#!/usr/bin/python3


def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
num = 0
    digits = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for roman in reversed(roman_string):
        arab = digits[roman]
        num += arab if num < arab * 5 else -arab
    return num
