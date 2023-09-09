#!/usr/bin/python3

def no_c(my_string):
    updated = ''
    for n in my_string:
        if n != 'c' and n != 'C':
            updated += n
    return (updated)
