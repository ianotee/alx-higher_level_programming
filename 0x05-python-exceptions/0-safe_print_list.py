#!/usr/bin/python3

"""This prints both integers and strings"""
def safe_print_list(my_list=[], x=0):
    sam = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            sam += 1
        except IndexError:
            break
    print()
    return(sam)
