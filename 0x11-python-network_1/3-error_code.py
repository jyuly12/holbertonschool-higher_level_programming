#!/usr/bin/python3
"""
sends a request to the URL and displays the body of the response).
"""


if __name__ == "__main__":
    from sys import argv
    import urllib.parse
    import urllib.error
    import urllib.request
    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
