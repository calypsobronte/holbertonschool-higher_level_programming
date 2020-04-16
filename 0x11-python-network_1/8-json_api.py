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
        data = req.json()
        if len(data) > 0:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
