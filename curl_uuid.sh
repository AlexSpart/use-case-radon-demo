#!/usr/bin/env bash

which jq
curl -X POST "$1" -H "accept: */*" -H "Content-Type: application/json" -d "$2" | jq .uuid | tr -d \" 
