#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv)
    if i == 1:
        print("{:d} arguments.".format(i - 1))
    elif i == 2:
        print("{:d} argument:".format(i - 1))
        print("{:d}: {}".format(i - 1, sys.argv[1]))
    elif i > 2:
        print("{:d} arguments:".format(i - 1))
        for x in range(1, i):
            print("{:d}: {}".format(x, sys.argv[x]))
