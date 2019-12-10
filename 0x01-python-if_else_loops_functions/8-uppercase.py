#!/usr/bin/python3
def uppercase(str):
    str = str + "\n"
    for i in str:
        letter = "abcdefghijklmnopqrstuvwxyz"
        if i in letter:
            letter = ord(i) - 32
        else:
            letter = ord(i)
        print("{:c}".format(letter), end='')
