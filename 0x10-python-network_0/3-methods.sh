#!/bin/bash
# Curl
curl -sI "$1" | grep Allow: | cut -d " " -f2-