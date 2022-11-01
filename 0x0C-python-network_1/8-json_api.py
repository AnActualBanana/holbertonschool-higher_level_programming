#!/usr/bin/python3
"""Script that sends a POST request with a passed letter"""


from requests import get, post
from sys import argv

def json_api():
    """Script that sends a POST request with a passed letter"""

    if len(argv) < 2:
        q = ""
    else:
        q = argv[1]
    webpage = 'http://0.0.0.0:5000/search_user'
    request = post(webpage, data={'q': q})
    try:
        dictionary = request.json()
        id = dictionary.get('id')
        name = dictionary.get('name')
        if len(dictionary) == 0:
            print("No result")
        else:
            print("[{}] {}".format(id, name))

    except:
        print("Not a valid JSON")


if __name__ == "__main__":
    json_api()