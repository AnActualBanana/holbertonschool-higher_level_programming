#!/usr/bin/python3
"""Script that reqeusts to passed URL and grabs response"""


from requests import post
from sys import argv

def post():
    """script sends POST request and displays body of response"""
    email = {"email": argv[2]}
    request = post(argv[1], email)
    print(request.text)


if __name__ == "__main__":
    post()