#!/usr/bin/env bash

curl -X POST "$1" -H "accept: */*" -H "Content-Type: application/json" -d "$2" | /home/jenkins/.local/lib/python3.6/site-packages/jq .uuid | tr -d \" 
