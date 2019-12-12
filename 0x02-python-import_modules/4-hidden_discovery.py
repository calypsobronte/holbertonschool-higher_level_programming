#!/usr/bin/python3
# Si es igual a __ no lo imprima
if __name__ == "__main__":
    import hidden_4
    letter = dir(hidden_4)
    for i in letter:
        if i[:2] != "__":
            print(i)
