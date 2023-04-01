#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status."""
import urllib.request


if __name__ == "__main__":
    request = urllib.request.Request("https://intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print(" "*4 + "- type: {}".format(type(body)))
        print(" "*4 + "- content: {}".format(body))
        print(" "*4 + "- utf8 content: {}".format(body.decode("utf-8")))
