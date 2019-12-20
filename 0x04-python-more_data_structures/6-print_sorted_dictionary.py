#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for result_keys in sorted(a_dictionary.keys()):
        print("{}: {}".format(result_keys, a_dictionary[result_keys]))
