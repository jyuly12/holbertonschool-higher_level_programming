#!/usr/bin/python3
"""
 takes in a URL and an email, sends a POST request to the passed URL
 with the email as a parameter, and displays the body of the response
"""


if __name__ == "__main__":
    from sys import argv
    import requests
    values = {'email': argv[2]}
    response = requests.post(argv[1], data=values)
    print(response.text)
