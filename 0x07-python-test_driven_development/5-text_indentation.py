#!/usr/bin/python3
def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    else:
        lr = text
        band = 0
        for i in range(len(lr)):
            if band == 0 and lr[i] == " ":
                band = 0
                continue
            band = 1
            if (band == 1) and (lr[i] == '?' or lr[i] == '.' or lr[i] == ':'):
                print(lr[i])
                print()
                band = 0
            else:
                print(lr[i], end='')
