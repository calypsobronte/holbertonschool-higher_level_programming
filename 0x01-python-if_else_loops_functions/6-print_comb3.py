#!/usr/bin/python3
for i in range(0, 100):
    for c in range(i + 1, 100):
        if i == 56 and c == 57:
            print("{:02d}, ".format(i))
            print("{:02d}, ".format(c))
        else:
            print("{:d}, ".format(i))
            print("{:d}, ".format(c))
