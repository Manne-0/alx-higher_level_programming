#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newList = my_list.copy()
    listlen = len(my_list)
    if idx < 0:
        return newList
    elif idx > listlen - 1:
        return newList
    else:
        newList[idx] = element
        return newList
