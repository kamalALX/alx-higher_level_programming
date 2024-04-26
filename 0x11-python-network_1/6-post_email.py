#!/usr/bin/python3
""" a script that takes in a URL
- sends a request to the URL
- displays the value of the variable X-Request-Id in the response header
"""
import requests
import sys

if __name__ == "__main__":
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
