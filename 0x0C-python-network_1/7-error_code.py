#!/usr/bin/python3
"""Script that sends request to URL and displays the response"""


from requests import get
from sys import argv

def error():
    """Script that sends request to URL and displays the response"""
    request = get(argv[1])
    if request.status_code >= 400:
        print("Error code: {}".format(request.status_code))
    else:
        print(request.text)


if __name__ == "__main__":
    error()