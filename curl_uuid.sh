#!/usr/bin/env bash
echo $PATH
sh 'export PATH="/home/jenkins/.local/lib/python3.6/site-packages:$PATH"'
echo $PATH

curl -X POST "$1" -H "accept: */*" -H "Content-Type: application/json" -d "$2" | jq .uuid | tr -d \" 
