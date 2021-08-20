#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the X-Request-Id
"""


if __name__ == "__main__":
    from sys import argv
    import urllib.request
    with urllib.request.urlopen(argv[1]) as response:
        print(response.getheader('X-Request-Id'))
