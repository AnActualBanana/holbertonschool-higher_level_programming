#!/usr/bin/python3
"""Script that fetches status of hbtn intranet"""


from requests import get
from sys import argv

def response():
    """gets response id"""
    request = get(argv[1])
    print(request.headers.get('X-Request-Id'))


if __name__ == "__main__":
    response()