#!/usr/bin/python3
""" takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
The letter must be sent in the variable q
"""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    query = ""
    if len(sys.argv) > 1:
        query = sys.argv[1]

    data = {"q": query}

    # execute the request
    response = requests.post(url, data)

    try:
        jsonResponse = response.json()

        if len(jsonResponse) == 2:
            print("[{}] {}".format(jsonResponse["id"], jsonResponse["name"]))
        else:
            print("No result")

    except Exception as error:
        print("Not a valid JSON")

    response.close()
