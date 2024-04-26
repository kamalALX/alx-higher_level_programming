#!/usr/bin/python3
""" a Python script that takes in a URL.
- sends a request to the URL
- displays the value of the X-Request-Id variable found in the header of the response.
"""


if __name__ == "__main__":
    import urllib.request
    import sys
    import urllib.parse

    url = sys.argv[1]
    value = {"email": sys.srgv[2]}

    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
