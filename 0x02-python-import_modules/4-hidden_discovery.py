#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    funtionName = dir()
    for name in range(0, len(functionName)):
        if funtionName[name][:2] != "__":
            print("{:s}".format(functionName[name]))
