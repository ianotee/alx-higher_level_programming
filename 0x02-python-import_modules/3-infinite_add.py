#!/usr/bin/python3

if __name__ == "__main__":
    """This program prints the number of arguments."""
    import sys

    overal = 0
    for m in range(len(sys.argv) - 1):
        overal += int(sys.argv[m + 1])
    print("{}".format(overal))
