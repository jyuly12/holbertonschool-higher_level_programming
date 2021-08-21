#!/usr/bin/python3
"""
Takes your GitHub credentials (username and password) and uses the GitHub API
"""


if __name__ == "__main__":
    from sys import argv
    from requests import auth
    import requests
    url = 'https://api.github.com/user'
    user = argv[1]
    password = argv[2]
    response = requests.get(url, auth=auth.HTTPBasicAuth(user, password))
    print(response.json().get('id'))
