#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    [(new_list.append(x) if x != search else new_list.append(replace))
        for x in my_list]
    return new_list
