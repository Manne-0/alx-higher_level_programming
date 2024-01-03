#!/usr/bin/python3
def uppercase(str):
    for char in str:
        newChar = char
        if ord(char) > 96 and ord(char) < 124:
            newChar = chr(ord(char) - 32)
        print("{}".format(newChar), end='')
    print()
