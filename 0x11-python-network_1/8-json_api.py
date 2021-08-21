#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to URL with the letter
as a parameter.
"""


if __name__ == "__main__":
    import requests
    from sys import argv
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    data = {"q": q}
    response = requests.post(url, data)
    try:
        rjonson = response.json()
        if rjonson:
            print("[{}] {}".format(rjonson.get('id'), rjonson.get('name')))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
