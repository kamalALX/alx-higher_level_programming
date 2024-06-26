#!/usr/bin/python3
"""A script that takes in a URL and an email
- sends a POST request to the passed URL
- displays the body of the response
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as res:
        print(res.read().decode("utf-8"))
