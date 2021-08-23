#!/usr/bin/python3
""" takes 2 arguments in order and list 10 commits
(from the most recent to oldest) of the repository “rails” by the user “rails”
"""

import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits?per_page=10".format(owner, repo)

    response = requests.get(url)

    for commit in response.json():
        sha = commit.get("sha")
        author = commit.get("commit").get("author").get("name")
        print("{}: {}".format(sha, author))
