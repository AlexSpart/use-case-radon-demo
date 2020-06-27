#!/usr/bin/env bash

curl -X POST "$1" -H "accept: */*" -H "Content-Type: application/json" -d "$2" | /home/jenkins/.local/bin/yq .uuid | tr -d \" 



