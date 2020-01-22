#!/usr/bin/python3
"""
This is module 0-read_file

This module contains one function `read_file()`
"""


def read_file(filename=""):
    """
    function that reads a text file (UTF8) and prints it to stdout

    Args:
    filename
    """
    open_file = open(filename, 'r', encoding='utf-8')
    read_file2 = open_file.read()
    print(read_file2)
    open_file.close()
