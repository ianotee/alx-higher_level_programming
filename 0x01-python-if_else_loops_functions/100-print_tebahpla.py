#!/usr/bin/python3
for m in range(ord('z'), ord('a') - 1, -1):
    if m % 2 == 0:
        nom = 0
    else:
        nom = 32
    print('{}'.format(chr(m - nom)), end='')

