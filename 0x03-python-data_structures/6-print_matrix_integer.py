#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for now in matrix:
        for col in now:
            if col == now[-1]:
                print('{:d}'.format(col), end='')
            else:
                print('{:d}'.format(col), end=' ')
        print()
