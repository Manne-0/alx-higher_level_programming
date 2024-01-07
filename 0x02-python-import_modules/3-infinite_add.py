#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    addition = 0
    for argument in range(1, len(sys.argv)):
        addition += int(sys.argv[argument])
    print("{}".format(addition))
