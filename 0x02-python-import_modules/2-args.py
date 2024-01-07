#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    x = len(sys.argv) - 1
    if x < 1:
        print("{} arguments.".format(x))
    elif x == 1:
        print("{} argument:".format(x))
    else:
        print("{} arguments:".format(x))
    for argument in range(x):
        print("{}: {}".format(argument + 1, sys.argv[argument + 1]))
