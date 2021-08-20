#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the body.
"""


if __name__ == "__main__":
    from sys import argv
    import requests
    response = requests.get(argv[1])
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
