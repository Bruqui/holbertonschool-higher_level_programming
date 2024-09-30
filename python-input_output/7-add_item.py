#!/usr/bin/python3
"""
This script adds all command-line arguments to a list and saves them
to a JSON file named add_item.json.
"""
from sys import argv
import os
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"
my_list = []
if os.path.exists(filename):
    my_list = load_from_json_file(filename)
my_list.extend(argv[1:])
save_to_json_file(my_list, filename)
