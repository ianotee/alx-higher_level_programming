#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    else:
        max_lin = my_list[0]
        for m in range(len(my_list)):
            if my_list[m] > max_lin:
                max_lin = my_list[m]
        return (max_lin)
