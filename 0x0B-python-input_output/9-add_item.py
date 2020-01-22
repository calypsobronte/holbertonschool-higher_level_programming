#!/usr/bin/python3
import sys


""" import of moduls """
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

point = sys.argv[1:]

try:
    file_list = load_from_json_file("add_item.json")
except IOError:
    file_list = []
save_to_json_file(file_list + point, "add_item.json")
