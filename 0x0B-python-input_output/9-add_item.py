#!/usr/bin/python3
import sys


""" import of moduls """
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

if __name__ == "__main__":

    try:
        file_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        file_list = []
        file_list.extend(sys.argv[1:])
        save_to_json_file(file_list, "add_item.json")
