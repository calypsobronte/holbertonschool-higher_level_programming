#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = list(set(my_list))
    num_result = 0
    for i in new_list:
        num_result += i
    return num_result
