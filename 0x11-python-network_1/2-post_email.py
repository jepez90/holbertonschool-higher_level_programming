#!/usr/bin/python3
""" takes in a URL and an email, sends a POST request to the passed URL with
the email as a parameter, and displays the body of the response
(decoded in utf-8)
"""
import urllib
import sys


def dataEncode(**kwargs):
    """ encode any number of params as data for the request """
    data = urllib.parse.urlencode(kwargs)
    return data.encode('utf-8')

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # add the variable to the request
    data = dataEncode(email=email)
    request = urllib.request.Request(url, data)

    # execute the request and show the response
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
