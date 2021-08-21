#!/usr/bin/python3
""" takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
The letter must be sent in the variable q
"""
import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/user"
    userName = sys.argv[1]
    userToken = sys.argv[2]

    # execute the request
    response = requests.get(url, auth=(userName, userToken))
    print(response.json().get("id"))

    response.close()
