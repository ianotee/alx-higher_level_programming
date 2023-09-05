#!/usr/bin/python3
for m in range(ord('z'), ord('a') - 1, -1):
    if m % 2 == 0:
        num = 0
    else:
        num  = 32
    print('{}'.format(chr(m - num)), end='')

