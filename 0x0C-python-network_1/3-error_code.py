#!/usr/bin/python3
"""sends a request to the URL and displays the body as a response"""


from urllib.request import Request, urlopen
from urllib.error import HTTPError
from sys import argv

def error_code():
    """gets status of hbtn intranet"""
    request = Request(argv[1])
    try:
        with urlopen(request) as webpage:
            webpage = webpage.read()
            print(webpage.decode("utf-8"))
    except HTTPError as error:
        print("Error code: {}".format(error.code))


if __name__ == "__main__":
    error_code()