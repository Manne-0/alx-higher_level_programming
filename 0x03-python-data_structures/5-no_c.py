#!/usr/bin/python3
def no_c(my_string):
    if my_string[:]:
        firstString = my_string.translate({ord("c"): None})
        newString = firstString.translate({ord("C"): None})
        return newString
    return my_string
