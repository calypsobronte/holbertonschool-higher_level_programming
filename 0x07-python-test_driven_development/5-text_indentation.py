#!/usr/bin/python3
def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    else:
        letter = text
        band = 0
        for i in range(len(letter)):
            if band == 0 and letter[i] == " ":
                band = 0
                continue
            band = 1
            if (band == 1) and (letter[i] == '?' or letter[i] == '.' or letter[i] == ':'):
                print(letter[i])
                print()
                band = 0
            else:
                print(letter[i], end='')