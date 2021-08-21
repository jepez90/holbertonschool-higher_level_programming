#!/usr/bin/python3
"""  takes in a URL, sends a request to the URL and displays the body of the
response (decoded in utf-8).
"""
import urllib
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    # add the variable to the request
    request = urllib.request.Request(url)

    # execute the request and show the response
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
