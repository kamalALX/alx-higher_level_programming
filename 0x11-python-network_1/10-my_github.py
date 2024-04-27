#!/usr/bin/python3
"""A script that:
- takes your GitHub credentials (username and password)
- uses the GitHub API to display your id
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
