#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status."""

import requests


if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io/status")
    response = r.text
    print("Body response:")
    print("\t- type:", type(response))
    print("\t- content:", response)
