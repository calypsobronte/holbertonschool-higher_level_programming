#!/usr/bin/python3
import urllib.request
from sys import argv


if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': argv[2]})
    data = data.encode('ascii')
    with urllib.request.urlopen(argv[1], data) as response:
        print(response.read().decode('utf-8'))
