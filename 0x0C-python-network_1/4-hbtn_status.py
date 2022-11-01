#!/usr/bin/python3
"""script that fetches status of hbtn intranet"""


from requests import get

def status():
    """fetches status of hbtn intranet"""
    request = get("https://intranet.hbtn.io/status")
    text = request.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))


if __name__ == "__main__":
    status()