#!/usr/bin/python3
"""
This module shows the last 10 commits of a repository
handling the format "<sha>: <author name>"
"""


if __name__ == "__main__":
    from sys import argv
    import requests
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    response = requests.get(url).json()
    for commit in response[0:10]:
        user = commit.get("commit").get("author").get("name")
        commit_id = commit.get("sha")
        print("{}: {}".format(commit_id, user))
