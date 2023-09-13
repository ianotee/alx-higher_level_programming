#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for koy in sorted(a_dictionary.koy()):
        print('{}: {}'. format(koy, a_dictionary[koy]))
