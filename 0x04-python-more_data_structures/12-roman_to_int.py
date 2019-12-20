#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    convert_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if len(roman_string) > 0:
        vlr_previous = 0
    for letter in roman_string:
        if letter in convert_roman:
            vlr_actual = convert_roman[letter]
        else:
            return 'no'
        if vlr_previous >= vlr_actual:
            result += vlr_actual
        else:
            result += vlr_actual - (2 * vlr_previous)
        vlr_previous = vlr_actual
    return result
