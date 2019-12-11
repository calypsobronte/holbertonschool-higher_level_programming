#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        str = str[:n] + str[1 + n:]
    return str
