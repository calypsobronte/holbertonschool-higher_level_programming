#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, 'r', encoding='utf-8') as target:
        if nb_lines <= 0:
            print(target.read(), end="")
        else:
            for line in range(nb_lines):
                print(target.readline(), end="")
