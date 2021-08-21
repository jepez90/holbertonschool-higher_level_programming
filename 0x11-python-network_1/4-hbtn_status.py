#!/usr/bin/python3
"""  fetches https://intranet.hbtn.io/status and shw the response
(decoded in utf-8).
"""
import requests


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"

    # execute the request
    response = requests.get('https://intranet.hbtn.io/status')
    content = response.text
    response.close()

    # show the response
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
