#!/usr/bin/python3
""" a Python script that
- takes in a URL
- sends a request to the URL
- and displays the body of the response.
"""
import request
import sys


if __name__ == '__main__':
    url = sys.argv[1]

    try:
        r = requests.get(url)
        print(r.text)
    except:
        code = r.status_code
        if code >= 400:
            print("Error code:", code)
