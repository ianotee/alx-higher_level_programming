#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = []
    for key_to in a_dictionary:
        if a_dictionary[key] == value:
            keys_to.append(key)
    for key in keys_to:
        del a_dictionary[key]
    return a_dictionary
