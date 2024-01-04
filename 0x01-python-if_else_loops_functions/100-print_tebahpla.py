#!/usr/bin/python3
for alphabet in range(ord('z'), ord('a') - 1, -2):
    print("{}{}".format(chr(alphabet), chr(alphabet - 33)),
          end='')
