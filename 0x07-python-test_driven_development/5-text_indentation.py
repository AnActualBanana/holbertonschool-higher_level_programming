#!/usr/bin/python3
def text_indentation(text):
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")
    else:
        replace(".", ".\n\n")
        replace("?", "?\n\n")
        replace(":", ":\n\n")
        replace("\n ", "\n")
