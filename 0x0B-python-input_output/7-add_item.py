#!/usr/bin/python3
"""adds all arguments to a python list, and saves them to a file"""


import json
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
def main(*argv):
    """makes a list of arguments, serializes them, then makes a new object"""
    if len(sys.argv) == 1:
        return
    try:
        arg_list = load_from_json_file("add_item.json")
    except:
        arg_list = []
    for arg in range(1, len(sys.argv)):
        arg_list.append(sys.argv[arg])
    save_to_json_file(arg_list, "add_item.json")
main()
