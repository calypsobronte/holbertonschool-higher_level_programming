#!/usr/bin/python3
import requests
from sys import argv


if __name__ == "__main__":
    if requests.get(argv[1]).status_code < 400:
        print((requests.get(argv[1])).text)
    else:
        print("Error code: {}".format((requests.get(argv[1])).status_code))
