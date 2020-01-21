#!/usr/bin/python3
def read_file(filename=""):
    """ Read from a text file """
    open_file = open(filename, 'r', encoding='utf-8')
    read_file2 = open_file.read()
    print(read_file2)
    open_file.close()
