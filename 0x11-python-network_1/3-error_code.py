#!/usr/bin/python3
""" a scrip that akes in a URL
- sends a request to the URL
- displays the body of the response (decoded in utf-8).
"""
import urllib
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as res:
            print(res.read().decode('UTF_8'))
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)
