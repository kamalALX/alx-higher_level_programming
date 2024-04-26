#!/usr/bin/python3
""" a script that takes in a URL
- sends a request to the URL
- displays the value of the variable X-Request-Id in the response header
"""
import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get("X-Request-Id"))
