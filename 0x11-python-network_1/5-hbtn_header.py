#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the X-Request-Id
"""


if __name__ == "__main__":
    from sys import argv
    import requests
    response = requests.get(argv[1])
    print(response.headers.get('X-Request-Id'))
