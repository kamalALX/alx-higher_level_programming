#!/usr/bin/python3
""" a Python script that takes in a letter and
- sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    headers = {'Authorization': f"token {token}"}
    api_url = f"https://api.github.com/users/{username}"

    r = requests.get(api_url, headers=headers)
    print(r.json().get("id"))
