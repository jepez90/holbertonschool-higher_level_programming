#!/usr/bin/python3
""" fetches https://intranet.hbtn.io/status and shoe the response """
import urllib

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        html = response.read()

        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        if ("=utf-8" in response.headers.get("Content-Type")):
            print("\t- utf8 content: {}".format("OK"))
        else:
            print("\t- utf8 content: {}".format("NOT OK"))
