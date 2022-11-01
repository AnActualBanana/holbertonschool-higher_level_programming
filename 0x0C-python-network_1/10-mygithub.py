#!/usr/bin/python3
"""Script that takes your GitHub credentials and displays your id"""


from requests import get
from requests.auth import HTTPBasicAuth
from sys import argv

def github():
    """Uses the GitHub APY to display your id"""
    requests = get('https://api.github.com/user',
                   auth=HTTPBasicAuth(argv[1], argv[2])).json()
    print(requests.get('id'))


if __name__ == "__main__":
    github()