#!/usr/bin/python3
def add_attribute(cla, attri, value):
    if not hasattr(cla, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(cla, attri, value)
