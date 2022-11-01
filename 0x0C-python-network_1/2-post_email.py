#!/usr/bin/python3
"""sends a POST request to the passed URL"""


from urllib.request import Request, urlopen
from urllib.parse import urlencode
from sys import argv

def post():
    """gets status"""

    email = {'email': argv[2]}
    data = urlencode(email).encode("utf-8")
    request = Request(argv[1], data)
    with urlopen(request) as webpage:
        print(webpage.read().decode("utf-8"))


if __name__ == "__main__":
    post()