#!/usr/bin/python3
from sys import argv
import requests


if __name__ == "__main__":
    try:
        data = argv[1]
    except IndexError:
        data = ""
    req = requests.post('http://0.0.0.0:5000/search_user', data={'q': data})
    try:
        print("[{}] {}".format(req.json().get('id'), req.json().get('name')))
    except ValueError:
        print("Not a valid JSON")
    except KeyError:
        print("No result")
