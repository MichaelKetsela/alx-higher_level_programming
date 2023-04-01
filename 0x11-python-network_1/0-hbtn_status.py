#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status."""
import urllib.request


req = ("https://intranet.hbtn.io/status")
with urllib.request.urlopen(req) as response:
    body = response.read()

print("Body response:\n\t- type: {}".format(type(body)))
print("\t- content: {}".format(body))
print("\t- utf8 content: {}".format(body.decode("utf-8")))
