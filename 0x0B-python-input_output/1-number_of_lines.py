#!/usr/bin/python3
def number_of_lines(filename=""):
    """
    open_file = open(filename, 'r', encoding='utf-8')
    cont_line = 0
    for lines in open_file:
        cont_line += 1
    return cont_line """

    with open(filename, 'r', encoding='utf-8') as target:
        cont_line = 0
        for lines in target:
            cont_line += 1
        return cont_line
